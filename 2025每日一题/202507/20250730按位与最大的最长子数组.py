class Solution:
	def longestSubarray(self, nums):
		mx_num = max(nums)
		ans = 1
		i = 0
		n = len(nums)
		while i < n:
			if nums[i] == mx_num:
				start = i
				while i < n and nums[i] == mx_num:
					i += 1
				ans = max(ans, i - start)
			i += 1
		return ans
				

if __name__ == '__main__':
	nums = [1,2,3,3,2,2]
	print(Solution().longestSubarray(nums))