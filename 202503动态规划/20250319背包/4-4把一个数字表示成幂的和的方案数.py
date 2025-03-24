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
	
if __name__ == '__main__':
	n = 10
	x = 2
	print(Solution1().numberOfWays(n, x))