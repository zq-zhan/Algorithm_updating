from functools import cache

class Solution1:  # （错解）
	def rob(self, nums):
		n = len(nums)
		tag = True
		@cache
		def dfs(i):
			if i <= 0:
				return 0
			if tag:
				return max(dfs(i - 1) + nums[0], dfs(i - 2) + nums[i])
			else:
				return max(dfs(i - 1), dfs(i - 2) + nums[i])
			tag = False
		return dfs(n - 1)
## 递推写法(错解)
class Solution2:
	def rob(self, nums):
		n = len(nums)
		f = [0] * n
		f[0] = nums[0]
		f[1] = max(nums[1], f[0])
		for i in range(2, n):
			f[i] = max(f[i - 1], f[i - 2] + nums[i])
## 灵神题解
class Solution3:
	def rob(self, nums):
		def rob_normal(nums):
			f0 = f1 = 0
			for x in nums:
				new_f = max(f1, f0 + x)
				f0 = f1
				f1 = new_f
			return f1
		ans = max(nums[0] + rob_normal(nums[2:-1]), rob_normal(nums[1:]))
		return ans
## 递归写法
class Solution4:
	def rob(self, nums):
		def rob_normal(nums):
			n = len(nums)
			@cache
			def dfs(i):
				if i < 0:
					return 0
				return max(dfs(i - 1), dfs(i - 2) + nums[i])
			return dfs(n - 1)
		ans = max(nums[0] + rob_normal(nums[2:-1]), rob_normal(nums[1:]))
		return ans

if __name__ == '__main__':
	nums = [2, 3, 2]
	print(Solution4().rob(nums))
	# print(Solution2().rob(nums))