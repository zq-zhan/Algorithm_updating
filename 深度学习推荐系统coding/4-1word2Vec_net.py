import torch
import torch.nn as nn
import torch.optim as optim
import random

# ============= 1. 数据准备 =======
corpus = "the quick brown fox jumps over the lazy dog".split()
vocab = list(set(corpus))
word2idx = {w: i for i, w in enumerate(vocab)}
idx2word = {i: w for w, i in word2idx.items()}

def getnerate_skipgram_pairs(corpus, window_size = 2):
    pairs = []
    for i, word in enumerate(corpus):
        center = word
        for j in range(-window_size, window_size+1):
            if j == 0 or i+j < 0 or i+j >= len(corpus):
                continue
            context = corpus[i+j]
            pairs.append((word2idx[center], word2idx[context]))
    return pairs

pairs = getnerate_skipgram_pairs(corpus, window_size=2)

# ============== 2. 定义模型 ============
class SkipGramModel(nn.Module):
    def __init__(self, vocab_size, embedding_dim):
        super().__init__()
        self.in_embedding = nn.Embedding(vocab_size, embedding_dim)  # 输入词嵌入层
        self.out_embedding = nn.Embedding(vocab_size, embedding_dim)  # 输出词嵌入层

    def forward(self, center, pos_context, neg_context):
        center_embed = self.in_embedding(center)
        pos_embedding = self.out_embedding(pos_context)
        neg_embedding = self.out_embedding(neg_context)

        pos_score = torch.sum(center_embed * pos_embedding, dim=1)
        pos_loss = -torch.log(torch.sogmoid(pos_score))

        neg_score = torch.bmm(neg_embedding, center_embed.unsqueeze(2)).squeeze()  # batch_size x neg_size,对batch中每个样本做一次矩阵乘法
        neg_loss = -torch.sum(torch.log(torch.sigmoid(-neg_score)), dim = 1)

        return (pos_loss + neg_loss).mean()
    
# ========== 3. 训练准备 =========
embedding_dim = 50
K = 5  # 负采样的个数
model = SkipGramModel(len(vocab), embedding_dim)
optimizer = optim.Adam(model.parameters(), lr = 0.01)

# ============= 4. 训练循环 =========
def get_negative_samples(batch_size, vocab_size, K, true_idx):
    negs = []
    for _ in range(batch_size):
        neg = []
        while len(neg) < K:
            neg = []
            r = random.randint(0, vocab_size-1)
            if r != true_idx:
                neg.append(r)
            negs.append(neg)
    return negs

for epoch in range(200):
    total_loss = 0
    for center, context in pairs:
        center = torch.tensor([center])
        context = torch.tensor([context])
        neg_context = get_negative_samples(1, len(vocab), K, context.item())

        loss = model(center, context, neg_context)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    if epoch % 10 == 0:
        print(f"epoch: {epoch}, loss: {total_loss}")

# ========= 5. 查看词向量 =======
word_vec = model.in_embedding.weight.data
for w in ["the", "dog", "fox", "quick"]:
    print(w, word_vec[word2idx[w]].numpy()[:5])