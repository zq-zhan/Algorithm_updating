from functools import cache

class Solution:
	def maxMoves(self, grid):
		n, m = len(grid), len(grid[0])
		@cache
		def dfs(i, j, x):
			if i < 0 or i >= n or j == m or grid[i][j] <= x:
				return -1
			x = grid[i][j]
			return max(dfs(i - 1, j + 1, x), dfs(i, j + 1, x), dfs(i + 1, j + 1, x)) + 1
		return max(dfs(i, 0, 0) for i in range(n))
	
if __name__ == '__main__':
	grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
	print(Solution().maxMoves(grid))