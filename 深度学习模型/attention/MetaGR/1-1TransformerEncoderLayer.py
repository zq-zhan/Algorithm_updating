import paddle
import paddle.nn as nn
import paddle.nn.Functional as F

class PostNormTransformerEncoderLayer(nn.Layer):
    '''
        输入/输出：[L, B, D]
    '''
    def __init__(self, d_model, nhead, dim_feedforward=2048, dropout=0.1, activation='gelu'):
        super().__init__()

        # 1) Multi-Head Self Attention
        self.self_attn = nn.MultiHeadAttention(
            embed_dim = d_model, 
            num_heads = nhead,
            dropout = dropout
        )

        # 2) Feed Forward Network
        self.linear1 = nn.Linear(d_model, dim_feedforward)
        self.linear2 = nn.Linear(dim_feedforward, d_model)

        # 3) Norms
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)

        # 4) Dropout
        self.dropout1 = nn.Dropout(dropout)
        self.dropout2 = nn.Dropout(dropout)

        # 5) Activation
        if activation == 'gelu':
            self.activation = F.gelu
        elif activation == 'relu':
            self.activation = F.relu
        else:
            raise ValueError(f"activation should be 'gelu' or'relu', but got {activation}")
    
    def forward(self, src, src_mask=None):
        '''
            src: [L, B, D]
        '''
        # self-attention block
        residual = src
        attn_output = self.self_attn(
            src, src, src, attn_mask = src_mask
        ) # 输入序列相同，但实际上在训练不同的投影Q,K,V
        src = residual + self.dropout1(attn_output)
        src = self.norm1(src)

        # feed-forward block
        residual = src
        ff = self.linear2(
            self.dropout2(
                self.activation(self.linear1(src))
            )
        )
        src = residual + ff
        src = self.norm2(src)
        return src
    
