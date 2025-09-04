class Solution:
	def sortMatrix(self, grid):
		m, n = len(grid), len(grid[0])
		for k in range(1, m + n):
			min_j = max(n - k, 0)
			max_j = min(m + n - 1 - k, n - 1)
			a = [grid[k + j - n][j] for j in range(min_j, max_j + 1)]
			a.sort(reverse = k >= n)
			for j, val in zip(range(min_j, max_j + 1), a):
				grid[k + j - n][j] = val
		return grid
	
if __name__ == '__main__':
	grid = [[1,7,3],[9,8,2],[4,5,6]]
	print(Solution().sortMatrix(grid))