from functools import cache

class Solution1:
	def maxMoves(self, grid):  # 错解
		m, n = len(grid), len(grid[0])
		@cache
		def dfs(i, j, val):
			if 0 <= i < m and val >= grid[i][j]:
				return 0
			else:
				if i < 0 or i > m - 1 or j >= n - 1:
					return 0
				# elif j == n - 1:
				# 	return 1
				new_val = grid[i][j]
				return max(dfs(i - 1, j + 1, new_val), dfs(i, j + 1, new_val), dfs(i + 1, j + 1, new_val)) + 1
		return max(dfs(x, 0, 0) for x in range(n))
	
## 灵神题解——递推
class Solution3:
	def maxMoves(self, grid):
		m, n = len(grid), len(grid[0])
		vis = [-1] * m
		q = range(m)
		for j in range(n - 1):
			tmp = q
			q = []
			for i in tmp:
				for k in (i - 1, i, i + 1):
					if 0 <= k < m and vis[k] != j and grid[k][j + 1] > grid[i][j]:
						vis[k] = j
						q.append(k)
			if not q:
				return j
		return n - 1
	
if __name__ == '__main__':
	# grid = [[3,2,4],[2,1,9],[1,1,7]]
	grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
	print(Solution3().maxMoves(grid))