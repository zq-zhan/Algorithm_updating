# 5.连续的子数组和
from collections import defaultdict

class Solution1:
	def checkSubarraySum(self, nums, k):
		temp_sum = 0
		left = 0
		for right, c in enumerate(nums):
			temp_sum += c
			if right - left + 1 < 2:
				continue
			while right - left + 1 >= 2 and temp_sum % k == 0:
				return True
		return False

class Solution2:
	def checkSubarraySum(self, nums, k):
		# pre_sum = [0] * (len(nums) + 1)
		# for i, c in enumerate(nums):
		# 	pre_sum[i + 1] = pre_sum[i] + c

		pre_sum = [nums[0]]
		for i in range(1, len(nums)):
			pre_sum.append(pre_sum[-1] + nums[i])

		cnt = {0:-1}
		for j, sj in enumerate(pre_sum):
			i = cnt.get(sj % k, j)
			if i == j:
				cnt[sj % k] = j
			elif i <= j - 2:
				return True
		return False
	
if __name__ == '__main__':
	nums = [23,2,4,6,7]
	k = 6
	print(Solution2().checkSubarraySum(nums, k))