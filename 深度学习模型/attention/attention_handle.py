def attention(q, k, v, mask=None):
    # q, k, v: [B, H, T, d], 即[batch_size, num_heads, seq_len, dmodel//h]
    scores = paddle.matmul(q, k.transpose([0, 1, 3, 2])) / math.sqrt(q.shape[-1])  # q * k^T = [B, H, T_q, d] * [B, H, d, T_k] = [B, H, T_q, T_k]，再除以sqrt(d)实现缩放，保证训练稳定性，以免梯度消失
    if mask is not None:
        scores += (mask * -1e9)  # 当mask值为1时把对应位置的值变成极小值,mask需扩展为[B, H, T_q, T_k]
    attn = F.softmax(scores, axis=-1) # 对T_k维度转换为概率分布,[B, H, T_q, T_k],实现每个query在所有key上的注意力权重和为1
    return paddle.matmul(attn, v) # [B, H, T_q, T_k] * [B, H, T_k, d] = [B, H, T_q, d]，对每个query把所有value加权求和（T_v = T_k）
# 总结
## 1.先用点积衡量query与每个key的相似度，并做尺度归一化
## 2.用mask屏蔽不应该看的key
## 3.对相似度做softmax得到注意力分布概率
## 4.用这个分布对values加权求和，作为每个query的输出



import paddle
import paddle.nn as nn
import paddle.nn.functional as F
import math


class SimpleMHA(nn.Layer):
    def __init__(self, d_model, num_heads):
        super().__init__()
        self.h = num_heads
        self.dk = d_model // num_heads

        self.qkv = nn.Linear(d_model, d_model * 3)
        self.out = nn.Linear(d_model, d_model)

    def forward(self, x, mask=None):
        B, T, D = x.shape

        # 1) 线性层一次性得到 QKV
        qkv = self.qkv(x)  # [B, T, 3D]
        q, k, v = paddle.split(qkv, 3, axis=-1)  # 三个 [B, T, D]

        # 2) reshape 成多头
        def split_heads(t):
            return t.reshape([B, T, self.h, self.dk]).transpose([0, 2, 1, 3])
        q, k, v = split_heads(q), split_heads(k), split_heads(v)  # [B, H, T, dk]

        # 3) 注意力
        scores = paddle.matmul(q, k.transpose([0, 1, 3, 2])) / math.sqrt(self.dk)
        if mask is not None:
            scores += (mask * -1e9)
        attn = F.softmax(scores, axis=-1)
        out = paddle.matmul(attn, v)  # [B, H, T, dk]

        # 4) 合并 heads
        out = out.transpose([0, 2, 1, 3]).reshape([B, T, D]) # [B, T, H, dk]，且H*dk=D，reshape的目的在于把每个token的所有head的输出拼接起来

        # 5) 输出线性层
        return self.out(out)
