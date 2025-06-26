from functools import cache
from math import inf

## 递归写法
class Solution1:
	def maxSubArray(self, nums):
		n = len(nums)
		# @cache
		def dfs(i):
			if i < 0:
				return 0
			return max(dfs(i - 1), 0) + nums[i]
		return max(dfs(j) for j in range(n))

## 递推空间优化
class Solution3:
	def maxSubArray(self, nums):
		# ans = -inf
		# f0 = 0
		# for x in nums:
		# 	f0 = max(f0, 0) + x
		# 	ans = max(ans, f0)
		# return ans
		ans = nums[0]
		f0 = nums[0]
		for i in range(1, len(nums)):
			f1 = max(f0, 0) + nums[i]
			ans = max(ans, f1)
			f0 = f1
		return ans
	
## 前缀和
class Solution4:
	def maxSubArray(self, nums):
		sub_pre = [0] * (len(nums) + 1)
		temp_sum = 0
		ans = -inf
		for i, x in enumerate(nums):
			temp_sum += x
			ans = max(ans, temp_sum - min(sub_pre))
			sub_pre[i + 1] = temp_sum
		return ans


## 递归写法
class Solution5:
	def maxSubArray(self, nums):
		@cache
		def dfs(i):
			if i < 0:
				return 0
			return max(dfs(i - 1), 0) + nums[i]
		n = len(nums)
		return max(dfs(x) for x in range(n))

class Solution6:
	def maxSubArray(self, nums):
		pre_s = [0] * (len(nums) + 1)
		# for i, c in enumerate(nums):
		# 	pre_s[i + 1] = pre_s[i] + x
		ans = -inf
		temp_s = 0
		for i, c in enumerate(nums):
			temp_s += c
			ans = max(ans, temp_s - min(pre_s))
			pre_s[i + 1] = pre_s[i] + c
		return ans

## 递推写法
class Solution7:
	def maxSubArray(self, nums):
		f0 = 0
		ans = -inf
		for i, c in enumerate(nums):
			# new_f = max(f0, 0) + c
			# f0 = new_f
			f0 = max(f0, 0) + c
			ans = max(ans, f0)
		return ans


if __name__ == '__main__':
	s = Solution7()
	nums = [-2,1,-3,4,-1,2,1,-5,4]
	print(s.maxSubArray(nums)) # Output: 6