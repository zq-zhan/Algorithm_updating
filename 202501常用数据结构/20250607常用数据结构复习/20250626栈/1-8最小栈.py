from collections import defaultdict

class MinStack:

	def __init__(self):
		self.stk = []
		self.stk_dic = defaultdict(int)

	def push(self, val):
		self.stk.append(val)
		self.stk_dic[val] += 1
	

	def pop(self):
		pop_val = self.stk.pop()
		if self.stk_dic[pop_val] == 1:
			del self.stk_dic[pop_val]
		else:
			self.stk_dic[pop_val] -= 1
	
	def top(self):
		return self.stk[-1]
	
	def getMin(self):
		return min(self.stk_dic.keys())
	
if __name__ == '__main__':
	ms = MinStack()
	ms.push(-2)
	ms.push(0)
	ms.push(-3)
	print(ms.getMin()) # Output: -3
	ms.pop()
	print(ms.top()) # Output: 0
	print(ms.getMin()) # Output: -2