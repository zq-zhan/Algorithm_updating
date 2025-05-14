from collections import Counter

class Solution1:
	def maxFrequency(self, nums, k):
		ans = 1
		left = 0
		nums.sort()
		n = len(nums)
		for right in range(1, n):
			# if nums[right] == nums[right - 1] or nums[right] - nums[right - 1] <= cnt:
			# 	k -= nums[right] - nums[right - 1]
			# 	ans = max(ans, right - left + 1)
			# else:
			# 	while k < 0:
			# 		k += nums[left + 1] - nums[left]
			# 		left += 1
			k -= (nums[right] - nums[right - 1]) * (right - left)
			while k < 0:
				k += nums[right] - nums[left]
				left += 1
			ans = max(ans, right - left + 1)
		return ans
	
if __name__ == '__main__':
	nums = [9930,9923,9983,9997,9934,9952,9945,9914,9985,9982,9970,9932,9985,9902,9975,9990,9922,9990,9994,9937,9996,9964,9943,9963,9911,9925,9935,9945,9933,9916,9930,9938,10000,9916,9911,9959,9957,9907,9913,9916,9993,9930,9975,9924,9988,9923,9910,9925,9977,9981,9927,9930,9927,9925,9923,9904,9928,9928,9986,9903,9985,9954,9938,9911,9952,9974,9926,9920,9972,9983,9973,9917,9995,9973,9977,9947,9936,9975,9954,9932,9964,9972,9935,9946,9966]
	k = 3056
	print(Solution1().maxFrequency(nums, k))