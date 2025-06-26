class Solution1:
	def numSubarrayProductLessThanK(self, nums, k):
		if min(nums) >= k:
			return 0
		temp_plus = 1
		ans = left = 0
		for right, c in enumerate(nums):
			temp_plus *= c
			while temp_plus >= k:
				temp_plus /= nums[left]
				left += 1
			ans += right - left + 1
		return ans
	
if __name__ == '__main__':
	nums = [10, 5, 2, 6]
	k = 100
	print(Solution1().numSubarrayProductLessThanK(nums, k))