from functools import cache

class Solution1:
	def findTargetSumWays(self, nums, target):
		n = len(nums)
		s = sum(nums)
		target = (target + s) // 2
		# if target % 2:
		# 	return 0
		@cache
		def dfs(i, c):
			if i < 0:
				return 1 if c == 0 else 0
			return dfs(i - 1, c) + dfs(i - 1, c - nums[i])
		return dfs(n - 1, target)
	
## 递推
class Solution2:
	def findTargetSumWays(self, nums, target):
		n = len(nums)
		s = sum(nums)
		target = (target + s) // 2
		# if target % 2:
		# 	return 0
		f = [[0] * (target + 1) for _ in range(n + 1)]
		f[0][0] = 1
		for i, x in enumerate(nums):
			for c in range(target + 1):
				if c >= x:
					f[i + 1][c] = f[i][c] + f[i][c - x]
				else:
					f[i + 1][c] = f[i][c]
		return f[n][target]
	
if __name__ == '__main__':
	nums = [1]
	target = 1
	print(Solution1().findTargetSumWays(nums, target))