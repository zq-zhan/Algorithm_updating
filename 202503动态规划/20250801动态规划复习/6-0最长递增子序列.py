from bisect import bisect_right
from functools import cache

class Solution:  # 用LCS求LIS
	def lengthOfLIS(self, nums):
		new_nums = sorted(set(nums))
		n, m = len(nums), len(new_nums)
		@cache
		def dfs(i, j):
			if i < 0 or j < 0:
				return 0
			if nums[i] == new_nums[j]:
				return dfs(i - 1, j - 1) + 1
			return max(dfs(i - 1, j), dfs(i, j - 1))
		return dfs(n - 1, m - 1)
## 灵神思路——枚举选哪个
class Solution:  
	def lengthOfLIS(self, nums):
		n = len(nums)
		@cache
		def dfs(i):
			res = 0
			for j in range(i):
				if nums[j] < nums[i]:
					res = max(res, dfs(j))
			return res + 1
		return max(dfs(i) for i in range(n))
class Solution:  # 二分查找
	def lengthOfLIS(self, nums):
		g = []
		for x in nums:
			j = bisect_right(g, x)
			if j == len(g):
				g.append(x)
			else:
				g[j] = x
		return len(g) 
	
if __name__ == '__main__':
	nums = [10,9,2,5,3,7,101,18]
	print(Solution().lengthOfLIS(nums))