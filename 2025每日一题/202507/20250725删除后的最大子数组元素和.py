from collections import defaultdict
from itertools import accumulate
from math import inf

# class Solution:
# 	def maxSum(self, nums):
# 		pre_s = list(accumulate(nums, initial = 0))
# 		ans = -inf
# 		left = 0
# 		dic_win = defaultdict(int)
# 		for right, x in enumerate(pre_s[1:]):
# 			dic_win[nums[right]] += 1
# 			while dic_win[nums[right]] > 1:
# 				dic_win[nums[left]] -= 1
# 				left += 1
# 			ans = max(ans, x - min(pre_s[left:right + 1]))
# 		return ans


	
if __name__ == '__main__':
	nums = [-1,-2,3,4]
	print(Solution().maxSum(nums))