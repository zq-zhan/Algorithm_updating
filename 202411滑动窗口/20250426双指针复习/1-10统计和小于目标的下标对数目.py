class Solution1:
	def countPairs(self, nums, target):
		nums.sort()
		n = len(nums)
		left, right = 0, n - 1
		ans = 0
		while left < right:
			if nums[left] + nums[right] < target:
				ans += right - left
				left += 1
			else:
				right -= 1
		return ans
	
if __name__ == '__main__':
	nums = [-1,1,2,3,1]
	target = 2
	print(Solution1().countPairs(nums, target))