from collections import defaultdict

# 1.绝对差不超过限制的最长连续子数组
class Solution1:
	def longestSubarray(self, nums, limit):
		ans = left = 0
		dic_win = defaultdict(int)
		for right, c in enumerate(nums):
			dic_win[c] += 1
			while max(dic_win.keys()) - min(dic_win.keys()) > limit:
				if dic_win[nums[left]] == 1:
					del dic_win[nums[left]]
				else:
					dic_win[nums[left]] -= 1
				left += 1
			ans = max(ans, right - left + 1)
		return ans
	
if __name__ == '__main__':
	nums = [8,2,4,7]
	limit = 4
	print(Solution1().longestSubarray(nums, limit))