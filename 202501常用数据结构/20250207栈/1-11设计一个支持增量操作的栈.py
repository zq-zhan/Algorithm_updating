# 11.设计一个支持增量操作的栈
# class CustomStack:
# 	def __init__(self, maxSize):
# 		self.maxSize = maxSize
# 		self.st = []

# 	def push(self, x):
# 		if len(self.st) < self.maxSize:
# 			self.st.append(x)

# 	def pop(self):
# 		if self.st:
# 			return self.st.pop()
# 		else:
# 			return -1

# 	def inc(self, k, val):
# 		# i = 0
# 		# while i < k and i < len(self.st):
# 		# 	self.st[i] += val
# 		# 	i += 1
# 		for i in range(0, min(k, len(self.st))):
# 			self.st[i] += val
			
# class CustomStack:
#     def __init__(self, maxSize):
#         self.stack = [0] * maxSize
#         self.nums = [0] * maxSize
#         self.size = maxSize - 1
#         self.p = -1

#     def push(self, x):
#         if self.p != self.size:
#             self.p += 1
#             self.stack[self.p] = x

#     def pop(self):
#         if self.p == -1:
#             return -1
#         x, val = self.stack[self.p], self.nums[self.p]
#         self.nums[self.p] = 0
#         self.p -= 1
#         if self.p != -1:
#             self.nums[self.p] += val
#         return x + val

#     def increment(self, k, val):
#         if self.p >= 0:
#             k = min(self.p, k - 1)
#             self.nums[k] += val

# class CustomStack:
# 	def __init__(self, maxSize):
# 		self.stack = []
# 		self.length = 0
# 		self.maxSize = maxSize

# 	def push(self, x):
# 		if self.length < self.maxSize:
# 			self.length += 1
# 			self.stack.append([x, 0])

# 	def pop(self):
# 		if self.length == 0:
# 			return -1
# 		else:
# 			self.length -= 1
# 			num, add = self.stack.pop()
# 			if self.length > 0:
# 				self.stack[-1][1] += add
# 			return num + add

# 	def increment(self, k, val):
# 		if self.length > 0:
# 			if self.length < k:
# 				k = self.length
# 			self.stack[k - 1][1] += val

class CustomStack:
	def __init__(self, maxSize):
		self.maxSize = maxSize
		self.st = []

	def push(self, x):
		if len(self.st) < self.maxSize:
			self.st.append([x, 0])

	def pop(self):
		if self.st:
			x, val = self.st.pop()
			if self.st:
				self.st[-1][1] += val
			return x + val
		else:
			return -1

	def increment(self, k, val):
		min_range = min(k, len(self.st))
		if self.st:
			self.st[min_range - 1][1] += val



if __name__ == '__main__':
	stack = CustomStack(3)
	# stack.push(1)
	# stack.push(2)
	# print(stack.pop())
	# stack.push(2)
	# stack.push(3)
	# stack.push(4)
	# stack.increment(5, 100)
	# stack.increment(2, 100)
	# print(stack.pop())
	# print(stack.pop())
	# print(stack.pop())
	# print(stack.pop())
	stack.push(34)
	print(stack.pop())
	stack.increment(1, 100)