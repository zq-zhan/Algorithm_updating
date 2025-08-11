from math import inf
from functools import cache
class Solution:
	def maximumSum(self, nums):
		def mxSub(arr):
			# n = len(arr)
			# @cache
			# def dfs(i):
			# 	if i < 0:
			# 		return 0
			# 	return max(dfs(i - 1), 0) + arr[i]
			# return max(dfs(i) for i in range(n))
			ans = -inf
			f = 0
			for x in nums:
				f = max(f, 0) + x
				ans = max(ans, f)
			return ans
		if all(x >= 0 for x in nums) or len(nums) == 1:
			return sum(nums)
		else:
			ans = -inf
			for j, x in enumerate(nums):
				if x < 0:
					ans = max(ans, mxSub(nums[:j] + nums[j + 1:]))
		return ans

class Solution:  
	def maximumSum(self, arr):
		@cache
		def dfs(i, j):
			if i < 0:
				return -inf
			if j == 0:
				return max(dfs(i - 1, 0), 0) + arr[i]
			return max(dfs(i - 1, 1) + arr[i], dfs(i - 1, 0))
		return max(max(dfs(i, 0), dfs(i, 1)) for i in range(len(arr)))


if __name__ == '__main__':
	arr = [-1,-1,-1,-1]
	print(Solution().maximumSum(arr))