class Solution1:
	def transformArray(self, nums):
		# if len(nums) == 1:
		# 	return [nums[-1] % 2]

		left, right = 0, len(nums) - 1
		while left <= right:
			if nums[left] % 2 == 0:
				nums[left] = 0
				left += 1
			else:
				nums[left] = 1

			if left <= right:
				if nums[right] % 2 == 0:
					nums[right] = nums[left]
					nums[left] = 0
					left += 1
				else:
					nums[right] = 1
					right -= 1
		return nums
	
if __name__ == '__main__':
	nums = [2]
	print(Solution1().transformArray(nums))