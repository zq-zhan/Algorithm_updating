from functools import cache
import math

class Solution1:
	def numberOfWays(self, n, x):
		mod = (10 ** 9) + 7
		target = int(math.pow(n, 1/x)) + 1
		nums = [num for num in range(1, target + 1)]
		@cache
		def dfs(i, c):
			if i < 0 or c < 0:
				return 1 if c == 0 else 0
			return (dfs(i - 1, c) + dfs(i - 1, c - nums[i] ** x)) % mod
		return dfs(len(nums) - 1, n) % mod
	
class Solution2:
	def numberOfWays(self, n, x):
		mod = 10 ** 9 + 7
		target = int(math.pow(n, 1/x)) + 1
		@cache
		def dfs(i, c):
			if i == 0:
				return 1 if c == 0 else 0
			return dfs(i - 1, c - i ** x) + dfs(i - 1, c)
		return dfs(target, n) % mod
	
class Solution3:
	def numberOfWays(self, n, x):
		mod = 10 ** 9 + 7
		left, right = 0, n + 1
		while left + 1 < right:
			mid = (left + right) // 2
			if mid ** x >= n:
				right = mid
			else:
				left = mid

		@cache
		def dfs(i, c):
			if i == 0:
				return 1 if c == 0 else 0
			return dfs(i - 1, c - i ** x) + dfs(i - 1, c)
		return dfs(right, n) % mod

## 递推写法
class Solution4:
	def numberOfWays(self, n, x):
		mod = 10 ** 9 + 7
		left, right = 0, n + 1
		while left + 1 < right:
			mid = (left + right) // 2
			if mid ** x >= n:
				right = mid
			else:
				left = mid

		f = [[0] * (n + 1) for _ in range(right + 1)]
		f[0][0] = 1
		for i in range(right):
			for c in range(n + 1):
				if c < (i + 1) ** x:
					f[i + 1][c] = f[i][c]
				else:
					f[i + 1][c] = f[i][c] + f[i][c - (i + 1) ** x]
		return f[-1][-1] % mod


class Solution5:
	def numberOfWays(self, n, x):
		# mod = 10 ** 9 + 7
		# left, right = 0, n + 1
		# while left + 1 < right:
		# 	mid = (left + right) // 2
		# 	if mid ** x >= n:
		# 		right = mid
		# 	else:
		# 		left = mid
		mod = (10 ** 9) + 7
		target = int(math.pow(n, 1/x)) + 1
		
		@cache
		def dfs(i, c):
			# if i <= 0:
			# 	return 1 if c == 0 else 0
			# if c < i ** x:
			# 	return dfs(i - 1, c) % mod
			## 优化
			if i <= 0 or c <= 0:
				return 1 if c == 0 else 0
			return (dfs(i - 1, c - i ** x) + dfs(i - 1, c)) % mod
		return dfs(target, n) % mod


if __name__ == '__main__':
	n = 4
	x = 2
	print(Solution5().numberOfWays(n, x))