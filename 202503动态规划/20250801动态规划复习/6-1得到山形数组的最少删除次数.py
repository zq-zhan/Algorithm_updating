from functools import cache

class Solution:
	def minimumMountainRemovals(self, nums):
		n = len(nums)
		@cache
		def dfs_add(i):
			res = 0
			for j in range(i):
				if nums[j] < nums[i]:
					res = max(res, dfs_add(j))
			return res + 1
		@cache
		def dfs_diff(i):
			res = 0
			for j in range(i + 1, n):
				if nums[j] < nums[i]:
					res = max(res, dfs_diff(j))
			return res + 1
		ans = 3
		for i in range(n):
			left = dfs_add(i)
			right = dfs_diff(i)
			if left >= 2 and right >= 2:
				ans = max(ans, left + right - 1)
		return n - ans


if __name__ == '__main__':
	nums = [100,92,89,77,74,66,64,66,64]
	print(Solution().minimumMountainRemovals(nums))