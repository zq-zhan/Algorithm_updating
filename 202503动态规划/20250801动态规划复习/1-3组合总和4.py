from functools import cache

class Solution:
	def combinationSum4(self, nums, target):
		@cache
		def dfs(i, path_s):
			if path_s == target:
				return 1
			elif path_s > target:
				return 0
			return sum(dfs(i + 1, path_s + x) for x in nums)
		return dfs(0, 0)


if __name__ == '__main__':
	nums = [1, 2, 3]
	target = 4
	print(Solution().combinationSum4(nums, target))