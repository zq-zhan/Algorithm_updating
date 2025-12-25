import paddle
import paddle.nn as nn
import paddle.nn.functional as F
from typing import Optional, Dict

class PositionalEncoding(nn.Layer):
    '''
        位置编码
        sin-cos 或 可学习的embedding形式
    '''
    def __init__(self, d_model, max_len, learnable = False):
        super().__init__()
        self.d_model = d_model
        self.max_len = max_len
        self.learnable = learnable

        if learnable:
            self.pos_embedding = nn.Embedding(max_len, d_model)
        else:
            pe = paddle.zeros([max_len, d_model], dtype = 'float32')
            position =paddle.arange(0, max_len, dtype = 'float32').unsqueeze(1) # [max_len, 1]
            div_term = paddle.exp(
                paddle.arange(0, d_model, 2, dtype = 'float32') * -(paddle.log(paddle.to_tensor(10000.0))/d_model)
            ) # [1, d_model/2]，一维向量，指数衰减序列，使位置编码能覆盖各级别的位置信息（短距离依赖、长距离依赖）
            pe[:, 0::2] = paddle.sin(position * div_term) # 广播，[max_len, d_model/2]
            pe[:, 1::2] = paddle.cos(position * div_term)
            self.pe = pe
        
    def forward(self, seq_len, device = None):
        if self.learnable:
            idx = paddle.arange(seq_len, dtype = 'int64')
            if device is not None:
                idx = idx.to(device)
            return self.pos_embedding(idx)
        else:
            return self.pe[:seq_len, :]

class FieldAwareEmbedding(nn.Layer):
    """
        字段感知型Embedding, 给feature一个field-aware偏移量，embedding = feature_vector + field_bias
    """
    def __init__(self, vocab_size, field_num, emb_dim, padding_idx):
        super().__init__()
        self.featrue_emb = nn.Embedding(vocab_size, emb_dim, padding_idx = padding_idx)
        self.field_emb = nn.Embedding(field_num, emb_dim)

    def forward(self, feature_ids, field_ids):
        f_e = self.featrue_emb(feature_ids)
        fld_e = self.field_emb(field_ids)
        return f_e + fld_e
    
class AttentionPooling(nn.Layer):
    def __init__(self, d_model):
        super().__init__()
        self.w = nn.Linear(d_model, 1, bias_attr = False)

    def forward(self, seq_emb, mask = None):
        # seq_emb: [B, L, D]
        logits = self.w(seq_emb).squeeze(-1) # [B, L]
        if mask is not None:
            logits = logits + (mask.astype('float32') - 1.0) * 1e9
        weights = F.softmax(logits, axis = -1).unsqueeze(-1) # [B, L, 1]
        out = paddle.sum(seq_emb * weights, axis = 1) # [B, D]
        return out

class MetaGRTransformerEncoder(nn.Layer):
    def __init__(self, d_model=256, nhead=8, num_layers=2, dim_feedforward=1024, dropout=0.1):
        super().__init__()
        encoder_layer = nn.TransformerEncoderLayer(d_model, nhead, dim_feedforward, dropout, activation = 'gelu')
        self.encoder = nn.TransformerEncoder(encoder_layer, num_layers)
    
    def forward(self, x, src_mask=None):
        # x:[B, L, D]，但注意paddle.nn.TransformerEncoder只接受[L, B, D]的输入
        x = x.transpose([1, 0, 2])
        if src_mask is not None:
            out = self.encoder(x, src_mask)
        else:
            out = self.encoder(x)
        out = out.transpose([1, 0, 2]) # [B, L, D]
        return out

class MetaGRNet(nn.Layer):
    """
    Meta-Graph Recommender
    输入:
        feature_ids: [B, L]
        field_ids: [B, L]
        seq_len: L
        mask: [B, L]
        dense_feats: [B, d]
    输出:
        score: [B, 1]
    """
    def __init__(self,
                 vocab_size,
                 field_num,
                 emb_dim = 256,
                 max_seq_len = 128,
                 transformer_layers = 2,
                 transformer_heads = 8,
                 transformer_ffn_dim = 1024,
                 mlp_hidden = 512,
                 dropout = 0.1,
                 use_learnable_pos = False,
                 pooling = 'attn'):
        super().__init__()
        self.emb_dim = emb_dim
        self.vocab_size = vocab_size
        self.field_num = field_num
        self.padding_idx = 0

        # embedding
        self.token_field_emb = FieldAwareEmbedding(vocab_size, field_num, emb_dim, padding_idx=self.padding_idx)
        self.pos_enc = PositionalEncoding(d_model=emb_dim, max_len=max_seq_len, learnable=use_learnable_pos)

        # 可选的cls token
        self.use_cls = (pooling == 'cls')
        if self.use_cls:
            self.cls_token = self.create_parameter(shape=[1, 1, emb_dim], default_initializer=nn.initializer.Constant(0.0))

        # transformer encoder
        self.encoder = MetaGRTransformerEncoder(d_model=emb_dim, nhead=transformer_heads, num_layers=transformer_layers,
                                                dim_feedforward=transformer_ffn_dim, dropout=dropout)
        
        # pooling
        if pooling == 'attn':
            self.pool = AttentionPooling(d_model=emb_dim)
        elif pooling == 'mean':
            self.pool = lambda seq, mask: paddle.sum(seq * mask.unsqueeze(-1).astype('float32'), axis=1) / (paddle.sum(mask.astype('float32'), axis = 1, keepdim=True) + 1e-9)
        else:
            raise ValueError(f"Unsupported pooling type: {pooling}")
        
        # mlp
        self.mlp = nn.Sequential(
            nn.Linear(emb_dim + (0 if mlp_hidden == 0 else 0), mlp_hidden),
            nn.Silu(),
            nn.Dropout(dropout),
            nn.Linear(mlp_hidden, 1)
        )
    
    def forward(self, inputs):
        feature_ids = input['feature_ids'] # [B, L]
        field_ids = input['field_ids'] # [B, L]
        mask = input.get('mask', None) # [B, L]
        dense = input.get('dense_feats', None) # [B, d]

        B, L = feature_ids.shape

        x = self.token_field_emb(feature_ids, field_ids) # [B, L, D]

        # 位置编码
        pos = self.pos_enc(L) # [L, D]
        pos = pos.unsqueeze(0) # [B, L, D]
        x = x + pos

        # if using cls pooling, prepend cls token
        if self.use_cls:
            cls = self.cls_token.tile([B, 1, 1])  # [B,1,D]
            x = paddle.concat([cls, x], axis=1)  # [B, L+1, D]
            if mask is not None:
                mask = paddle.concat([paddle.ones([B,1], dtype=mask.dtype), mask], axis=1)

        enc_out = self.encoder(x) # [B, L, D]

        # pooling
        if self.use_cls:
            enc_out = enc_out[:, 0, :]  # [B, L, D]
        else:
            if isinstance(self.pool, AttentionPooling):
                pooled = self.pool(enc_out, mask)  # [B, D]
            else:
                pooled = self.pool(enc_out, mask)  # [B, D]

        # concat dense features
        if dense is not None:
            pooled = paddle.concat([pooled, dense.astype('float32')], axis=1)  # [B, D+d]
        
        # mlp
        score = self.mlp(pooled)
        return score
    
if __name__ == '__main__':
    B = 4
    L = 16
    vocab_size = 50000
    field_num = 12
    emb_dim = 128 # D

    net = MetaGRNet(vocab_size=vocab_size, field_num=field_num, emb_dim=emb_dim,
                    max_seq_len=64, transformer_layers=2, transformer_heads=4, pooling='attn')
    feature_ids = paddle.randint(0, vocab_size, shape=[B, L], dtype='int64')
    field_ids = paddle.randint(0, field_num, shape=[B, L], dtype='int64')
    mask = paddle.randint(0, 2, shape=[B, L], dtype='int64')

    outputs = net({'feature_ids':feature_ids, 'field_ids':field_ids, 'mask':mask})
    print('score shape:', outputs.shape) # [B, 1]