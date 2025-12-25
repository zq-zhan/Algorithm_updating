# scaled dot-product attention: 用向量点积衡量Query和Key的相关性,再用根号d把数值拉回到可训练区间,使softmax保持有效梯度,从而实现高效稳定的序列建模
# attention(Q, K, V) = softmax(Q*K^T/sqrt(d_k)) * V
#       Q, K, V: query, key, value, d_k: key的维度
#       softmax: 对每一个Q,K,V,计算出一个概率分布(归一化),概率越大,表示Q,K,V越相关
#       Q*K^T: 表示Query和Key的相关程度
#       /sqrt(d_k): 缩放因子,防止数值过大,导致softmax输出趋于0或1
#       *V: 加权和后的value
# scaled dot-product attention的优点:
#       计算简单,可并行,矩阵乘法友好,适合长序列

import paddle
import paddle.nn as nn
import paddle.nn.functional as F
import math

class PositionalEncoding(nn.Layer):
    """
        可学习的位置编码
    """
    def __init__(self, max_len, embed_dim):
        super().__init__()
        self.pos_embed = self.create_parameter(
            shape = [max_len, embed_dim],
            dtype = 'float32',
            default_initializer = nn.initializer.XavierUniform()
        )
    
    def forward(self, x):
        # x: [B, T, D]
        T = x.shape[1]
        pos = self.pos_embed[:T, :] # [T, D],取前T个位置的位置编码
        pos = pos.unsqueeze(0) # [1, T, D]
        return x + pos # bradcast to [B, T, D]

class FeedForward(nn.Layer):
    """
        transformer中的前馈子层(两层线性+激活)
    """
    def __init__(self, embed_dim, ffn_dim, dropout):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(embed_dim, ffn_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(ffn_dim, embed_dim),
            nn.Dropout(dropout)
        )
    
    def forward(self, x):
        return self.net(x)
    
class EncoderLayer(nn.Layer):
    """
        Transformer中的编码层
        - self-Attention -> Add & Norm
        - FeedForward -> Add & Norm
    """
    def __init__(self, embed_dim, num_heads, ffn_dim, dropout):
        super().__init__()
        self.self_attn = nn.MultiHeadAttention(embed_dim, num_heads, dropout) 
        self.norm1 = nn.LayerNorm(embed_dim)
        self.dropout1 = nn.Dropout(dropout)

        self.ffn = FeedForward(embed_dim, ffn_dim, dropout)
        self.norm2 = nn.LayerNorm(embed_dim)

    def forward(self, x, src_mask = None):
        # x: [B, T, D]
        att = self.self_attn(x, x, x, attn_mask = src_mask) # [B, T, D], padding_mask
        x = x + self.dropout1(att) 
        x = self.norm1(x)

        f = self.ffn(x)
        x = x + f
        x = self.norm2(x)
        return x

class DecoderLayer(nn.Layer):
    """
        Transformer中的解码层
        - Masker self-Attention -> Add & Norm
        - Cross-Attention (query from decoder, key/value from encoder) -> Add & Norm
        - FeedForward -> Add & Norm 
    """
    def __init__(self, embed_dim, num_heads, ffn_dim, dropout):
        super().__init__()
        self.self_attn = nn.MultiHeadAttention(embed_dim, num_heads, dropout)
        self.norm1 = nn.LayerNorm(embed_dim)
        self.dropout1 = nn.Dropout(dropout)

        self.cross_attn = nn.MultiHeadAttention(embed_dim, num_heads, dropout)
        self.norm2 = nn.LayerNorm(embed_dim)
        self.dropout2 = nn.Dropout(dropout)

        self.ffn = FeedForward(embed_dim, ffn_dim, dropout)
        self.norm3 = nn.LayerNorm(embed_dim)

    def forward(self, x, memory, tgt_mask = None, memory_mask = None):
        # x: [B, T_tgt, D],即T_q; memory: [B, T_src, D],即T_kv
        att = self.self_attn(x, x, x, attn_mask = tgt_mask) # [B, T_tgt, D], masked self-attn, decode block的第一个多头注意力采用masked操作, casual_mask
        x = x + self.dropout1(att)
        x = self.norm1(x)

        att2 = self.cross_attn(x, memory, memory, attn_mask = memory_mask) # [B, T_tgt, D], cross-attn, decode block的第二个多头注意力, K&V矩阵使用encoder的输出计算, attention_mask使用encoder的padding mask
        x = x + self.dropout2(att2)
        x = self.norm2(x)

        f = self.ffn(x)
        x = x + f
        x = self.norm3(x)
        return x
    
class TransformerModel(nn.Layer):
    """
        Transformer模型 (encoder-deocder结构)
        输入参数:
            vocab_size_src: 源语言词表大小
            vocab_size_tgt: 目标语言词表大小
            embed_dim: 词向量维度
            nhead: 多头注意力头数
            num_encoder_layers: 编码层数
            num_decoder_layers: 解码层数
            ffn_dim: 前馈网络中间层维度
            dropout: dropout概率
            max_len: 最大序列长度(用于位置编码)
        输出:
    """
    def __init__(self, 
                 vocab_size_src,
                 vocab_size_tgt,
                 embed_dim = 512,
                 nhead = 8,
                 num_encoder_layers = 6, 
                 num_decoder_layers = 6,
                 ffn_dim = 2048,
                 dropout = 0.1,
                 max_len = 5000,
                 share_embedding = False):
        super().__init__()

        # embedding层
        self.src_embedding = nn.Embedding(vocab_size_src, embed_dim)
        if share_embedding:
            self.tgt_embedding = self.src_embedding
        else:
            self.tgt_embedding = nn.Embedding(vocab_size_tgt, embed_dim)
        
        # 位置编码层
        self.pos_enc = PositionalEncoding(max_len, embed_dim)

        # encoder stack
        self.encoder_layers = nn.LayerList([
            EncoderLayer(embed_dim, nhead, ffn_dim, dropout)
            for _ in range(num_encoder_layers)
        ])

        # decoder stack
        self.decoder_layers = nn.LayerList([
            DecoderLayer(embed_dim, nhead, ffn_dim, dropout)
            for _ in range(num_decoder_layers)
        ])

        # 输出层
        self.output_fc = nn.Linear(embed_dim, vocab_size_tgt) # 将源序列的词向量映射到目标序列的词表空间

        self.embed_scale = math.sqrt(embed_dim)
        self.dropout = nn.Dropout(dropout)

    @staticmethod # 静态方法,定义的函数属于类的命名空间但不依赖类或实例的任何属性
    def _make_pad_mask(seq, pad_idx = 0):
        """
            生成padding mask
            seq: [B, T]
            pad_idx: padding的索引值
            输出:
                mask: [B, T], bool类型, 值为True的位置表示有效token
        """
        if seq is None:
            return None
        mask = (seq != pad_idx).astype('bool') # [B, T]
        return mask

    @staticmethod
    def _make_subsequent_mask(sz, dtype = 'bool'):
        """
            生成decoder的subsequent mask
            sz: 序列长度
            dtype: 数据类型
            输出:
                mask: [T, T], bool类型, 值为True的位置表示当前位置
        """
        mask = paddle.tril(paddle.ones((sz, sz), dtype = dtype)) # [T, T],下三角矩阵，用于控制解码器decoder在自注意力计算时只能看到自己以及之前的token
        return mask
    
    def encode(self, src, src_mask = None):
        """
            src: [B, T_src]
            src_mask: [B, T_src] boolead
            输出:
                memory: [B, T_src, D]
        """
        x = self.src_embedding(src) * self.embed_scale # [B, T, D], T = T_src * 
        x = self.pos_enc(x) 
        x = self.dropout(x)

        attn_mask = None
        if src_mask is not None:
            attn_mask = src_mask # [B, T_src]
        for layer in self.encoder_layers:
            x = layer(x, attn_mask) # [B, T_src, D]
        return x

    def decode(self, tgt, memory, tgt_mask = None, memory_mask = None):
        """
            tgt: [B, T_tgt]
            memory: [B, T_src, D]
            tgt_mask: [B, T_tgt]
            memory_mask: [B, T_src]
            输出:
                output: [B, T_tgt, D]
        """
        x = self.tgt_embedding(tgt) * self.embed_scale 
        x = self.pos_enc(x)
        x = self.dropout(x)

        for layer in self.decoder_layers:
            x = layer(x, memory, tgt_mask, memory_mask) # [B, T_tgt, D]
        return x # [B, T_tgt, D]

    def forward(self, src, tgt, src_pad_idx = 0, tgt_pad_idx = 0):
        """
            src: [B, T_src]
            tgt: [B, T_tgt]
            src_pad_idx: padding的索引值
            tgt_pad_idx: padding的索引值
            输出:
                output: [B, T_tgt, vocab_size_tgt]
        """
        src_mask = self._make_pad_mask(src, src_pad_idx) # [B, T_src]
        memory = self.encode(src, src_mask = src_mask)

        tgt_pad_mask = self._make_pad_mask(tgt, tgt_pad_idx) # [B, T_tgt]
        B, T_tgt = tgt.shape
        subsequent = self._make_subsequent_mask(T_tgt) # [T_tgt, T_tgt]
        tgt_mask = subsequent
        memory_mask = src_mask
        dec_out = self.decode(tgt, memory, tgt_maks = tgt_mask, memory_mask = memory_mask) # [B, T_tgt, D]

        logits = self.output_fc(dec_out) # [B, T_tgt, vocab_size_tgt]
        return logits




        



