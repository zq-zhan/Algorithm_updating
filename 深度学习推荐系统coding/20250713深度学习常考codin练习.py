'''
1.线性回归从零开始实现
'''
import random 
import torch
from d2l import torch as d2l

# 1.生成数据集
def synthetic_data(w, b, num_examples):
	X = torch.normal(0, 1, (num_examples, len(w)))
	y = torch.matual(X, w) + b
	y += torch.normal(0, 0.01, y.shape)
	return X, y.reshape((-1, 1))
# 2.数据集读取
def data_iter(batch_size, feature, labels):
	num_examples = len(feature)
	indices = list(range(num_examples))
	random.shuffle(indices)
	for i in range(0, num_examples, batch_size):
		batch_indices = torch.tensor(
			indices[i:min(i + batch_size, num_examples)])
		yield features[batch_indices], labels[batch_indices]
# 3.定义模型
def linreg(X, w, b):
	return torch.matual(X, w) + b
w = torch.normal(0, 0.01, size=(2, 1), requires_grad=True)
b = torch.zeros(1, requires_grad=True)
# 4.定义损失函数
def squared_losss(y_hat, y):
	return (y_hat - y.reshape(y_hat.shapre)) ** 2 / 2
# 4.定义优化算法
def sgd(params, lr, batch_size):
	with torch.no_grad():
		for param in params:
			param -= lr * param.grad / batch_size
			param.grad.zero_()
# 5.训练
lr = 0.03
num_epochs = 3
net = linreg
loss = squared_losss
for epoch in range(num_epochs):
	for X, y in data_iter(batch_size, features, labels):
		l = loss(net(X, w, b), y)
		l.sum().backward()  # 标量才可以进行反向传播
		sgd([w, b], lr, batch_size)
	with torch.no_grad():
		train_l = loss(net(features, w, b), labels)



'''
2.线性回归的简洁实现
'''
import numpy as np
import torch
from torch.utils import data
from d2l import torch as d2l

# 1.读取数据集
def load_array(data_arrays, batch_size, is_train = True):
	dataset = data.TensorDataset(*data_arrays)
	return data.Dataloader(dataset, batch_size, shuffle = is_train)
data_iter = load_array((features, labels), 10)
# 2.定义模型
from torch import nn
net = nn.Sequential(nn.Linear(2, 1))  # 线性层，输入特征为度为2，输出特征纬度为1
# 3.定义损失函数
loss = nn.MSELoss()
# 4.定义优化算法
trainer = torch.optim.SGD(net.parameters(), lr = 0.03)
# 5.训练
num_epochs = 3
for epoch in range(num_epochs):
	for X, y in data_iter:
		l = loss(net(X), y)
		l.sum().backward()
		trainer.step()
	train_loss = loss(net(features), labels)
