from math import inf
from collections import Counter

class Solution:
	def getLargestOutlier(self, nums):
		s = sum(nums)
		ans = -inf
		dic_win = Counter(nums)
		for target_s in set(nums):
			dic_win[target_s] -= 1
			temp_diff = s - target_s
			if dic_win[temp_diff]:
				for temp_ans in dic_win:
					if dic_win[temp_ans]:
						dic_win[temp_ans] -= 1
						if target_s == sum(key for key in dic_win.keys() if dic_win[key] > 0):
							ans = max(ans, temp_ans)
						dic_win[temp_ans] += 1
			dic_win[target_s] += 1
		return ans
## 排序
class Solution:
	def getLargestOutlier(self, nums):
		s = sum(nums)
		nums.sort()
		right = len(nums) - 1
		for i, y in enumerate(nums):
			while right >= 0 and 2 * y > s - nums[right]:
				right -= 1
			if 2 * y == s - nums[right] and right != i:
				return nums[right]

if __name__ == '__main__':
	nums = [2,3,5,10]
	print(Solution().getLargestOutlier(nums))