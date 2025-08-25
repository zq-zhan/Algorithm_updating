# class Solution:  # 错解
# 	def numSubmat(self, mat):
# 		ans = 0
# 		m, n = len(mat), len(mat[0])
# 		for i in range(m):
# 			for j in range(n):
# 				if mat[i][j] == 1:
# 					ans += 1
# 					for k in range(j + 1, n):
# 						if mat[i][k] == 1:
# 							ans += 1
# 						else:
# 							break
# 					for k in range(i + 1, m):
# 						if mat[k][j] == 1:
# 							ans += 1
# 						else:
# 							break
# 					cnt = 1
# 					while i + cnt < m and j + cnt < n:
# 						temp_s = 0
# 						for r in range(i, i + cnt + 1):
# 							temp_s += sum(mat[r][j:j + cnt + 1])
# 						if temp_s == (cnt + 1) ** 2:
# 							ans += 1
# 							cnt += 1
# 						else:
# 							break
# 		return ans

## 灵神题解
class Solution:
    def numSubmat(self, mat):
        m, n = len(mat), len(mat[0])
        ans = 0
        for top in range(m):  # 枚举上边界
            a = [0] * n
            for bottom in range(top, m):  # 枚举下边界
                h = bottom - top + 1  # 高
                # 2348. 全 h 子数组的数目
                last = -1
                for j in range(n):
                    a[j] += mat[bottom][j]  # 把 bottom 这一行的值加到 a 中
                    if a[j] != h:
                        last = j  # 记录上一个非 h 元素的位置
                    else:
                        ans += j - last
        return ans

	
if __name__ == '__main__':
	mat = [[0,1,1,0], [0,1,1,1], [1,1,1,0]]
	print(Solution().numSubmat(mat))