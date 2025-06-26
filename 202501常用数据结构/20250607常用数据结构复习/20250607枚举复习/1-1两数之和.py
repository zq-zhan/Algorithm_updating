from collections import defaultdict

class Solution:
	def twoSum(self, nums, target):
		n = len(nums)
		dic_left = defaultdict(int)
		for i, x in enumerate(nums):
			if target - x in dic_left:
				return [dic_left[target - x], i]
			dic_left[x] = i
			
if __name__ == '__main__':
	nums = [2, 7, 11, 15]
	target = 9
	print(Solution().twoSum(nums, target))