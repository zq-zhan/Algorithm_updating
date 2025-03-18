# 2.子数组最大平均数1
from math import inf

class Solution1:
	def findMaxAverage(self, nums, k):
		ans = -inf
		temp_sum = 0
		for i, c in enumerate(nums):
			temp_sum += c
			if i < k - 1:
				continue
			ans = max(ans, temp_sum/k)
			temp_sum -= nums[i - k + 1]
		return ans
	
class Solution2:
	def findMaxAverage(self, nums, k):
		ans = -inf
		temp_ans = 0
		for left, x in enumerate(nums):
			temp_ans += x
			if left >= k - 1:
				ans = max(ans, temp_ans / k)
				temp_ans -= nums[left - k + 1]
		return ans

if __name__ == '__main__':
	nums = [1,12,-5,-6,50,3]
	k = 4
	print(Solution2().findMaxAverage(nums, k))