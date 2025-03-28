from functools import cache

## 值域数组
class Solution1:
	def deleteAndEarn(self, nums):
		n = max(nums) + 1
		a = [0] * n
		for x in nums:
			a[x] += x
		@cache
		def dfs(i):
			if i < 0:
				return 0
			return max(dfs(i - 1), dfs(i - 2) + a[i])
		return dfs(n - 1)
	
## 递推写法
class Solution2:
	def deleteAndEarn(self, nums):
		n = max(nums) + 1
		a = [0] * n
		for x in nums:
			a[x] += x
		f = [0] * n
		f[0] = 0
		f[1] = max(f[0], a[1])
		for i in range(2, n):
			f[i] = max(f[i - 1], f[i - 2] + a[i])
		return f[-1]
## 递推空间优化
class Solution3:
	def deleteAndEarn(self, nums):
		n = max(nums) + 1
		a = [0] * n
		for x in nums:
			a[x] += x
		f0 = f1 = 0
		for x in a:
			new_f = max(f1, f0 + x)
			f0 = f1
			f1 = new_f
		return f1
	
class Solution4:
	def deleteAndEarn(self, nums):
		n = max(nums) + 1
		a = [0] * n
		for x in nums:
			a[x] += x
		@cache
		def dfs(i):
			if i < 0:
				return 0
			return max(dfs(i - 1), dfs(i - 2) + a[i])
		return dfs(n - 1)


if __name__ == '__main__':
	s = Solution4()
	nums = [3, 4, 2]
	print(s.deleteAndEarn(nums)) # Output: 6