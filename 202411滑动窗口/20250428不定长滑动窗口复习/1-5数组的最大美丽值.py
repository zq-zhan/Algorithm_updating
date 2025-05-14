# 5.数组的最大美丽值
class Solution1:
	def maximumBeauty(self, nums, k):
		nums.sort()
		ans = left = 0
		for right, c in enumerate(nums):
			while c - nums[left] > 2 * k:
				left += 1
			ans = max(ans, right - left + 1)
		return ans
	
if __name__ == '__main__':
	nums = [4,6,1,2]
	k = 2
	print(Solution1().maximumBeauty(nums, k)) # Output: 3