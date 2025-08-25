class Solution:
	def minimumArea(self, grid):
		n, m = len(grid), len(grid[0])
		left = m - 1
		right = 0
		high = 0
		low = n - 1
		for i in range(n):
			for j in range(m):
				if grid[i][j]:
					left = min(left, j)
					right = max(right, j)
					high = max(high, i)
					low = min(low, i)
		return (right - left + 1) * (high - low + 1)
	
if __name__ == '__main__':
	grid = [[0,1,0],[1,0,1]]
	print(Solution().minimumArea(grid))