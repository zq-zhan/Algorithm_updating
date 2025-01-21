# 2.子数组最大平均数1
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