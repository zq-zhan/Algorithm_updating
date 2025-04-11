from functools import cache

# 1.获得分数的方法数
class Solution1:
	def waysToReachTarget(self, target, types):
		@cache
		def dfs(i, c, type):
			if i < 0:
				return 1 if c == 0 else 0
			if type[1] > c or type[0] == 0:
				return dfs(i - 1, c, types[i - 1])
			temp = type.copy()
			temp[0] -= 1
			return dfs(i, c - types[1], temp) + dfs(i - 1, c, types[i - 1])
		return dfs(len(types) - 1, target, types[-1])
## 灵神题解
class Solution1:
	def waysToReachTarget(self, target, types):
		mod = 10 ** 9 + 7
		@cache
		def dfs(i, c):
			if i < 0:
				return 1 if c == 0 else 0
			res = dfs(i - 1, c)
			for _ in range(types[i][0]):
				c -= types[i][1]
				if c < 0:
					break
				res = (res + dfs(i - 1, c)) % mod
			return res
		return dfs(len(types) - 1, target)
class Solution3:
	def waysToReachTarget(self, target, types):
		mod = 10 ** 9 + 7
		@cache
		def dfs(i, c):
			if i < 0:
				return 1 if c == 0 else 0
			count, marks = types[i]
			res = 0
			for k in range(min(count, c // marks) + 1):
				res += dfs(i - 1, c - marks * k)
			return res % mod
		return dfs(len(types) - 1, target)
	
if __name__ == '__main__':
	target = 6
	types = [[6,1],[3,2],[2,3]]
	print(Solution3().waysToReachTarget(target, types))