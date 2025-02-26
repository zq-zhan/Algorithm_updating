# 使结果不超过阈值的最小除数
from math import ceil

class Solution1:
	def smallestDivisor(self, nums, threshold):
		nums.sort()
		for i in range(1,nums[-1] + 1):
			cum_sum = 0
			j = len(nums) - 1
			while j >= 0 and cum_sum <= threshold:
				cum_sum += ceil(nums[j] / i)
				j -= 1

			if j < 0 and cum_sum <= threshold:
				return i
			
## 灵神二分法思路
class Solution2:
	def smallestDivisor(self, nums, threshold):
		left, right = 0, max(nums)
		while left + 1 < right:
			mid = (left + right) // 2
			if sum((x - 1) // mid for x in nums) <= threshold - len(nums):
				right = mid
			else:
				left = mid
		return right

# 8.使结果不超过阈值的最小除数
class Solution3:
	def smallestDivisor(self, nums, threshold):
		left, right = 0, max(nums) + 1
		while left + 1 < right:
			mid = (left + right) // 2
			if sum((x - 1) // mid + 1 for x in nums) <= threshold:
				right = mid
			else:
				left = mid
		return right
			
if __name__ == '__main__':
	nums = [44,22,33,11,1]
	threshold = 5
	s = Solution3()
	print(s.smallestDivisor(nums, threshold))