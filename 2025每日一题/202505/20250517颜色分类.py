class Solution1:
	def sortColors(self, nums):
		left = 0
		for target in (0, 1):
			right = left
			while right < len(nums):
				if nums[right] == target:
					nums[left], nums[right] = nums[right], nums[left]
					left += 1
				right += 1
		return nums
					

					

			
if __name__ == '__main__':
	nums = [0,2,2,1,1,0]
	print(Solution1().sortColors(nums))