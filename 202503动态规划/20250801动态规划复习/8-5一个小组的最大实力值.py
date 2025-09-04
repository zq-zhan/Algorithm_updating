from functools import cache
from math import inf

## 回溯写法
class Solution:
	def maxStrength(self, nums):
		res = -inf
		path = []
		def dfs(i):
			nonlocal res
			if i < 0:
				if path:
					temp = 1
					for x in path:
						temp *= x
					res = max(res, temp)
				return
			# 选
			path.append(nums[i])
			dfs(i - 1)
			path.pop()

			# 不选
			dfs(i - 1)
		dfs(len(nums) - 1)
		return res
## 回溯写法二
class Solution:
	def maxStrength(self, nums):
		n = len(nums)
		ans = -inf
		def dfs(i, temp, k):
			nonlocal ans
			if i < 0:
				if k:
					ans = max(ans, temp)
				return
			## 选
			dfs(i - 1, temp * nums[i], k + 1)
			## 不选
			dfs(i - 1, temp, k)
		dfs(n - 1, 1, 0)
		return ans
	
if __name__ == '__main__':
	nums = [3,-1,-5,2,5,-9]
	print(Solution().maxStrength(nums))