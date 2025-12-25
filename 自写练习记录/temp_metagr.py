import paddle
import paddle.nn as nn
import paddle.nn.functional as F
from typing import Optional, Dict


class PositionalEncoding(nn.Layer):
    """
    Sin-cos positional encoding (same dims as embeddings) or learnable.
    """
    def __init__(self, d_model: int, max_len: int = 512, learnable: bool = False):
        super(PositionalEncoding, self).__init__()
        self.d_model = d_model
        self.max_len = max_len
        self.learnable = learnable

        if learnable:
            self.pos_embedding = nn.Embedding(max_len, d_model)
        else:
            # build sin/cos fixed embedding
            pe = paddle.zeros([max_len, d_model], dtype='float32')
            position = paddle.arange(0, max_len, dtype='float32').unsqueeze(1)
            div_term = paddle.exp(
                paddle.arange(0, d_model, 2, dtype='float32') * -(paddle.log(paddle.to_tensor(10000.0)) / d_model)
            ) # 指数衰减序列，使位置编码能覆盖各级别的位置信息
            pe[:, 0::2] = paddle.sin(position * div_term)
            pe[:, 1::2] = paddle.cos(position * div_term)
            # register as buffer so it is moved with .to(device)
            self.register_buffer('pe', pe)  # shape [max_len, d_model]

    def forward(self, seq_len: int, device=None):
        if self.learnable:
            idx = paddle.arange(seq_len, dtype='int64')
            if device is not None:
                idx = idx.copy_to(device)
            return self.pos_embedding(idx)
        else:
            return self.pe[:seq_len, :]


class FieldAwareEmbedding(nn.Layer):
    """
    Feature embedding + field embedding (additive) so each token carries its field id info.
    Inputs are integer ids for feature and field.
    字段感知型embedding，给feature一个field-aware偏移量，embedding = feature_vector + field_bias
    """
    def __init__(self, vocab_size: int, field_num: int, emb_dim: int, padding_idx: int = 0):
        super(FieldAwareEmbedding, self).__init__()
        self.feature_emb = nn.Embedding(vocab_size, emb_dim, padding_idx=padding_idx)
        self.field_emb = nn.Embedding(field_num, emb_dim)

    def forward(self, feature_ids: paddle.Tensor, field_ids: paddle.Tensor) -> paddle.Tensor:
        # both tensors: [B, L]
        f_e = self.feature_emb(feature_ids)
        fld_e = self.field_emb(field_ids)
        return f_e + fld_e


class AttentionPooling(nn.Layer):
    """
    Simple attention pooling: compute a weighted sum of sequence tokens to a vector.
    """
    def __init__(self, d_model: int):
        super(AttentionPooling, self).__init__()
        self.w = nn.Linear(d_model, 1, bias_attr=False)

    def forward(self, seq_emb: paddle.Tensor, mask: Optional[paddle.Tensor] = None) -> paddle.Tensor:
        # seq_emb: [B, L, D]
        logits = self.w(seq_emb).squeeze(-1)  # [B, L]
        if mask is not None:
            logits = logits + (mask.astype('float32') - 1.0) * 1e9
        weights = F.softmax(logits, axis=-1).unsqueeze(-1)  # [B, L, 1]
        out = paddle.sum(seq_emb * weights, axis=1)  # [B, D]
        return out


class MetaGRTransformerEncoder(nn.Layer):
    """
    Transformer encoder that ingests a unified meta-sequence.
    Uses Paddle's TransformerEncoder.
    """
    def __init__(self, d_model:int=256, nhead:int=8, num_layers:int=2, dim_feedforward:int=1024, dropout:float=0.1):
        super(MetaGRTransformerEncoder, self).__init__()
        # build a stack of TransformerEncoderLayer + TransformerEncoder
        encoder_layer = nn.TransformerEncoderLayer(d_model=d_model, nhead=nhead,
                                                   dim_feedforward=dim_feedforward, dropout=dropout,
                                                   activation='gelu')
        self.encoder = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)

    def forward(self, x: paddle.Tensor, src_mask: Optional[paddle.Tensor] = None):
        # Paddle's Transformer expects shape [L, B, D]
        # Accept x: [B, L, D]
        x = x.transpose([1, 0, 2]) # 将[B, L, D]transpose成[L, B, D]
        if src_mask is not None:
            # src_mask expected shape [L, L] or [B*H, L, L] depending on API; keep None for simplicity
            out = self.encoder(x, src_mask)
        else:
            out = self.encoder(x)
        out = out.transpose([1, 0, 2])  # [B, L, D]
        return out


class MetaGRNet(nn.Layer):
    """
    Meta-Graph Recommender style unified-sequence model.

    Expected inputs (packed in a dict):
      - feature_ids: LongTensor [B, L]  (global vocab id for each token)
      - field_ids: LongTensor [B, L]    (which feature domain each token belongs to)
      - seq_len: LongTensor or int (sequence length L)
      - mask: optional Bool/Byte tensor [B, L] where 1 indicates valid token
      - dense_feats: optional FloatTensor [B, d] (other numerical features)

    Output: logits or score [B, 1]
    """
    def __init__(self,
                 vocab_size: int,
                 field_num: int,
                 emb_dim: int = 256,
                 max_seq_len: int = 128,
                 transformer_layers: int = 2,
                 transformer_heads: int = 8,
                 transformer_ffn_dim: int = 1024,
                 mlp_hidden: int = 512,
                 dropout: float = 0.1,
                 use_learnable_pos: bool = False,
                 pooling: str = 'attn'  # 'cls' or 'attn' or 'mean'
                 ):
        super(MetaGRNet, self).__init__()
        self.emb_dim = emb_dim
        self.vocab_size = vocab_size
        self.field_num = field_num
        self.padding_idx = 0

        # embeddings
        self.token_field_emb = FieldAwareEmbedding(vocab_size=vocab_size, field_num=field_num, emb_dim=emb_dim,
                                                   padding_idx=self.padding_idx)
        self.pos_enc = PositionalEncoding(d_model=emb_dim, max_len=max_seq_len, learnable=use_learnable_pos)

        # optional cls token (learnable)
        self.use_cls = (pooling == 'cls')
        if self.use_cls:
            self.cls_token = paddle.create_parameter(shape=[1, 1, emb_dim], dtype='float32', default_initializer=nn.initializer.Constant(0.0))

        # transformer encoder
        self.encoder = MetaGRTransformerEncoder(d_model=emb_dim, nhead=transformer_heads, num_layers=transformer_layers,
                                                dim_feedforward=transformer_ffn_dim, dropout=dropout)

        # pooling
        if pooling == 'attn':
            self.pool = AttentionPooling(emb_dim)
        elif pooling == 'mean':
            self.pool = lambda seq, mask=None: paddle.sum(seq * mask.unsqueeze(-1).astype('float32'), axis=1) / (paddle.sum(mask.astype('float32'), axis=1, keepdim=True) + 1e-9)
        elif pooling == 'cls':
            self.pool = None
        else:
            raise ValueError('unknown pooling: %s' % pooling)

        # final MLP head
        self.mlp = nn.Sequential(
            nn.Linear(emb_dim + (0 if mlp_hidden == 0 else 0), mlp_hidden),
            nn.Silu(),
            nn.Dropout(dropout),
            nn.Linear(mlp_hidden, 1)
        )

    def forward(self, inputs: Dict[str, paddle.Tensor]) -> paddle.Tensor:
        # parse inputs
        feature_ids = inputs['feature_ids']               # [B, L]
        field_ids = inputs['field_ids']                   # [B, L]
        mask = inputs.get('mask', None)                   # [B, L] (1 for valid)
        dense = inputs.get('dense_feats', None)           # [B, D]

        B, L = feature_ids.shape

        # token + field embedding
        x = self.token_field_emb(feature_ids, field_ids)  # [B, L, D]

        # positional encoding (additive)
        pos = self.pos_enc(L)
        # pos has shape [L, D]
        pos = pos.unsqueeze(0)  # [1, L, D]
        x = x + pos

        # if using cls pooling, prepend cls token
        if self.use_cls:
            cls = self.cls_token.tile([B, 1, 1])  # [B,1,D]
            x = paddle.concat([cls, x], axis=1)  # [B, L+1, D]
            if mask is not None:
                mask = paddle.concat([paddle.ones([B,1], dtype=mask.dtype), mask], axis=1)

        # encoder (Transformer)
        enc_out = self.encoder(x)  # [B, L, D]

        # pooling
        if self.use_cls:
            pooled = enc_out[:, 0, :]
        else:
            if isinstance(self.pool, AttentionPooling):
                pooled = self.pool(enc_out, mask)
            else:
                pooled = self.pool(enc_out, mask)

        # optionally concat dense features
        if dense is not None:
            pooled = paddle.concat([pooled, dense.astype('float32')], axis=1)

        # MLP head -> score
        score = self.mlp(pooled)
        return score


# ------------------ example usage ------------------
if __name__ == '__main__':
    B = 4
    L = 16
    vocab_size = 50000
    field_num = 12
    emb_dim = 128

    net = MetaGRNet(vocab_size=vocab_size, field_num=field_num, emb_dim=emb_dim, max_seq_len=64,
                    transformer_layers=2, transformer_heads=4, pooling='attn')

    feature_ids = paddle.randint(0, vocab_size, shape=[B, L], dtype='int64')
    field_ids = paddle.randint(0, field_num, shape=[B, L], dtype='int64')
    mask = paddle.randint(0, 2, shape=[B, L], dtype='int64')

    outputs = net({'feature_ids': feature_ids, 'field_ids': field_ids, 'mask': mask})
    print('score shape:', outputs.shape)  # [B, 1]
