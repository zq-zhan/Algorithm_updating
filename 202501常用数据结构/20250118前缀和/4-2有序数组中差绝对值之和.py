# 2.有序数组中差绝对值之和
from itertools import accumulate
from bisect import bisect_left

class Solution1:
	def getSumAbsoluteDifferences(self, nums):
		n = len(nums)
		s = list(accumulate(nums, initial = 0))
		ans = []
		for q in nums:
			j = bisect_left(nums, q)
			left = q * j - s[j]
			right = s[n] - s[j] - q * (n - j)
			ans.append(left + right)
		return ans
	
if __name__ == '__main__':
	nums = [2,3,5]
	cls = Solution1()
	print(cls.getSumAbsoluteDifferences(nums))