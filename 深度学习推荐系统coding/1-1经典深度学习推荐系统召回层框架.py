# 召回层结构：输入层+不同特征域的Embedding层+连接层+多层神经网络+输出层


import torch
import torch.nn as nn
import torch.optim as optim

class RecommendationModel(nn.Module):
    def __init__(self,user_count,item_count,age_bucket_count,gender_count,embedding_dim):
        super(RecommendationModel,self).__init__()  # 继承父类初始化方法

        # 嵌入层
        self.user_embedding = nn.Embedding(user_count, embedding_dim)  # 用户特征维度, 嵌入维度
        self.item_embedding = nn.Embedding(item_count, embedding_dim)
        self.age_embedding = nn.Embedding(age_bucket_count, embedding_dim)
        self.gender_embedding = nn.Embedding(gender_count, embedding_dim)

        # MLP层
        self.fc1 = nn.Linear(embedding_dim*4, 64)
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, 16)
        self.fc_output = nn.Linear(16, 1)
    
    def forward(self, user_input, item_input, age_input, gender_input):
        # 获取嵌入向量
        user_vec = self.user_embedding(user_input)  # user_input:(batch_size, 1), user_vec:(batch_size, embedding_dim),通过传入的用户索引，获取用户对应的embedding向量
        item_vec = self.item_embedding(item_input)
        age_vec = self.age_embedding(age_input)
        gender_vec = self.gender_embedding(gender_input)

        # 拼接特征
        concat_vec = torch.cat((user_vec, item_vec, age_vec, gender_vec),dim=1)

        # MLP前向传播
        x = torch.relu(self.fc1(concat_vec))
        x = torch.relu(self.fc2(x))
        x = torch.relu(self.fc3(x))
        output = torch.sigmoid(self.fc_output(x))

        return output
    
# 参数设置
user_count = 1000  # 用户属性向量维度
item_count = 500
age_bucket_count = 10
gender_count = 2
embedding_dim = 8

# 模型实例化
model = RecommendationModel(user_count, item_count, age_bucket_count, gender_count, embedding_dim)

# 定义损失函数和优化器
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 模拟一些训练数据
X_users = torch.randint(0,user_count,(10000,1))  # 10000个样本，0-user_count维度的用户属性向量
X_items = torch.randint(0,item_count,(10000,1))
X_ages = torch.randint(0,age_bucket_count,(10000,1))
X_genders = torch.randint(0,gender_count,(10000,1))

# Y(真实值)
y = torch.randint(0,2,(10000,1)).float()

# 模型训练
num_epochs = 10
batch_size = 32

model.train()  # 训练模式
for epoch in range(num_epochs):
    for i in range(0,X_users.size(0),batch_size):
        # 获取当前batch的数据
        user_batch = X_users[i:i+batch_size]
        item_batch = X_items[i:i+batch_size]
        age_batch = X_ages[i:i+batch_size]
        gender_batch = X_genders[i:i+batch_size]
        labels = y[i:i+batch_size]

        # 梯度清零
        optimizer.zero_grad()

        # 前向传播
        outputs = model(user_batch, item_batch, age_batch, gender_batch)

        # 计算损失
        loss = criterion(outputs, labels)

        # 反向传播及优化
        loss.backward()
        optimizer.step()
        
    print(f'Epoch [{epoch+1}/{num_epochs}],Loss:{loss.item():.4f}')
