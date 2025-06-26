from functools import cache

class Solution1:
	def countPathsWithXorValue(self, grid, k):
		mod = (10 ** 9 + 7)
		@cache
		def dfs(i, j, ans):
			if i == 0 and j == 0:
				if ans ^ grid[i][j] == k:
					return 1
				else:
					return 0
			elif i < 0 or j < 0:
				return 0
			return (dfs(i - 1, j, ans ^ grid[i][j]) + dfs(i , j - 1, ans ^ grid[i][j])) % mod
		m, n = len(grid), len(grid[0])
		return dfs(m - 1, n - 1, 0) % mod
	
## 灵神递归：定义dfs(i, j, x)为递归到i，j时路径异或值为x的方案数
class Solution2:
	def countPathsWithXorValue(self, grid, k):
		mod = (10 ** 9 + 7)
		@cache
		def dfs(i, j, x):
			if i == j == 0:
				return 1 if x == grid[0][0] else 0
			elif i < 0 or j < 0:
				return 0
			val = grid[i][j]
			return (dfs(i - 1, j, x ^ val) + dfs(i, j - 1, x ^ val)) % mod
		m, n = len(grid), len(grid[0])
		return dfs(m - 1, n - 1, k) % mod

## 递推
class Solution3:
    def countPathsWithXorValue(self, grid, k):
        MOD = 1_000_000_007
        u = 1 << max(map(max, grid)).bit_length()
        # if k >= u:
        #     return 0

        m, n = len(grid), len(grid[0])
        f = [[[0] * u for _ in range(n + 1)] for _ in range(m + 1)]
        f[0][1][0] = 1
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                for x in range(u):
                    f[i + 1][j + 1][x] = (f[i + 1][j][x ^ val] + f[i][j + 1][x ^ val]) % MOD
        return f[m][n][k]
	

class Solution4:
	def countPathsWithXorValue(self, grid, k):
		n, m = len(grid), len(grid[0])
		@cache
		def dfs(i, j, c):
			if i < 0 or j < 0:
				return 0
			elif i == 0 and j == 0:
				return 1 if c == grid[0][0] ^ k else 0
			c ^= grid[i][j]
			return dfs(i - 1, j, c) + dfs(i, j - 1, c)
		return dfs(n - 1, m - 1, 0)
		
if __name__ == '__main__':
	grid = [[2, 1, 5], [7, 10, 0], [12, 6, 4]]
	k = 11
	print(Solution4().countPathsWithXorValue(grid, k))