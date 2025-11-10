import paddle
import paddle.nn as nn
import paddle.nn.functional as F
import math

class AttentionPooling(nn.Layer):
    """
    AFM中的注意力池化层, 对两两交互向量进行attention加权求和

    输入: interaction: [B, P, K]
        B: batch_size
        P: num_pairs, (F * (F - 1) / 2), 即特征交互的数量
        K: embedding dim
    输出: pooled: [B, K]
    """
    def __init__(self, embedding_dim, attention_size = 32, dropout_rate = 0.0):
        super(AttentionPooling, self).__init__() # 继承父类初始化
        self.embedding_dim = embedding_dim
        self.attention_size = attention_size
        
        self.attention_fc = nn.Linear(embedding_dim, attention_size)
        self.attention_h = nn.Linear(attention_size, 1)
        self.dropout = nn.Dropout(dropout_rate) if dropout_rate > 0.0 else None
    
    def forward(self, interactions):
        # interactions: [B, P, K]
        attn_hidden = F.relu(self.attention_fc(interactions)) # [B, P, A]
        attn_score = self.attention_h(attn_hidden) # [B, P, 1]
        attn_weight = F.softmax(attn_score, axis = 1) # [B, P, 1], 归一化 将权重归一化到0-1之间
        weighted_interactions = paddle.sum(attn_weight * interactions, axis = 1) # [B, K],对两两特征交叉向量进行加权求和
        if self.dropout is not None:
            weighted_interactions = self.dropout(weighted_interactions)
        return weighted_interactions

class AFM(nn.Layer):
    """
        vocab_size: 词表大小
        field_num: 特征数
        embedding_dim: K
        attention_size: A
        mlp_hidden: list, MLP隐藏层大小
        dropout_rate: 
    """
    def __init__(self, vocab_size, field_num, embedding_dim=16, attention_size=32, mlp_hidden=None, dropout_rate=0.2):
        super().__init__()
        self.vocab_size = vocab_size
        self.field_num = field_num
        self.embedding_dim = embedding_dim

        self.embedding = nn.Embedding(
            num_embeddings = vocab_size,
            embedding_dim = embedding_dim,
            weight_attr = paddle.ParamAttr(
                initializer = nn.initializer.TruncatedNormal(
                    mead = 0.0, std = 1.0 / math.sqrt(embedding_dim)
                ) # 截断正态分布
            )
        )

        self.linear_embedding = nn.Embedding(
            num_embeddings = vocab_size,
            embedding_dim = 1,
            weight_attr = paddle.ParamAttr(
                initializer = nn.initializer.Constant(value=0.0)
            )
        )
        self.attention_pool = AttentionPooling(embedding_dim, attention_size, dropout_rate) # [B, K]

        if mlp_hidden is None:
            mlp_hidden = [64, 32]
        mlp_layers = []
        input_dim = embedding_dim # K,输入为attention_pool的输出
        for h in mlp_hidden:
            mlp_layers.append(nn.Linear(input_dim, h))
            mlp_layers.append(nn.ReLU())
            mlp_layers.append(nn.Dropout(p=dropout_rate))
            input_dim = h
        self.mlp = nn.Sequential(*mlp_layers) if len(mlp_layers) > 0 else None # MLP层

        self.final_linear = nn.Linear(input_dim, 1)

        self.bias = paddle.create_Parameter(shape = [1], dtype = 'float32', default_initializer = nn.initializer.Constant(value=0.0))

    def forward(self, sparse_inputs):
        """
            sparse_inputs: [B, F]
            return: [B, 1]
        """
        embed_x = self.embedding(sparse_inputs)

        linear_part = paddle.sum(self.linear_embedding(sparse_inputs), axis = 1) # [B, 1]

        B, F, K = embed_x.shape
        interactions = []
        for i in range(F - 1):
            e_i = embed_x[:, i:i+1, :] # [B, 1, K]
            e_j = embed_x[:, i+1:, :] # [B, F-i-1, K]
            inter_ij = e_i * e_j # [B, F-i-1, K]
            interactions.append(inter_ij)
        interactions = paddle.concat(interactions, axis=1) # [B, P, K]

        pooled = self.attention_pool(interactions)

        if self.mlp is not None:
            mlp_out = self.mlp(pooled)
        else:
            mlp_out = pooled
        
        attn_part = self.final_linear(mlp_out) # [B, 1]

        logit = linear_part + attn_part + self.bias # [B, 1]
        pred = F.sigmoid(logit) # [B, 1]
        return pred



