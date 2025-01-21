# 3.直角三角形
class Solution1:
	def numberOfRightTriangles(self, grid):
		n = len(s)
		rowSum_lis = []
		colSum_lis = [0] * n
		for i in range(n):
			rowSum_lis.append(sum(grid[i]))
			colSum_lis += list(grid[i][j] for j in range(n))
## 灵神题解
class Solution1:
	def numberOfRightTriangles(self, grid):
		col_sum = [sum(col) - 1 for col in zip(*grid)]  # zip(*grid) 转置矩阵，zip(*grid)[i] 第i列
		ans = 0
		for row in grid:
			row_sum = sum(row) - 1
			ans += row_sum * sum(cs for x, cs in zip(row, col_sum) if x)  # 所以需要和row合并到一起，判断此时的列和对应列上有没有1的元素，否则也是无效的
		return ans


class Solution2:  # 错解：需要保证1在同一行和列
	def numberOfRightTriangles(self, grid):
		col_sum = [sum(col) - 1 for col in zip(*grid)]  # zip(*grid) 转置矩阵，zip(*grid)[i] 第i列
		ans = 0
		for row in grid:
			row_sum = sum(row) - 1
			if row_sum > 0:
				for col in col_sum:
					if col >= 0:
						ans += row_sum * col
				# ans += sum(row_sum * col for col in col_sum if clo >= 0)
		return ans


	    
if __name__ == '__main__':
	grid = [[1,0,0,0],[0,1,0,1],[1,0,0,0]]
	cls = Solution1()
	print(cls.numberOfRightTriangles(grid))