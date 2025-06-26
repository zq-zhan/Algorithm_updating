class Solution1:
	def numSubseq(self, nums, target):
		nums.sort()
		ans = 0
		left, right = 0, len(nums) - 1
		while left <= right:
			if nums[left] + nums[right] <= target:
				ans += 2 ** (right - left)  # 以left最小元素
				left += 1
			else:
				ans += 1 if nums[right] * 2 <= target else 0
				right -= 1
		return ans
	
if __name__ == '__main__':
	nums = [3,5,6,7]
	target = 9
	print(Solution1().numSubseq(nums, target))