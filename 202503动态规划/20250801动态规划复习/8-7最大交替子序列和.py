from functools import cache

class Solution:
	def maxAlternatingSum(self, nums):
		@cache
		def dfs(i, t):
			if i < 0:
				return 0
			if t % 2 == 0:
				return max(dfs(i - 1, t ^ 1) - nums[i], dfs(i - 1, t))
			return max(dfs(i - 1, t ^ 1) + nums[i], dfs(i - 1, t))
		return dfs(len(nums) - 1, 1)
	
if __name__ == '__main__':
	nums = [4,2,5,3]
	print(Solution().maxAlternatingSum(nums))