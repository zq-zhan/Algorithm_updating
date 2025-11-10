import paddle
import paddle.nn as nn
import paddle.nn.functional as F
import math

class AUGRUCell(nn.Layer):
    """
    AUGRUCell: 使用注意力得分调节GRU更新,AUGRU是在GRU的更新门上插入注意力得分
        h_next = att_socre * h_candidate + (1 - att_score) * h_prev
    输入:
        x: [B, H], 通常为interest_hidden[:,t,:]
        h_prev: [B, H]
        att_score: [B, 1] 注意力得分
    输出:
        h_next: [B, H]
    """
    def __init__(self, input_size, hidden_size):
        super().__init__()
        self.gru_cell = nn.GRUCell(input_size, hidden_size) # 单个时间步处理的GRU单元
    
    def forward(self, x, h_prev, att_score):
        h_candidate = self.gru_cell(x, h_prev)
        if len(att_score.shape) == 2:
            a = att_score
        else:
            a = paddle.unsqueeze(att_score, axis = -1) # 确认是[B, 1]
        a_exp = paddle.expand(a, shape = [-1, h_candidate.shape[-1]]) # [B, H]
        h_next = a_exp * h_candidate + (1 - a_exp) * h_prev
        return h_next

class DIENNet(nn.Layer):
    """
    DIEN
    输入:
        sparse_feature_num: 词表大小
        embedding_dim: 词向量维度
        hidden_size: GRU隐藏层维度
        mlp_sizes: MLP层维度列表
    """
    def __init__(self, sparse_feature_num, embedding_dim = 16, hidden_size = 32, mlp_sizes = [64, 32], dropout_rate = 0.1):
        super().__init__()
        self.embedding = nn.Embedding(
            num_embeddings = sparse_feature_num,
            embedding_dim = embedding_dim,
            weight_attr = paddle.ParamAttr(
                initializer = nn.initializer.TruncatedNormal(mean = 0.0, std = 1.0 / math.sqrt(embedding_dim))
            )
        )
        # 兴趣提取层GRU: 提取每个时间步的兴趣表示
        self.interest_gru(embedding_dim, hidden_size)

        # self.attention = AttentionUnit(hidden_size) # 注意力层

        self.augru_cell = AUGRUCell(hidden_size, hidden_size) # 单个时间步的注意力得分调节GRU单元

        # MLP层
        mlp_layers = []
        input_dim = hidden_size + embedding_dim
        for h in mlp_sizes:
            mlp_layers.append(nn.Linear(input_dim, h))
            mlp_layers.append(nn.ReLU())
            mlp_layers.append(nn.Dropout(p = dropout_rate))
            input_dim = h
        mlp_layers.append(nn.Linear(input_dim, 1))
        self.mlp = nn.Sequential(*mlp_layers)

    def forward(self, hist_seq, target_item, seq_len = None):
        """
        输入:
            hist_seq: [B, T] 用户历史item id序列
            target_item: [B, 1] 当前候选item id
            seq_len: 
        输出:
            prob: [B, 1]
        """
        B, T = hist_seq.shape

        hist_emb = self.embedding(hist_seq) # [B, T, E]
        target_emb = self.embedding(target_item).squeeze(1) # [B, E]

        # 兴趣提取层GRU
        interest_hidden = self.interest_gru(hist_emb) # [B, T, H]

        # 注意力层
        # att_weight = self.attention(target_emb, interest_hidden) # [B, T, 1]

        # 兴趣进化层AUGRU，使用注意力得分作为每一步的门控系数
        h = paddle.zeors([B, interest_hidden.shape[-1]], dtype = interest_hidden.dtye) # 初始化一个形状为[B,H]的全0向量作为GRU的隐藏状态
        for t in range(T):
            att_score_t = F.sigmoid(
                paddle.sum(interest_hidden[:, t, :] * target_emb, axis = -1, keepdim = True)
            )
            h = self.augru_cell(interest_hidden[:, t, :], h, att_score_t)
        evolved_interest = h # [B, H]

        # 拼接
        concat_vec = paddle.concat([evolved_interest, target_emb], axis = -1) # [B, H+E]

        # 输出层
        logit = self.mlp(concat_vec)
        prob = F.sigmoid(logit)
        return prob


