from collections import defaultdict

class Solution1:
	def checkSubarraySum(self, nums, k):
		dic_win = defaultdict(int)
		dic_win[0] = -1
		temp_s = 0
		for i, x in enumerate(nums):
			temp_s += x
			target = dic_win.get(temp_s % k, i)
			if target == i:
				dic_win[temp_s % k] = i
			elif target <= i - 2:
				return True
		return False
	
class Solution:
	def checkSubarraySum(self, nums, k):
		dic_win = defaultdict(int)
		dic_win[0] = -1
		temp_s = 0
		for i, x in enumerate(nums):
			temp_s += x
			if temp_s % k in dic_win and i - dic_win[temp_s % k] + 1 >= 2:
				return True
			dic_win[temp_s % k] = min(dic_win[temp_s % k], i)
		return False

	
if __name__ == '__main__':
	nums = [1,2,12]
	k = 6
	print(Solution1().checkSubarraySum(nums, k))