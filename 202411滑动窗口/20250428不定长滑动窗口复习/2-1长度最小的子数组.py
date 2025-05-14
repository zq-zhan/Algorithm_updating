class Solution1:
	def minSubArrayLen(self, target, nums):
		ans = len(nums) + 1
		left = 0
		temp_sum = 0
		for right, c in enumerate(nums):
			temp_sum += c
			while temp_sum >= target:
				ans = min(ans, right - left + 1)
				temp_sum -= nums[left]
				left += 1
		return ans if ans < len(nums) + 1 else 0
	
if __name__ == '__main__':
	target = 7
	nums = [2,3,1,2,4,3]
	print(Solution1().minSubArrayLen(target, nums))