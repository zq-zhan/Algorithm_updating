from math import inf

class Solution:
	def maxAbsoluteSum(self, nums):
		n = len(nums)
		suf_s = [0] * (n + 1)
		for i, x in enumerate(nums):
			suf_s[i + 1] = suf_s[i] + x

		diff_s = -inf
		pre_mn = 0
		pre_mx = 0
		for i in range(1, n + 1):
			diff_s = max(diff_s, abs(suf_s[i] - pre_mn), abs(suf_s[i] - pre_mx))
			pre_mn = min(pre_mn, suf_s[i])
			pre_mx = max(pre_mx, suf_s[i])
		return diff_s

if __name__ == '__main__':
	nums = [6]
	print(Solution().maxAbsoluteSum(nums))