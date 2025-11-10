class Solution:
	def hasIncreasingSubarrays(self, nums, k):
		left = before = 0
		nums.append(-1001)
		n = len(nums)
		for right in range(1, n):
			if nums[right] > nums[right - 1]:
				continue
			if (before >= k and right - left >= k) or right - left >= 2*k:
				return True
			before = right - left
			left = right
		return False

if __name__ == '__main__':
	# nums = [2,5,7,8,9,2,3,4,3,1]
	# k = 3
	nums = [-15, 19]
	k = 1
	print(Solution().hasIncreasingSubarrays(nums, k))