from math import inf
from itertools import accumulate

class Solution:
	def maxSubarraySum(self, nums, k):
		ans = -inf
		left = 0
		n = len(nums)
		while left < len(nums):
			temp_s = 0
			for right in range(left, n):
				temp_s += nums[right]
				if (right - left + 1) % k == 0:
					ans = max(temp_s, ans)
			left += 1
		return ans

## 灵神题解
class Solution:
	def maxSubarraySum(self, nums, k):
		pre = list(accumulate(nums, initial = 0))
		min_s = [inf] * k
		ans = -inf
		for j, s in enumerate(pre):
			i = j % k
			ans = max(ans, s - min_s[i])
			min_s[i] = min(min_s[i], s)
		return ans


if __name__ == '__main__':
	nums = [-5,1,2,-3,4]
	k = 2
	print(Solution().maxSubarraySum(nums, k))