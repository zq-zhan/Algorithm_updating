from functools import cache

## 优化
class Solution1:
	def canPartition(self, nums):
		@cache
		def dfs(i, c):
			if i < 0:
				return c == 0
			return (c >= nums[i] and dfs(i - 1, c - nums[i])) or dfs(i - 1, c)
		s = sum(nums)
		return s % 2 == 0 and dfs(len(nums) - 1, s // 2)

## 递推写法
class Solution2:
	def canPartition(self, nums):
		n = len(nums)
		s = sum(nums)
		if s % 2:
			return False
		target = s // 2
		f = [[False] * (target + 1) for _ in range(n + 1)]
		f[0][0] = True
		for i, x in enumerate(nums):
			for c in range(target + 1):
				f[i + 1][c] = c >= x and f[i][c - x] or f[i][c]
				# if x > c:
				# 	f[i + 1][c] = f[i][c]
				# else:
				# 	f[i + 1][c] = f[i][c] or f[i][c - x]
		return f[n][target]
	
class Solution3:
	def canPartition(self, nums):
		s = sum(nums)
		if s % 2 == 1:
			return False
		@cache
		def dfs(i, c):
			if i < 0:
				return True if c == 0 else False
			if c < nums[i]:
				return dfs(i - 1, c)
			return dfs(i - 1, c) or dfs(i - 1, c - nums[i])
		return dfs(len(nums) - 1, s // 2)

if __name__ == '__main__':
	nums = [1, 5, 11 ,5]
	print(Solution3().canPartition(nums))