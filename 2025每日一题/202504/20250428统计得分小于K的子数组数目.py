class Solution1:
	def countSubarrays(self, nums, k):
		# n = len(nums)
		ans = left = 0
		tmp_sum = 0
		for right, c in enumerate(nums):
			tmp_sum += c
			while tmp_sum * (right - left + 1) >= k:
				tmp_sum -= nums[left]
				left += 1
			ans += right - left + 1
		return ans
	
if __name__ == '__main__':
	nums = [2,1,4,3,5]
	k = 10
	print(Solution1().countSubarrays(nums, k))