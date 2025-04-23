from functools import cache

# 1.检查数组是否存在有效划分
class Solution1:
	def validPartition(self, nums):
		n = len(nums)
		f = [True] + [False] * n
		for i in range(n):
			if (i > 0 and f[i - 1] and nums[i] == nums[i - 1]) or \
				(i > 1 and f[i - 2] and (nums[i] == nums[i - 1] == nums[i - 2] or \
					nums[i] == nums[i - 1] + 1 == nums[i - 2] + 2)):
				f[i + 1] = True
		return f[-1]
## 递归
class Solution2:
	def validPartition(self, nums):
		@cache
		def dfs(i):
			if i == -1:
				return True
			elif i == 0:
				return False
			res = False
			if nums[i] == nums[i - 1]:
				res |= dfs(i - 2)
			if i > 1 and (nums[i] == nums[i - 1] == nums[i - 2] or nums[i] == nums[i - 1] + 1 == nums[i - 2] + 2):
				res |= dfs(i - 3)
			return res
		return dfs(len(nums) - 1)

if __name__ == '__main__':
	nums = [4,4,4,5,6]
	print(Solution2().validPartition(nums))