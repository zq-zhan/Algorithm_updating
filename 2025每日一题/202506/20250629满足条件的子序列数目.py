class Solution:
	def numSubseq(self, nums, target):
		mod = 10 ** 9 + 7
		nums.sort()
		n = len(nums)
		ans = 0
		left, right = 0, n - 1
		while left <= right:
			if nums[left] + nums[right] > target:
				right -= 1
			else:
				ans = (2 ** (right - left) + ans) % mod
				left += 1
		return ans



if __name__ == '__main__':
	nums = [3,5,6,7]
	target = 9
	print(Solution().numSubseq(nums, target))