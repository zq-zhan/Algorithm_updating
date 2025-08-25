# class Solution:
# 	def longestSubarray(self, nums):
# 		ans = cnt = left = 0
# 		for right, x in enumerate(nums):
# 			while x == 0 and cnt == 1:
# 				cnt -= int(nums[left] == 0)
# 				left += 1
# 			cnt += int(x == 0)
# 			ans = max(ans, right - left + 1 - cnt)
# 		return ans

## 不定长滑动窗口解法
class Solution:
	def longestSubarray(self, nums):
		cnt_win = 0
		ans = 0 
		left = 0
		for right, c in enumerate(nums):
			cnt_win += 1 if c == 0 else 0
			while cnt_win > 1:
				cnt_win -= 1 if nums[left] == 0 else 0
				left += 1
			ans = max(ans, right - left)
		return ans
	
if __name__ == '__main__':
	nums = [0,1,1,1]
	print(Solution().longestSubarray(nums)) # Output: 3