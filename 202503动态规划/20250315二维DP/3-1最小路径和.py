# 1.最小路径和
from functools import cache
from math import inf

class Solution1:
	def minPathSum(self, grid):
		m, n = len(grid), len(grid[0])
		@cache
		def dfs(i, j):
			if i == 0 and j == 0:
				return grid[0][0]
			elif i < 0 or j < 0:
				return inf
			return min(dfs(i - 1, j), dfs(i, j - 1)) + grid[i][j]
		return dfs(m - 1, n - 1)
	

## 递推写法
class Solution2:
	def minPathSum(self, grid):
		m, n = len(grid), len(grid[0])
		f = [[inf] * (n + 1) for _ in range(m + 1)]
		for i, row in enumerate(grid):
			for j, x in enumerate(row):
				if i == j == 0:
					f[1][1] = x
				else:
					f[i + 1][j + 1] = min(f[i + 1][j], f[i][j + 1]) + x
		return f[m][n]
	
class Solution3:
	def minPathSum(self, grid):
		m, n = len(grid), len(grid[0])
		@cache
		def dfs(i, j):
			if i < 0 or j < 0:
				return inf
			elif i == 0 and j == 0:
				return grid[0][0]
			return min(dfs(i - 1, j), dfs(i, j - 1)) + grid[i][j]
		return dfs(m - 1, n - 1)
## 递推写法
class Solution4:
	def minPathSum(self, grid):
		m, n = len(grid), len(grid[0])
		f = [[inf] * (n + 1) for _ in range(m + 1)]
		for i, row in enumerate(grid):
			for j, x in enumerate(row):
				if i == j == 0:
					f[1][1] = x
				else:
					f[i + 1][j + 1] = min(f[i + 1][j], f[i][j + 1]) + x
		return f[-1][-1]

if __name__ == '__main__':
	grid = [[1,3,1],[1,5,1],[4,2,1]]
	s = Solution4()
	print(s.minPathSum(grid))