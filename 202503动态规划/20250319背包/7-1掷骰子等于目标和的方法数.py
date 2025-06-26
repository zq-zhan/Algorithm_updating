from functools import cache

# 1.掷骰子等于目标和的方法数
class Solution1:
	def numRollsToTarget(self, n, k, target):
		## 优化
		if not (n <= target <= n * k):
			return 0
		mod = 10 ** 9 + 7
		@cache
		def dfs(i, c):
			if i == 0:
				return 1 if c == 0 else 0
			res = 0
			for j in range(1, min(k, c) + 1):
				res += dfs(i - 1, c - j)
			return res % mod
		return dfs(n, target)
## 递推写法
class Solution2:
	def numRollsToTarget(self, n, k, target):
		## 优化
		if not (n <= target <= n * k):
			return 0
		mod = 10 ** 9 + 7
		f = [[0] * (target + 1) for _ in range(n + 1)]
		f[0][0] = 1  # dfs(0, 0) = 1
		for i in range(1, n + 1):
			for j in range(target + 1):
				for x in range(1, min(k, j) + 1):
					f[i][j] = (f[i][j] + f[i - 1][j - x]) % mod
		return f[-1][-1]


if __name__ == '__main__':
	n = 2
	k = 6
	target = 7
	print(Solution2().numRollsToTarget(n, k, target)) # Output: 6