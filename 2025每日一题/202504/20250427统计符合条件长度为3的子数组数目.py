class Solution1:
	def countSubarrays(self, nums):
		ans = left = 0
		for right, c in enumerate(nums):
			if right - left + 1 < 3:
				continue
			if nums[left] + nums[right] == nums[left + 1] // 2:
				ans += 1
			left += 1
			# if right - left + 1 == 3:
			# 	if nums[left] + nums[right] == nums[left + 1] // 2:
			# 		ans += 1
			# 	left += 1
		return ans
	
if __name__ == '__main__':
	nums = [1,2,1,4,1]
	print(Solution1().countSubarrays(nums))