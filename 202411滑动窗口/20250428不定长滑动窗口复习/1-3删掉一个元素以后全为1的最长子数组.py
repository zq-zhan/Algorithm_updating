class Solution1:
	def longestSubarray(self, nums):
		cnt_win = 0
		ans = left = 0
		for right, c in enumerate(nums):
			cnt_win += (1 - c)
			while cnt_win > 1:
				cnt_win -= 1 - nums[left]
				left += 1
			ans = max(ans, right - left + 1 - cnt_win)
		return min(ans, len(nums) - 1)
	
if __name__ == '__main__':
	nums = [1,1,0,1]
	print(Solution1().longestSubarray(nums)) # Output: 4