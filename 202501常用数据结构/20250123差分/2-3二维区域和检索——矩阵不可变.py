# 3.二维区域和检索——矩阵不可变
class NumMatrix:
	def __init__(self,matrix):
		m = len(matrix)
		n = len(matrix[0])

		# 1.计算二维前缀和
		# ans = 0
		s = [[0] * (n + 1) for _ in range(m + 1)]
		for i, row in enumerate(matrix):
			for j, v in enumerate(row):
				s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + v

		self.s = s
	def sumRegion(self, row1, col1, row2, col2):
		# new_arr = self.matrix
		# m = len(new_arr)
		# n = len(new_arr[0])

		# # 1.计算二维前缀和
		# # ans = 0
		# s = [[0] * (n + 1) for _ in range(m + 1)]
		# for i, row in enumerate(new_arr):
		# 	for j, v in enumerate(row):
		# 		s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + v
		s = self.s
		return s[row2 + 1][col2 + 1] - s[row2 + 1][col1] - s[row1][col2 + 1] + s[row1][col1]


if __name__ == '__main__':
	
	matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
	cls = NumMatrix(matrix)
	print(cls.sumRegion(2, 1, 4, 3)) # 8
	print(cls.sumRegion(1, 1, 2, 2)) # 11
	print(cls.sumRegion(1, 2, 2, 4)) # 12