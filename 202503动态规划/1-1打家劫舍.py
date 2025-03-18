# 1.打家劫舍
from functools import cache


class Solution1:  # 贪心做法是错误的
	def rob(self, nums):
		choose_1 = 0
		choose_2 = 0
		for i, c in enumerate(nums):
			if i % 2 == 0:
				choose_1 += c
			else:
				choose_2 += c
		return max(choose_1, choose_2)
##
class Solution2:
	def rob(self, nums):
		@cache
		def dfs(i):
			if i >= 2:
				return max(dfs(i - 1), dfs(i - 2) + nums[i])
			elif i == 1:
				return max(dfs(0), nums[1])
			else:
				return nums[0]

		n = len(nums)
		return dfs(n - 1)
	
## 递归写法
class Solution3:
	def rob(self, nums):
		n = len(nums)
		f = [0] * n
		f[0] = nums[0]
		for i in range(1, n):
			if i >= 2:
				f[i] = max(f[i - 1], f[i - 2] + nums[i])
			elif i == 1:
				f[i] = max(nums[0], nums[1])
		return f[n - 1]
	
if __name__ == '__main__':
	s = Solution3()
	print(s.rob([1,2,3,1]))