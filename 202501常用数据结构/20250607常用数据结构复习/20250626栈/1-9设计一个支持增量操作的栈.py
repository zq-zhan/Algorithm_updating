# class CustomStack:

# 	def __init__(self, maxSize):
# 		self.stk = []
# 		self.maxSize = maxSize

# 	def push(self, x):
# 		if len(self.stk) < self.maxSize:
# 			self.stk.append(x)


# 	def pop(self):
# 		return self.stk.pop() if self.stk else -1

# 	def increment(self, k, val):
# 		for i in range(min(k, len(self.stk))):
# 			self.stk[i] += val
			

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
    obj = CustomStack(3)
    obj.push(1)
    obj.push(2)
    print(obj.pop())
    obj.push(2)
    obj.push(3)
    obj.push(4)
    obj.increment(5, 100)
    obj.increment(2, 100)
    print(obj.pop())
    print(obj.pop())
    print(obj.pop())
    print(obj.pop())
	

        