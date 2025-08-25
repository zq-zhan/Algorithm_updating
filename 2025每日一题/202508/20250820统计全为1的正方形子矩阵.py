class Solution:
    def countSquares(self, matrix):
        ans = 0
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:  # 只有以 1 开头的才可能形成正方形
                    cnt = 0
                    while i + cnt < m and j + cnt < n:
                        # 计算子矩阵 (i,j) 到 (i+cnt, j+cnt) 的和
                        total = 0
                        for r in range(i, i + cnt + 1):
                            total += sum(matrix[r][j:j + cnt + 1])
                        # 判断是否全是 1
                        if total == (cnt + 1) * (cnt + 1):
                            ans += 1
                            cnt += 1
                        else:
                            break
        return ans

## 灵神题解——动态规划
# class Solution:
# 	def countSquares(self, matrix):
# 		m, n = len(matrix), len(matrix[0])
# 		f = [[0] * (n + 1) for _ in range(m + 1)]
# 		for i, row in enumerate(matrix):
# 			for j, x in enumerate(row):
# 				if x:
# 					f[i + 1][j + 1] = min(f[i][j], f[i][j + 1], f[i + 1][j]) + 1
# 			return sum(map(sum, f))
		
if __name__ == '__main__':
	matrix = [
		[0,1,1,1],
		[1,1,1,1],
		[0,1,1,1]
	]
	print(Solution().countSquares(matrix)) # Output: 15