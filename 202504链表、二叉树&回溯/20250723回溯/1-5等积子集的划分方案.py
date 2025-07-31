from functools import cache

class Solution:
	def checkEqualPartitions(self, nums, target):
		plus_s = 1
		n = len(nums)
		for x in nums:
			plus_s *= x
		@cache
		def dfs(i, temp_plus):
			if i == n:
				return temp_plus == target and plus_s // temp_plus == target
			return dfs(i + 1, temp_plus * nums[i]) or dfs(i + 1, temp_plus)
		return dfs(0, 1)
	
if __name__ == '__main__':
	nums = [3,1,6,8,4]
	target = 24
	print(Solution().checkEqualPartitions(nums, target))