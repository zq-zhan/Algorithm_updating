class CombinationIterator:

	def __init__(self, characters, combinationLength):
		self.ans = []
		## 方法一：选或不选
		# n = len(characters)
		# path = []
		# def dfs(i):
		# 	if i == n:
		# 		if len(path) == combinationLength:
		# 			self.ans.append(''.join(path))
		# 		return
		# # 	dfs(i + 1)  # 不选
		# # 	path.append(characters[i])
		# # 	dfs(i + 1)  # 选
		# # 	path.pop()
		# # dfs(0)
		# # self.ans.sort()

		# # 优化——要求有序必须先选
		# 	path.append(characters[i])
		# 	dfs(i + 1)  # 选
		# 	path.pop()
		# 	dfs(i + 1)  # 不选
		# dfs(0)
		
		
		## 方法二：枚举选那个
		path = []
		self.queue = []
		def dfs(i):
			if len(path) == combinationLength:
				self.queue.append(''.join(path))
				return 
			for j in range(i, len(characters)):
				path.append(characters[j])
				dfs(j+1)
				path.pop()
		dfs(0)
		self.queue

	def next(self):
		return self.ans.pop(0)

	def hasNext(self):
		return len(self.ans) > 0
	
if __name__ == '__main__':
	characters = "abc"
	combinationLength = 2
	obj = CombinationIterator(characters, combinationLength)
	print(obj.next())
	print(obj.hasNext())
	print(obj.next())
	print(obj.hasNext())
	print(obj.next())
	print(obj.hasNext())