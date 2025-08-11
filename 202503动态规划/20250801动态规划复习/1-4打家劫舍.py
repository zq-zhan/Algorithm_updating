from functools import cache

class Solution:
	def rob(self, nums):
		n = len(nums)
		# @cache
		def dfs(i):
			if i < 0:
				return 0
			return max(dfs(i - 1), dfs(i - 2) + nums[i])
		return dfs(n - 1)
	
if __name__ == '__main__':
	nums = [1,2,3,1]
	print(Solution().rob(nums))