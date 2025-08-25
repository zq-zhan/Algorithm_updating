from functools import cache

class Solution:
	def numberOfWays(self, n, x):
		MOD = 10 ** 9 + 7
		@cache
		def dfs(i, path):
			if i < 0 or path > n:
				return 0
			if path == n:
				return 1
			return (dfs(i - 1, path + i ** x) + dfs(i - 1, path)) % MOD
		return dfs(n, 0)


if __name__ == '__main__':
	n = 10
	x = 2
	print(Solution().numberOfWays(n, x))