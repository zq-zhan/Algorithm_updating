from functools import cache

class Solution1:
	def uniquePaths(self, m, n):
		@cache
		def dfs(i, j):
			if i < 0 or j < 0:
				return 0
			elif i == 0 and j == 0:
				return 1
			return dfs(i - 1, j) + dfs(i, j - 1)
		return dfs(m - 1, n - 1)
	
## 递推写法
class Solution2:
	def uniquePaths(self, m, n):
		f = [[0] * (n + 1) for _ in range(m + 1)]
		for i in range(m):
			for j in range(n):
				if i == 0 and j == 0:
					f[1][1] = 1
				else:
					f[i + 1][j + 1] = f[i][j + 1] + f[i + 1][j]
		return f[m][n]

	
if __name__ == '__main__':
	print(Solution2().uniquePaths(3, 7)) # Output: 3