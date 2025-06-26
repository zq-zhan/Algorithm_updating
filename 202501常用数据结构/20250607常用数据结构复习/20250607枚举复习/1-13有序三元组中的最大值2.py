from math import inf

class Solution:
	def maximumTripletValue(self, nums):
		n = len(nums)
		if n < 3:
			return 0
		# 后缀最大值
		mx_k = [nums[-1]] * n
		for i in range(n - 2, -1, -1):
			mx_k[i - n] = max(mx_k[i + 1], nums[i])

		mx_i = nums[0]
		ans = 0
		for j in range(1, n - 1):
			ans = max(ans, (mx_i - nums[j]) * mx_k[j + 1])
			mx_i = max(mx_i, nums[j])
		return ans



if __name__ == '__main__':
	nums = [12, 6, 1, 2, 7]
	print(Solution().maximumTripletValue(nums))