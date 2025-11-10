import torch
import torch.nn as nn
import torch.optim as optim
from torch.util.data import DataLoader, TensorDataset

class FNNEmbedding(nn.Module):
    def __init__(self, categorical_cardinalities, embedding_dims=None, num_numerical=0, hidden_dims=[64,32], output_dim=1):
        '''
        categorical_cardinalities: list[int], 每个类别特征的取值个数
        embedding_dims: list[int], 每个类别特征embedding的维度
        num_numerical: int, 数值型特征的维度
        hide_dims: list[int], MLP隐藏层大小
        out_dims: int, 输出维度
        '''
        super(FNNEmbedding, self).__init__()  # 继承父类初始化
        self.num_numerical = num_numerical
        self.num_categories = len(categorical_cardinalities)
        assert self.num_categories == len(embedding_dims), 'categorical_cardinalities and embedding_dims must have the same length'

        if embedding_dims is None:
            embedding_dims = [min(50, (cat+1)//2) for cat in categorical_cardinalities]  # 自动设置embedding维度
        self.embedding_dims = embedding_dims

        # 创建embedding层
        self.embeddings = nn.ModuleList([
            nn.Embedding(cardinality, emb_dim)  # V*d，V为每个类别特征的取值个数，d为embedding维度
            for cardinality, emb_dim in zip(categorical_cardinalities, embedding_dims)
        ])

        # MLP 输入维度=所有embedding维度和(concate特点) + 数值特征维度
        input_dim = sum(embedding_dims) + num_numerical

        # 构建MLP
        self.hidden_layers = nn.ModuleList()
        prev_dum = input_dim
        for h_dim in hidden_dims:
            self.hidden_layers.append(nn.Linear(prev_dum, h_dim))  # 全连接层
            prev_dum = h_dim
        self.output_layer = nn.Linear(prev_dum, output_dim)  # 输出层
        self.activation = nn.ReLU()  # 激活函数

    def forward(self, categorical_inputs, numerical_inputs=None):
        '''
        categorical_inputs: list[Tensor], 类别型特征的输入
        numerical_inputs: Tensor, 数值型特征的输入
        '''
        embedded = [emb(cat_input) for emb, cat_input in zip(self.embeddings, categorical_inputs)]  # 嵌入层，对每个类别特征进行embedding，获取对应的embedding向量
        x = torch.cat(embedded + ([numerical_inputs] if numerical_inputs is not None else []))

        for layer in self.hidden_layers:
            x = self.activation(layer(x))
        x = self.output_layer(x)
        return x    

# 类别型特征：3个
num_categories = [10, 50, 100]  # 每个类别特征的取值数
# 数值特征
num_numeric_features = 5
# 输出类别
num_classes = 2
num_samples = 1000
batch_size = 16

# 生成随机数据
categorical_data = [torch.randint(0, n, (num_samples,)) for n in num_categories]
numeric_data = torch.randn(num_samples, num_numeric_features)
labels = torch.randint(0, num_classes, (num_samples,))

dataset = TensorDataset(*categorical_data, numeric_data, labels)
train_loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# 创建模型
model = FNNEmbedding(num_categories, num_numerical=num_numeric_features, hidden_dims=[64,32], output_dim=num_classes)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")  # 选择设备
model = model.to(device)

# 定义损失函数和优化器
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 训练模型
for epoch in range(10):
    model.train()
    total_loss = 0
    for batch in train_loader:
        *cat_feats, num_feats, labels = batch
        cat_feats = [feat.to(device) for feat in cat_feats]
        num_feats = num_feats.to(device)
        labels = labels.to(device)

        optimizer.zero_grad()  # 梯度清零
        outputs = model(cat_feats, num_feats)
        loss = criterion(outputs, labels)  # 平均损失
        loss.backward()  # 反向传播
        optimizer.step()  # 更新参数
        total_loss += loss.item() * labels.size(0)  # 累计损失
    print(f"Epoch {epoch+1}, Loss: {total_loss/num_samples:.4f}")
