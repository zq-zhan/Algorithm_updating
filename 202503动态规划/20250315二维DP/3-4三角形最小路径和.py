from functools import cache

# 4.三角形最小路径和
class Solution1:
	def minimumTotal(self, triangle):
		m = len(triangle)
		@cache
		def dfs(i, j):
			if i >= m:
				return 0
			return min(dfs(i + 1, j), dfs(i + 1, j + 1)) + triangle[i][j]
		return dfs(0, 0)
## 递推
class Solution2:
    def minimumTotal(self, triangle):
        n = len(triangle)
        f = [[0] * (i + 1) for i in range(n)]
        f[-1] = triangle[-1]
        for i in range(n - 2, -1, -1):
            for j, x in enumerate(triangle[i]):
                f[i][j] = min(f[i + 1][j], f[i + 1][j + 1]) + x
        return f[0][0]
	
# 4.三角形最小路径和
class Solution3:
	def minimumTotal(self, triangle):
		n = len(triangle)
		@cache
		def dfs(i, j):
			if i == n:
				return 0
			return min(dfs(i + 1, j), dfs(i + 1, j + 1)) + triangle[i][j]
		return dfs(0,0)

## 递推写法2
class Solution4:
	def minimumTotal(self, triangle):
		n = len(triangle)
		f = []
		for i in range(n):
			f.append([0] * (i + 1))
		for i in range(n - 1, -1, -1):
			for j in range(i + 1):
				if i == n - 1:
					f[i][j] = triangle[i][j]
				else:
					f[i][j] = min(f[i + 1][j], f[i + 1][j + 1]) + triangle[i][j]
		return f[0][0]

if __name__ == '__main__':
	triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
	s = Solution4()
	print(s.minimumTotal(triangle))