# class Solution:
# 	def numberOfRightTriangles(self, grid):
# 		ans = 0
# 		n, m = len(grid), len(grid[0])
# 		for i, lis in enumerate(grid):
# 			suf_lis = [0] * m
# 			suf_lis[-1] = lis[-1]
# 			for j in range(m - 2, -1, -1):
# 				suf_lis[j] = max(suf_lis[j + 1], lis[j])
# 			pre_mx = 0
# 			for key in lis:
# 				if pre_mx == 1 and key and suf_lis[]
## 灵神题解
class Solution:
	def numberOfRightTriangles(self, grid):
		ans = 0
		col_sum = [sum(col) - 1 for col in zip(*grid)]
		for row in grid:
			row_sum = sum(row) - 1
			ans += row_sum * sum(cs for x, cs in zip(row, col_sum) if x)
		return ans
	
if __name__ == '__main__':
	grid = [[0,1,0],[0,1,1],[0,1,0]]
	print(Solution().numberOfRightTriangles(grid)) # Output: 2