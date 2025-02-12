# 2.子矩阵元素加1
class Solution1:
	def rangeAddQueries(self, n, queries):
		mat = [[0] * n for _ in range(n)]

		# 1.计算二维前缀和
		# s = [[0] * (n + 1) for _ in range(n + 1)]  # 前缀和全是0

		# 2.计算二维差分
		d = [[0] * (n + 2) for _ in range(n + 2)]
		for r1, c1, r2, c2 in queries:
			# for  in querie:
			d[r1 + 1][c1 + 1] += 1
			d[r1 + 1][c2 + 2] -= 1
			d[r2 + 2][c1 + 1] -= 1
			d[r2 + 2][c2 + 2] += 1

		# 3.计算二维前缀和、还原计数矩阵
		for i in range(1, n + 1):
			for j in range(1, n + 1):
				d[i][j] += d[i][j - 1] + d[i - 1][j] - d[i - 1][j - 1]
				mat[i - 1][j - 1] = d[i][j]
		return mat
	
## 灵神题解
class Solution2:
    def rangeAddQueries(self, n, queries):
        # 二维差分
        diff = [[0] * (n + 2) for _ in range(n + 2)]
        for r1, c1, r2, c2 in queries:
            diff[r1 + 1][c1 + 1] += 1
            diff[r1 + 1][c2 + 2] -= 1
            diff[r2 + 2][c1 + 1] -= 1
            diff[r2 + 2][c2 + 2] += 1

        # 计算 diff 的二维前缀和（原地修改）
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                diff[i][j] += diff[i][j - 1] + diff[i - 1][j] - diff[i - 1][j - 1]

        # 保留中间 n*n 的部分，即为答案
        diff = diff[1:-1]
        for i, row in enumerate(diff):
            diff[i] = row[1:-1]
        return diff
    
if __name__ == '__main__':
	cls = Solution1()
	n = 3
	queries = [[1,1,2,2],[0,0,1,1]]
	print(cls.rangeAddQueries(n, queries))