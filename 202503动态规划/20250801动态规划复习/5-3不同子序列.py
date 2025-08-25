from functools import cache

class Solution:
	def numDistinct(self, s, t):
		n, m = len(s), len(t)
		@cache
		def dfs(i, j):
			if j < 0:
				return 1
			elif i < 0:
				return 0
			res = 0
			if s[i] == t[j]:
				res += dfs(i - 1, j - 1)
			res += dfs(i - 1, j)
			return res
		return dfs(n - 1, m - 1)
	
if __name__ == '__main__':
	s = "rabbbit"
	t = "rabbit"
	print(Solution().numDistinct(s, t))