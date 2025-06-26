class Solution1:
	def removeElement(self, nums, val):
		ans = 0
		left, right = 0, len(nums) - 1
		while left <= right:
			if nums[left] == val:
				nums[left], nums[right] = nums[right], nums[left]
				right -= 1
			else:
				left += 1
				ans += 1
		return ans

if __name__ == '__main__':
	nums = [3,2,2,3]
	val = 3
	print(Solution1().removeElement(nums, val))