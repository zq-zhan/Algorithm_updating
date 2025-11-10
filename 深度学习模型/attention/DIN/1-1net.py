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
