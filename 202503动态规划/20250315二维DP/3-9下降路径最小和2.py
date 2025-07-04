# 9.下降路径最小和2
from functools import cache

class Solution1:
	def minFallingPathSum(self, grid):
		m, n = len(grid), len(grid[0])
		@cache
		def dfs(i, j):
			if i == 0:
				return grid[i][j]
			return min(dfs(i - 1, x) for x in range(n) if x != j) + grid[i][j]
		return min(dfs(m - 1, c) for c in range(n))
	
class Solution2:
	def minFallingPathSum(self, grid):
		n, m = len(grid), len(grid[0])
		@cache
		def dfs(i, j):
			if i == 0:
				return grid[i][j]
			return min(dfs(i - 1, x) for x in range(m) if x != j) + grid[i][j]
		return min(dfs(n - 1, y) for y in range(m))

if __name__ == '__main__':
	# grid = [[1,2,3],[4,5,6],[7,8,9]]
	grid = [[7]]
	print(Solution2().minFallingPathSum(grid)) # Output: 13