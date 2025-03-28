from functools import cache
from math import inf

class Solution1:  # 超出内存限制
	def largestNumber(self, cost, target):
		@cache
		def dfs(i, c, ans):
			if i < 0:
				return ans if c == 0 else '0'
			if c >= cost[i]:
				return max_a_b(dfs(i - 1, c, ans), dfs(i, c - cost[i], ans * 10 + i + 1))
			return dfs(i - 1, c, ans)
		def max_a_b(a, b):
			a = str(a)
			b = str(b)
			if len(a) == len(b):
				return max(a, b)
			elif len(a) > len(b):
				return a
			else:
				return b
		ans = dfs(len(cost) - 1, target, 0)
		return ans 

## 一维的递推
class Solution2:
	def largestNumber(self, cost, target):
		# n = len(cost)
		f = [0] + [-inf] * target
		for i in range(len(cost) - 1, -1, -1):
			for c in range(cost[i], target + 1):
				f[c] = max(f[c], f[c - cost[i]] * 10 + i + 1)
		return str(f[-1]) if f[-1] > 0 else '0'
	
## 内存优化
class Solution3:
	def largestNumber(self, cost, target):
		def max_a_b(a, b):
			a = str(a)
			b = str(b)
			if len(a) == len(b):
				return max(a, b)
			elif len(a) > len(b):
				return a
			else:
				return b
				
		cost = [0] + cost
		f = ['0'] * (target + 1)
		f[0] = ''
		for x in range(1, 10):
			for c in range(cost[x], target + 1):
				if f[c - cost[x]] != '0':
					tmp = str(x) + f[c - cost[x]]
					f[c] = max_a_b(f[c], tmp)
		return f[-1]
	
if __name__ == '__main__':
	cost = [4, 3, 2, 5, 6, 7, 2, 5, 5]
	target = 9
	s = Solution3()
	print(s.largestNumber(cost, target))