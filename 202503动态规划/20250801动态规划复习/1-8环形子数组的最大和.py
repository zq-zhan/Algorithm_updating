from functools import cache

class Solution:
	def maxSubarraySumCircular(self, nums):
		n = len(nums)
		nums = nums + nums
		@cache
		def dfs(i, x):
			if i != n and i % n == x:
				return 0
			return max(nums[i % n], dfs(i - 1, x) + nums[i % n])
		return max(dfs(i + n, i) for i in range(n))
	
if __name__ == '__main__':
	nums = [1,-2,3,-2]
	print(Solution().maxSubarraySumCircular(nums))