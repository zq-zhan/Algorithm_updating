from functools import cache

class Solution:
	def soupServings(self, n):
		@cache
		def dfs(i, j):
			if i <= 0 and j > 0:
				return 1
			elif i <= 0 and j <= 0:
				return 0.5
			elif j <= 0:
				return 0
			return 0.25 * (dfs(i - 100, j) + dfs(i - 75, j - 25) + dfs(i - 50, j - 50) + dfs(i - 25, j - 75))
		return dfs(n, n)


if __name__ == '__main__':
	n = 100
	print(Solution().soupServings(n))