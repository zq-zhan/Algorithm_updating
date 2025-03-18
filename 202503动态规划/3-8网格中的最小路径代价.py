# 8.网格中的最小路径代价
from functools import cache
from math import inf

class Solution1:
	def minPathCost(self, grid, moveCost):
		m, n = len(grid), len(grid[0])
		@cache
		def dfs(i, j):
			if i == m - 1:
				return grid[i][j]
			val = grid[i][j]
			return min(dfs(i + 1, x) + grid[i][j] + moveCost[val][x] for x in range(n))

		return min(dfs(0, c) for c in range(n))
	
## 递推写法
class Solution2:
	def minPathCost(self, grid, moveCost):
		m, n = len(grid), len(grid[0])
		f = [[inf] * n for _ in range(m)]
		f[-1] = grid[-1]
		for i in range(m - 2, -1, -1):
			for j, c in enumerate(grid[i]):
				for k, cost in enumerate(moveCost[c]):
					f[i][j] = min(f[i][j], f[i + 1][k] + cost)
				f[i][j] += c
		return min(f[0])
## 原地修改（空间复杂度O(1)）
class Solution3:
	def minPathCost(self, grid, moveCost):
		m, n = len(grid), len(grid[0])
		for i in range(m - 2, -1, -1):
			for j in range(n):
				grid[i][j] += min(g + c for g, c in zip(grid[i + 1], moveCost[grid[i][j]]))
		return min(grid[0])

if __name__ == '__main__':
	grid = [[5,3],[4,0],[2,1]]
	moveCost = [[9,8],[1,5],[10,12],[18,6],[2,4],[14,3]]
	print(Solution3().minPathCost(grid, moveCost))