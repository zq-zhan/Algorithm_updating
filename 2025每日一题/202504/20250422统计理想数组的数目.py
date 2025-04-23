from functools import cache

# 20250422统计理想数组的数目
class Solution1:
	def idealArrays(self, n, maxValue):
		@cache
		def dfs(i, c):
			if i < 0:
				return 1
			for x in range(1, maxValue + 1):
				if c % x == 0:
					return dfs(i - 1, x)
				else:
					return 0
		return sum(dfs(n - 1, x) for x in range(1, maxValue + 1))
	
if __name__ == '__main__':
	n = 2
	maxValue = 5
	print(Solution1().idealArrays(n, maxValue))