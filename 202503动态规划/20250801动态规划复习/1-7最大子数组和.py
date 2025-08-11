from functools import cache

class Solution:
	def maxSubArray(self, nums):
		n = len(nums)
		@cache
		def dfs(i):
			if i < 0:
				return 0
			return max(nums[i], dfs(i - 1) + nums[i])
		return max(dfs(i) for i in range(n))
	
if __name__ == '__main__':
	nums = [-2,1,-3,4,-1,2,1,-5,4]
	print(Solution().maxSubArray(nums))