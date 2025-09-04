from functools import cache

# class Solution:
# 	def getMaxLen(self, nums):
# 		ans = 0
# 		n = len(nums)
# 		for i in range(n):
# 			temp = 1
# 			for j in range(i, -1, -1):
# 				temp *= nums[j]
# 				if temp > 0:
# 					ans = max(ans, i - j + 1)
# 		return ans

## 状态机
class Solution:  
	def getMaxLen(self, nums):
		nums = [1] + nums
		n = len(nums)
		@cache
		def dfs(i, j):
			if j < 0:
				return 0
			if nums[i] * nums[j] > 0:
				return dfs(i - 1, j - 1) + 1
			elif nums[i] > 0:
				return max(dfs(i - 1, j - 1), 1)
			return dfs(i - 1, j - 1)
		return dfs(n - 1, n - 2)


if __name__ == '__main__':
	nums = [1, -2, -3, 4]
	print(Solution().getMaxLen(nums))