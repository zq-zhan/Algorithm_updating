# item-aware Attention:当前候选item为Query,对用户历史行为进行加权,从而生成针对该item的用户兴趣表示
# 输入:
#     hist_items: [B, T] 用户历史点击的商品序列(商品id,商铺id,商品类型id),经过embedding后形成[B,T,D]
#     target_item: [B, 1] 当前候选商品(商品id,商铺id,商品类型id),经过embedding后形成[B,1,D]
# attention打分: 
#     att_weight = softmax(MLP([q, h, q-h, q*h])),q为候选item,h为第i个历史行为
#     weighted_sum/Interest(q) = sum(att_weight * h, axis = 1), [B, D]
#     weighted_sum: [B, D],对axis=1求和
# concat_vec: 拼接[Interest(q), target_item], [B, 2D]
# 输出: 
#     dnn_out = MLP(concat_vec)
#     pred = sigmoid(dnn_out)
#
#
# 为什么DIN一定要item-aware?
#     因为item-aware Attention可以捕捉到用户对不同item的偏好,从而生成针对该item的用户兴趣表示,而不是仅仅关注用户的全局平均兴趣,导致多兴趣用户被抹平
#     优缺点:
#         优点: 显示建模多兴趣,用户表示和item强相关,CTR任务强target相关性
#         缺点: 复杂度高,对每个候选item都要算一遍item,不适合召回
# 为什么要concat?
#     weighted_sum代表用户兴趣向量,target_item代表物品向量
#     attention只影响如何聚合历史行为,如果预测网络只看到weighted_item则无法知道当前item
#     weighted_sum != f(user, item),用了不代表传递了,target_item只用于算权重而不是求和,目的是从用户历史行为中提取出与当前item相关的兴趣,weighted_sum是hist_item的线性组合
#     总结:虽然weighted_sum的权重由target_item决定,但最终向量仍是hist_item的线性组合,所以需要显式拼接target_item,才能让后续网络建模捕捉user-item的非线形交互
#     concat的优势: 让模型自己学interaction(任意非线性)
#
# 为什么DIN用concat+MLP而不是点积?
#     点积attention表达能力受embedding空间限制,而DIN可以用MLP捕捉复杂的非线性匹配关系,但计算更慢
#     
# 总结:
#     DIN模型是一种item-aware Attention模型,以候选item为Query,通过对用户历史行为进行加权,
#     生成针对当前候选item的用户兴趣表示,从而解决多兴趣用户的建模问题,提升召回效果


import paddle
import paddle.nn as nn
import paddle.nn.functional as F
import math

class LocalActivationUnit(nn.Layer):
    """
    局部激活单元,用于计算目标item与每个历史行为之间的注意力权重
    输入:
        query: [B, 1, K] 当前目标item的embedding
        keys: [B, T, K] 历史行为序列embedding
    输出:
        att_weight: [B, T, 1] 每个历史行为的注意力得分
    """
    def __init__(self, embedding_dim, hidden_units=[64,32]):
        super().__init__()
        layers = []
        input_dim = embedding_dim * 4 # 拼接[e_i, e_t, e_i - e_t, e_i * e_t]
        for h in hidden_units:
            layers.append(nn.Linear(input_dim, h))
            layers.append(nn.ReLU())
            input_dim = h
        layers.append(nn.Linear(input_dim, 1)) # 输出注意力得分
        self.mlp = nn.Sequential(*layers)
    
    def forward(self, query, keys):
        B, T, K = keys.shape
        query = paddle.expand(query, shape = [B, T, K])
        inp = paddle.concat([query, keys, query - keys, query * keys], axis=-1) # [B, T, 4K]
        att_score = self.mlp(inp) # [B, T, 1]
        att_weight = F.softmax(att_score, axis=1) # 归一化
        return att_weight

class DIN(nn.Layer):
    """
    DIN模型, 用于建模用户历史兴趣对当前item的影响
    输入:
        vocab_size:词表大小
        embedding_dim: embedding维度
        hidden_units: MLP隐藏层大小列表
        seq_len: 用户历史行为序列长度
        dropout_rate: dropout比例
    """
    def __init__(self, vocab_size, embedding_dim=16, hidden_units=[128, 64], seq_len=10, dropout_rate=0.2):
        super().__init__()
        self.vocab_size = vocab_size
        self.embedding_dim = embedding_dim
        self.seq_len = seq_len

        self.embedding_dim = nn.Embedding(
            num_embeddings = vocab_size,
            embedding_dim = embedding_dim,
            weight_attr = nn.initializer.TruncatedNormal(
                mean=0.0, std=1.0/math.sqrt(embedding_dim)
            )
        )

        # 局部激活单元(注意力模块)
        self.attention = LocalActivationUnit(embedding_dim)

        # DNN
        dnn_layers = []
        input_dim = embedding_dim * 2 # 拼接用户兴趣向量+当前item向量
        for h in hidden_units:
            dnn_layers.append(nn.Linear(input_dim, h))
            dnn_layers.append(nn.ReLU())
            dnn_layers.append(nn.Dropout(dropout_rate))
            input_dim = h
        self.dnn = nn.Sequential(*dnn_layers)

        # 输出层
        self.out_layer = nn.Linear(input_dim, 1)
        self.bias = self.create_parameter(
            shape = [1], dtype = 'float32', default_initializer = nn.initializer.Constant(value=0.0)
        )
    
    def forward(self, hist_items, target_item):
        """
        输入:
            hist_items: [B, T] 用户历史点击的商品序列(商品id,商铺id,商品类型id)
            target_item: [B, 1] 当前候选商品(商品id,商铺id,商品类型id)
        输出:
            pred: [B, 1] ctr预测概率
        """
        B, T = hist_items.shape

        hist_embed = self.embedding(hist_items) # [B, T, K]
        target_embed = self.embedding(target_item) # [B, 1, K]

        # 注意力加权求和
        att_weight = self.attention(target_embed, hist_embed) # [B, T, 1]
        weighted_sum = paddle.sum(att_weight * hist_embed, axis = 1) # [B, K],对用户历史点击序列的原始embedding进行注意力权重加权求和

        # 拼接目标item的embedding与注意力加权求和的兴趣向量embedding
        concat_vec = paddle.concat([weighted_sum, target_embed.squeeze(1)], axis = -1) # [B, 2K]

        # DNN + 输出层
        dnn_out = self.dnn(concat_vec)
        logit = self.out_layer(dnn_out) + self.bias # [B, 1]
        pred = F.sigmoid(logit)
        return pred
