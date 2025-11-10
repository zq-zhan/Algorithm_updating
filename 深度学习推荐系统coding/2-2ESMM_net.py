import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset

# ========== 1. 构造数据集类 ==========
class MyDataset(Dataset):
    def __init__(self, uids, ages, cities, used_quota, vip_types, brands, click_labels, conversion_labels):
        self.uids = uids
        self.ages = ages
        self.cities = cities
        self.used_quota = used_quota
        self.vip_types = vip_types
        self.brands = brands
        self.click_labels = click_labels       # CTR 标签 (0/1)
        self.conversion_labels = conversion_labels  # CVR 标签 (0/1)

    def __len__(self):
        return len(self.uids)

    def __getitem__(self, idx):
        return (
            self.cities[idx],
            self.vip_types[idx],
            self.brands[idx],
            torch.tensor([self.ages[idx], self.used_quota[idx]], dtype=torch.float),
            self.click_labels[idx],
            self.conversion_labels[idx],
        )


# ========== 2. 定义 ESMM 模型（复用上面的类） ==========
class ESMM(nn.Module):
    def __init__(self, categorical_cardinalities, embedding_dims=None, num_numeric=0,
                 ctr_hidden_dims=[64, 32], ctcvr_hidden_dims=[64, 32]):
        super(ESMM, self).__init__()
        
        if embedding_dims is None:
            embedding_dims = [min(50, (cardinality+1)//2) for cardinality in categorical_cardinalities]
        self.embeddings = nn.ModuleList([
            nn.Embedding(cardinality, emb_dim)
            for cardinality, emb_dim in zip(categorical_cardinalities, embedding_dims)
        ])
        
        input_dim = sum(embedding_dims) + num_numeric
        self.ctr_layers = self._build_mlp(input_dim, ctr_hidden_dims, output_dim=1)
        self.ctcvr_layers = self._build_mlp(input_dim, ctcvr_hidden_dims, output_dim=1)
        self.sigmoid = nn.Sigmoid()
    
    def _build_mlp(self, input_dim, hidden_dims, output_dim):
        layers = []
        prev_dim = input_dim
        for h in hidden_dims:
            layers.append(nn.Linear(prev_dim, h))
            layers.append(nn.ReLU())
            prev_dim = h
        layers.append(nn.Linear(prev_dim, output_dim))  # 输出层
        return nn.Sequential(*layers)
    
    def forward(self, categorical_inputs, numeric_inputs=None):
        embedded = [emb(cat_input) for emb, cat_input in zip(self.embeddings, categorical_inputs)]
        x = torch.cat(embedded + ([numeric_inputs] if numeric_inputs is not None else []), dim=1)
        
        pctr = self.sigmoid(self.ctr_layers(x))
        pctcvr = self.sigmoid(self.ctcvr_layers(x))
        pcvr = pctcvr / (pctr + 1e-8)
        
        return pctr, pctcvr, pcvr


# ========== 3. 构造示例数据 ==========
num_samples = 2000
city_cardinality = 100    # 城市数量
vip_type_cardinality = 10 # 会员类型数量
brand_cardinality = 50    # 品牌数量

uids = torch.arange(num_samples)
ages = torch.randint(18, 60, (num_samples,))
cities = torch.randint(0, city_cardinality, (num_samples,))
used_quota = torch.randint(0, 1000, (num_samples,))
vip_types = torch.randint(0, vip_type_cardinality, (num_samples,))
brands = torch.randint(0, brand_cardinality, (num_samples,))
click_labels = torch.randint(0, 2, (num_samples,)).float()
conversion_labels = (click_labels * torch.randint(0, 2, (num_samples,))).float()

dataset = MyDataset(uids, ages, cities, used_quota, vip_types, brands, click_labels, conversion_labels)
train_loader = DataLoader(dataset, batch_size=32, shuffle=True)


# ========== 4. 模型、优化器 ==========
model = ESMM([city_cardinality, vip_type_cardinality, brand_cardinality],
             num_numeric=2,  # age + used_quota
             ctr_hidden_dims=[64,32], ctcvr_hidden_dims=[64,32])

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

optimizer = optim.Adam(model.parameters(), lr=0.001)
bce_loss = nn.BCELoss()


# ========== 5. 训练循环 ==========
for epoch in range(3):
    model.train()
    total_ctr_loss, total_ctcvr_loss = 0, 0
    for batch in train_loader:
        cities, vip_types, brands, numeric_feats, ctr_label, cvr_label = batch
        
        cities = cities.to(device)
        vip_types = vip_types.to(device)
        brands = brands.to(device)
        numeric_feats = numeric_feats.to(device)
        ctr_label = ctr_label.to(device).unsqueeze(1)
        cvr_label = cvr_label.to(device).unsqueeze(1)
        
        optimizer.zero_grad()
        pctr, pctcvr, pcvr = model([cities, vip_types, brands], numeric_feats)  # 调用forward前向传播
        
        # ESMM 的两个损失：点击预测 + 点击后转化预测
        loss_ctr = bce_loss(pctr, ctr_label)
        loss_ctcvr = bce_loss(pctcvr, cvr_label)
        loss = loss_ctr + loss_ctcvr
        
        # 反向传播
        loss.backward()
        optimizer.step()
        
        total_ctr_loss += loss_ctr.item() * ctr_label.size(0)
        total_ctcvr_loss += loss_ctcvr.item() * cvr_label.size(0)
    
    print(f"Epoch {epoch+1}, CTR Loss: {total_ctr_loss/len(dataset):.4f}, CTCVR Loss: {total_ctcvr_loss/len(dataset):.4f}")
