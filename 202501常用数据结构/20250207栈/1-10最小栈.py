# 10.最小栈
from math import inf


# class MinStack():
# 	def __init__(self):
# 		self.ori_lis = []
# 		# self.min_num = inf

# 	def push(self, val):
# 		self.ori_lis.append(val)
# 		# self.min_num = min(self.min_num, val)

# 	def pop(self):
# 		self.ori_lis.pop()

# 	def top(self):
# 		return self.ori_lis[-1]

# 	def getMin(self):
# 		return min(self.ori_lis)
	
## 灵神思路：O(1)
class MinStack:
	def __init__(self):
		self.st = [(0, inf)]  # 栈底哨兵

	def push(self, val):
		self.st.append((val, min(self.st[-1][1], val)))

	def pop(self):
		self.st.pop()

	def top(self):
		return self.st[-1][0]

	def getMin(self):
		return self.st[-1][1]
	
if __name__ == '__main__':
	stack = MinStack()
	stack.push(-2)
	# print(stack.top())
	# print(stack.getMin()) # Output: -1

	stack.push(0)
	stack.push(-3)
	print(stack.getMin()) # Output: -3
	stack.pop()
	print(stack.top()) # Output: 0
	print(stack.getMin()) # Output: -2