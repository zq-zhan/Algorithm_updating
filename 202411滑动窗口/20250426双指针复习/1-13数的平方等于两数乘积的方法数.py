class Solution1:
	def numTriplets(self, nums1, nums2):
		def upper(nums, target):
			nums.sort()
			ans = 0
			left, right = 0, len(nums) - 1
			while left < right:
				if nums[left] * nums[right] <= target:
					ans += right - left 
					left += 1
				else:
					right -= 1
			return ans

		ans_result = 0
		for x in nums1:
			ans_result += upper(nums2, x ** 2) - upper(nums2, x ** 2 - 1)
		for y in nums2:
			ans_result += upper(nums1, y ** 2) - upper(nums1, y ** 2 - 1)
		return ans_result
	
	
if   __name__ == '__main__':
	nums1 = [7,4]
	nums2 = [5,2,8,9]
	print(Solution1().numTriplets(nums1, nums2))