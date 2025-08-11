from functools import cache

class Solution:
	def canPartition(self, nums):
		s = sum(nums)
		if s % 2:
			return False
		n = len(nums)
		@cache
		def dfs(i, temp_s):
			if i < 0 or temp_s > s // 2:
				return temp_s == s // 2
			return dfs(i - 1, temp_s + nums[i]) or dfs(i - 1, temp_s)
		return dfs(n - 1, 0)
	
if __name__ == '__main__':
	nums = [1, 5, 11, 5]
	print(Solution().canPartition(nums))