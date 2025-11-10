import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Dict, List, Optional, Tuple


class EGESLayer(nn.Module):
    '''
    EGES 聚合层(单层)
    输入：
        node_emb: [B, D], 中心节点当前的embedding
        neighBor_emb: [B, K, D], 每个中心对应的K个邻居的embedding
        edge_feat: [B, K, E], 每条边的特征
        mask: [B, K], 1 表示存在邻居，0 表示不存在邻居
    输出：
        new_node_emb: [B, out_dim]
    设计：
        用一个小MLP从(center_emb, neighbor_emb, edge_feat)  -> attention_score
        attention_score 做softmax, 得到权重 
        聚合neighbor_emb * weight, 和center_emb 拼接或加权和, 经过linear层得到新的融合embedding
    '''
    def __init__(self, in_dim: int, out_dim: int, edge_feat_dim: int = 0, hidden: int = 64, use_concat: bool = True):
        super().__init__()
        self.in_dim = in_dim
        self.out_dim = out_dim
        self.edge_feat_dim = edge_feat_dim
        self.use_concat = use_concat

        # 注意力层 MLP：
        att_in = in_dim + in_dim + edge_feat_dim
        self.att_mlp = nn.Sequential(
            nn.Linear(att_in, hidden), 
            nn.ReLU(),
            nn.Linear(hidden, 1)
        )

        # transformer层
        if use_concat:
            self.final_linear = nn.Linear(in_dim + in_dim, out_dim)
        else:
            self.center_proj = nn.Linear(in_dim, out_dim)
            self.neigh_proj = nn.Linear(in_dim, out_dim)
        
        self.reset_parameters()

    def reset_parameters(self):
        for p in self.parameters():
            if p.dim() > 1:
                nn.init.xavier_uniform_(p)
    
    def forward(self,
                node_emb: torch.Tensor,
                neighbor_emb: torch.Tensor,
                edge_feat: Optional[torch.Tensor] = None,  # 可选参数
                mask: Optional[torch.Tensor] = None) -> torch.Tensor:
        '''
        node_emb: [B, D]
        neighbor_emb: [B, K, D]
        edge_feat: [B, K, E] or None
        mask: [B, K] or None
        '''
        B, K, D = neighbor_emb.shape
        assert node_emb.shape == (B, D)

        center_expand = node_emb.unsqueeze(1).expand(-1, K, -1) # (B, K, D)

        if edge_feat is None:
            att_input = torch.cat([center_expand, neighbor_emb], dim = -1) # (B, K, 2D)
        else:
            att_input = torch.cat([center_expand, neighbor_emb, edge_feat], dim = -1) # (B, K, 2D+E)
        
        raw_scores = self.att_mlp(att_input).squeeze(-1) # (B, K)

        if mask is not None:
            mask_f = mask.float()
            neg_inf = -1e9
            raw_scores = raw_scores * mask_f + (1.0 - mask_f) * neg_inf
        
        att_weights = F.softmax(raw_scores, dim = -1) # (B, K),对最后一维做softmax

        att_weights_unsq = att_weights.unsqueeze(-1) # (B, K, 1)
        neigh_agg = torch.sum(att_weights_unsq * neighbor_emb, dim = 1) # (B, D)

        if self.use_concat:
            combined = torch.cat([node_emb, neigh_agg], dim = -1) # (B, 2D)
            out = self.final_linear(combined) # (B, out_dim)
        else:
            out = self.center_proj(node_emb) + self.neigh_proj(neigh_agg) # (B, out_dim)
        
        return F.relu(out)
    
class EGES(nn.Module):
    '''
    EGES 网络
        节点 embedding table: num_nodes * emb_dim
    节点表征学习
    '''
    def __init__(self,
                 num_nodes: int,
                 emb_dim: int = 128,
                 num_layers: int = 2,
                 edge_raw_dim: int = 0,
                 edge_feat_dim: int = 16,
                 hidden_att: int = 64,
                 use_concat: bool = True
                 ):
        super().__init__()
        self.num_nodes = num_nodes
        self.emb_dim = emb_dim
        self.num_layers = num_layers
        self.edge_raw_dim = edge_raw_dim
        self.edge_feat_dim = edge_feat_dim
        self.hidden_att = hidden_att
        self.use_concat = use_concat
    
        self.node_embeddings = nn.Embedding(num_nodes, emb_dim)

        if edge_raw_dim > 0:
            self.edge_proj = nn.Sequential(
                nn.Linear(edge_raw_dim, edge_feat_dim),
                nn.ReLU(),
                nn.Linear(edge_feat_dim, edge_feat_dim)
            )
        else:
            self.edge_proj = None
            edge_feat_dim = 0
        
        layers = []
        in_dim = emb_dim
        out_dim = emb_dim
        for i in range(num_layers):
            layers.append(
                EGESLayer(in_dim = in_dim,
                          out_dim = out_dim,
                          edge_feat_dim = edge_feat_dim,
                          hidden = hidden_att,
                          use_concat = use_concat
                          )
            )
            in_dim = out_dim
        self.layer = nn.ModuleList(layers)

        self.reset_parameters()

    def register_parameter(self):
        nn.init.xavier_uniform_(self.node_embeddings.weight)

    def forward(self,
                center_ids: torch.LongTensor,
                neighbor_ids: torch.LongTensor,
                edge_raw_feats: Optional[torch.Tensor] = None,
                mask: Optional[torch.Tensor] = None) -> torch.Tensor:
        '''
        center_ids: (B,)
        neighbor_ids: (B, K)
        edge_raw: (B, K, edge_raw_dim) or None
        mask: (B, K) or None
        返回融合后的中心节点embedding
        '''
        B, K = neighbor_ids.shape

        center_emb = self.node_embeddings(center_ids) # (B, D)
        neigh_emb = self.node_embeddings(neighbor_ids) # (B, K, D)

        if (edge_raw_feats is not None) and (self.edge_proj is not None):
            edge_feat = self.edge_proj(edge_raw_feats) # (B, K, E)
        else:
            edge_feat = None
        
        x = center_emb
        for layer in self.layer:
            x = layer(x, neigh_emb, edge_feat, mask) # (B, D)
        return x


# 假设有 1000 个节点，每个节点我们为其采样 K=5 个邻居
num_nodes = 1000
K = 5
model = EGES(num_nodes=num_nodes, emb_dim=64, num_layers=2, edge_raw_dim=1, edge_feat_dim=8)

# fake batch: 32 个中心节点
B = 32
center_ids = torch.randint(0, num_nodes, (B,))
neighbor_ids = torch.randint(0, num_nodes, (B, K))

# 假设边特征是一个标量权重（比如交互次数），放在最后一维
edge_raw_feats = torch.rand(B, K, 1)  # (B, K, 1)

# mask：全部有效（没有 padding）
mask = torch.ones(B, K)

embs = model(center_ids, neighbor_ids, edge_raw_feats, mask)  # (B, emb_dim)
print("out emb shape:", embs.shape)

# --- 简单训练示例 (如 node classification / contrastive)
# 假设我们要做简单的 self-supervised: 将中心 emb 与真实邻居 emb 相似度最大化：
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
for epoch in range(10):
    optimizer.zero_grad()
    out = model(center_ids, neighbor_ids, edge_raw_feats, mask)  # (B, D)
    # pos: mean of neighbor embeddings
    pos = model.node_embeddings(neighbor_ids).mean(dim=1)  # (B, D)
    loss = 1.0 - F.cosine_similarity(out, pos).mean()      # 尽量让相似度接近 1
    loss.backward()
    optimizer.step()
    print("epoch", epoch, "loss", loss.item())








        