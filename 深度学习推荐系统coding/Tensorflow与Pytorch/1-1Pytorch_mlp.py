import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np

class MLP(nn.Module):
    def __init__(self, input_size = 128, hidden_size = 32, output_size = 2):
        super().__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)
    
    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

model = MLP()
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr = 0.001)

x_train = torch.from_numpy(np.random.rand(100, 128).astype(np.float32)) # [100, 128]
y_train = torch.from_numpy(np.random.randint(2, size = (100,)).astype(np.int64)) # [100, 2]

num_epochs = 10
batch_size = 10
num_batches = len(x_train) // batch_size

for epoch in range(num_epochs):
    for i in range(num_batches):
        batch_x = x_train[i*batch_size:(i + 1)*batch_size]
        batch_y = y_train[i*batch_size:(i + 1)*batch_size]
        outputs = model(batch_x)
        loss = criterion(outputs, batch_y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
