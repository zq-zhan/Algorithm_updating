from functools import cache
from math import inf

class Solution1:
	def minFallingPathSum(self, matrix):
		n = len(matrix)
		@cache
		def dfs(i, j):
			if i < 0 or j >= n or j < 0:
				return inf
			elif i == 0 and j < n:
				return matrix[i][j]
			return min(dfs(i - 1, j - 1), dfs(i - 1, j), dfs(i - 1, j + 1)) + matrix[i][j]
		return min(dfs(n - 1, x) for x in range(n))
	
## 递推
class Solution2:
	def minFallingPathSum(self, matrix):
		n = len(matrix)
		f = [[0] * n for _ in range(n)]
		f[0] = matrix[0]
		for i in range(1, n):
			for j in range(n):
				if j == 0:
					f[i][j] = min(f[i - 1][j], f[i - 1][j + 1]) + matrix[i][j]
				elif j == n - 1:
					f[i][j] = min(f[i - 1][j - 1], f[i - 1][j]) + matrix[i][j]
				else:
					f[i][j] = min(f[i - 1][j - 1], f[i - 1][j], f[i - 1][j + 1]) + matrix[i][j]
		return min(f[-1])
	
if __name__ == '__main__':
	matrix = [[2,1,3],[6,5,4],[7,8,9]]
	print(Solution2().minFallingPathSum(matrix)) # Output: 13