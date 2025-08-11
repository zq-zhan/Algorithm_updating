from collections import Counter
from functools import cache


class Solution:
	def deleteAndEarn(self, nums):
		mn, mx = min(nums), max(nums)
		new_num = list(range(mn, mx + 1))
		n = mx - mn + 1
		nums = Counter(nums)
		@cache
		def dfs(i):
			if i < 0:
				return 0
			x = new_num[i]
			return max(dfs(i - 1), dfs(i - 2) + x * nums[x])
		return dfs(n - 1)
	
if __name__ == '__main__':
	nums = [2,2,3,3,3,4]
	print(Solution().deleteAndEarn(nums))
