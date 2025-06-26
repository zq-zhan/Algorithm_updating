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
	
class Solution3:
	def findTargetSumWays(self, nums, target):
		n = len(nums)
		@cache
		def dfs(i, c):
			if i < 0:
				return 1 if c == 0 else 0
			return dfs(i - 1, c - nums[i]) + dfs(i - 1, c + nums[i])
		return dfs(n - 1, target)
## 递推
class Solution4:
	def findTargetSumWays(self, nums, target):
		n = len(nums)
		s = sum(nums)
		if target > s:
			return 0
		f = [[0] * (s + 1) for _ in range(n + 1)]
		f[0][0] = 1
		for i, x in enumerate(nums):
			for c in range(s + 1):
				if c < x:
					f[i + 1][c] = f[i][c + x]
				else:
					f[i + 1][c] = f[i][c - x] + f[i][c + x]
		return f[-1][target]

## 递推——使用 f[i][c + s] 来表示和为 c 的情况，这样 c 的范围从 -s 到 s，就被映射到了 0 到 2s 的索引上。
class Solution5:
	def findTargetSumWays(self, nums, target):
		n = len(nums)
		s = sum(nums)
		if abs(target) > s:
			return 0
		f = [[0] * (2 * s + 1) for _ in range(n + 1)]
		f[0][s] = 1
		for i, x in enumerate(nums):
			for c in range(2 * s + 1):
				if c - x >= 0:
					f[i + 1][c] += f[i][c - x]
				if c + x <= 2 * s:
					f[i + 1][c] += f[i][c + x]
		return f[-1][s + target]

if __name__ == '__main__':
	nums = [1,1,1,1,1]
	target = 3
	print(Solution5().findTargetSumWays(nums, target))