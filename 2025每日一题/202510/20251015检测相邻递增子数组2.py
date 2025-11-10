from math import inf

class Solution:
	def maxIncreasingSubarrays(self, nums):
		ans = 1
		nums.append(-inf)
		left = before = 0
		n = len(nums)
		for right in range(1, n):
			if nums[right] > nums[right - 1]:
				continue
			ans = max(ans, (right - left) // 2, min(before, right - left))
			before = right - left
			left = right
		return ans
	
if __name__ == '__main__':
	nums = [2,5,7,8,9,2,3,4,3,1]
	print(Solution().maxIncreasingSubarrays(nums))