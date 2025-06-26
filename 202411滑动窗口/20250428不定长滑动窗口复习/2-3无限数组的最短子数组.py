from math import inf

class Solution1:
	def minSizeSubarray(self, nums, target):
		n = len(nums)
		s = sum(nums)
		cnt = target // s
		target = target % s
		if target == 0:
			return cnt * n
		ans = inf
		left = temp_sum = 0
		nums = nums + nums
		for right, c in enumerate(nums):
			temp_sum += c
			while temp_sum >= target:
				if temp_sum == target:
					ans = min(ans, right - left + 1)
				temp_sum -= nums[left]
				left += 1
		return ans + cnt * n if ans < inf else -1
	
if __name__ == '__main__':
	nums = [1,6,5,5,1,1,2,5,3,1,5,3,2,4,6,6]
	target = 56
	print(Solution1().minSizeSubarray(nums, target))