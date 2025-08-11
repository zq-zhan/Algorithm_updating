from math import inf

class Solution:
	def maxAbsoluteSum(self, nums):
		ans = temp_s = 0
		min_s = inf
		for x in nums:
			temp_s += x
			ans = max(ans, abs(temp_s) - min_s, abs(x))
			min_s = min(min_s, abs(temp_s), abs(x))
		return ans		
	
if __name__ == '__main__':
	nums = [1,-3,2,3,-4]
	print(Solution().maxAbsoluteSum(nums))