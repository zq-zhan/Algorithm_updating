from functools import cache
from math import inf

class Solution:
	def maximumTotalCost(self, nums):
		@cache
		def cost(i, j):
			res = 0
			for k, x in enumerate(nums[i:j + 1]):
				res += x * (-1) ** k
			return res
		@cache
		def dfs(i):
			if i < 0:
				return 0
			res = -inf
			for j in range(i + 1):
				res = max(res, dfs(j - 1) + cost(j, i))
			return res
		return dfs(len(nums) - 1)

if __name__ == '__main__':
	nums = [-937]
	print(Solution().maximumTotalCost(nums))