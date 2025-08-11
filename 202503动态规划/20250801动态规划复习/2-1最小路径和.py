from functools import cache
from math import inf

class Solution:
	def minPathSum(self, grid):
		n, m = len(grid), len(grid[0])
		@cache
		def dfs(i, j):
			if i < 0 or j < 0:
				return inf
			elif i == 0 and j == 0:
				return grid[0][0]
			return min(dfs(i - 1, j), dfs(i, j - 1)) + grid[i][j]
		return dfs(n - 1, m - 1)
	
if __name__ == '__main__':
	grid = [[1,3,1],[1,5,1],[4,2,1]]
	s = Solution()
	print(s.minPathSum(grid))