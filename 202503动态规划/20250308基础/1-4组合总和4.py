# 4.组合总和4
from functools import cache

class Solution1:
	def combinationSum4(self, nums, target):
		# n = len(nums)
		# min_num = min(nums)
		# @cache
		def dfs(i):
			if i == 0:
				return 1
			elif i < 0:
				return 0
			else:
				ori = 0
				for x in nums:
					# tag = 1 if dfs(i - x) > 0 else 0
					ori += dfs(i - x) if i >= x else 0
				return ori
		return dfs(target)
## 递推
class Solution2:
	def combinationSum4(self, nums, target):
		f = [0] * (target + 1)
		f[0] = 1
		for i in range(1, target + 1):
			for x in nums:
				f[i] += f[i - x] if i >= x else 0
		return f[-1]
	
## 递推空间优化（无法优化）
class Solution3:
	def combinationSum4(self, nums, target):
		f0 = 0
		f1 = 1
		for i in range(1, target + 1):
			new_f = 0
			for x in nums:
				new_f += f1 if i >= x else 0
			f0 = f1
			f1 = new_f
		return f1
	
if __name__ == '__main__':
	nums = [1, 2, 3]
	target = 4
	s = Solution3()
	print(s.combinationSum4(nums, target))