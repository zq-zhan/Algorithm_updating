from functools import cache

class Solution1:
	def uniquePathsWithObstacles(self, obstacleGrid):
		m, n = len(obstacleGrid), len(obstacleGrid[0])
		@cache
		def dfs(i, j):
			if i < 0 or j < 0 or obstacleGrid[i][j] == 1:
				return 0
			elif i == 0 and j == 0:
				return 1
			return dfs(i - 1, j) + dfs(i, j - 1)
		return dfs(m - 1, n - 1)
	
class Solution2:
	def uniquePathsWithObstacles(self, grid):
		m, n = len(grid), len(grid[0])
		def dfs(i, j):
			if i < 0 or j < 0:
				return 0
			else:
				c = grid[i][j]
				if c == 1:
					return 0
				else:
					if i == 0 and j == 0:
						return 1
					else:
						return dfs(i - 1, j) + dfs(i, j - 1)
		return dfs(m - 1, n - 1)
	
if __name__ == '__main__':
	obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
	print(Solution2().uniquePathsWithObstacles(obstacleGrid)) # Output: 2