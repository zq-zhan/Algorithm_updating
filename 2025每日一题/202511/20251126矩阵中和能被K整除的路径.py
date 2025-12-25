from functools import cache

class Solution:
	def numberOfPaths(self, grid, k):
		MOD = 10 ** 9 + 7
		m, n = len(grid), len(grid[0])
		@cache
		def dfs(i, j, s):
			if i == m - 1 and j == n - 1:
				return int(s % k == 0)
			if i < m - 1 and j < n - 1:
				return dfs(i + 1, j, (s + grid[i + 1][j]) % k) + dfs(i, j + 1, (s + grid[i][j + 1]) % k)
			elif i < m - 1:
				return dfs(i + 1, j, (s + grid[i + 1][j]) % k)
			else:
				return dfs(i, j + 1, (s + grid[i][j + 1]) % k)

		ans = dfs(0, 0, grid[0][0]) % MOD
		dfs.cache_clear()
		return ans

if __name__ == '__main__':
	grid = [[50]]
	print(Solution().numberOfPaths(grid, 25))