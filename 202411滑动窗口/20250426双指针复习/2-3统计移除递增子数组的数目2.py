class Solution1:
	def incremovableSubarrayCount(self, nums):
		n = len(nums)
		right = n - 1 
		while right > 0 and nums[right - 1] < nums[right]:
			right -= 1
		if right == 0:
			return n * (n + 1) // 2

		ans = n - right + 1
		left = 0
		while left == 0 or nums[left] > nums[left - 1]:
			while right < n and nums[right] <= nums[left]:
				right += 1
			ans += n - right + 1
			left += 1
		return ans
	
if __name__ == '__main__':
	nums = [8,7,6,6]
	print(Solution1().incremovableSubarrayCount(nums))