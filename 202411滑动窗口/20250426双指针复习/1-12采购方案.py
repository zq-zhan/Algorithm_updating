class Solution1:
	def purchasePlans(self, nums, target):
		mod = 10 ** 9 + 7
		nums.sort()
		ans = 0
		left, right = 0, len(nums) - 1
		while left < right:
			if nums[left] + nums[right] <= target:
				ans += right - left
				left += 1
			else:
				right -= 1
		return ans

if __name__ == '__main__':
	nums = [2,5,3,5]
	target = 6
	print(Solution1().purchasePlans(nums, target))