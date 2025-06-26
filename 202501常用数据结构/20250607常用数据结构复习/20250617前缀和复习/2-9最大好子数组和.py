from collections import defaultdict
from math import inf

class Solution:
	# 这种思路都是错误的，因为nums[i]可能是负数，不是子数组越长和越大
	def maximumSubarraySum(self, nums, k):
		dic_win = defaultdict(lambda : inf)
		ans = -inf
		for i, x in enumerate(nums):
			a = dic_win[x + k]
			b = dic_win[x - k]
			ans = max(ans, sum(nums[a:i + 1]), sum(nums[b:i + 1]))
			dic_win[x] = min(dic_win[x], i)
		return ans if ans > -inf else 0
## 灵神题解
class Solution:
	# 在保证|a[i] - a[j]|=k时维护前缀和最小，从而子数组和最大
	def maximumSubarraySum(self, nums, k):
		ans = -inf
		min_s = defaultdict(lambda:inf)  # 存储至相同a[i]下s[i]的最小值
		pre_s = 0
		for x in nums:
			ans = max(ans, pre_s + x - min(min_s[x - k], min_s[x + k]))
			min_s[x] = min(min_s[x], pre_s)
			pre_s += x
		return ans if ans > -inf else 0

if __name__ == '__main__':
	nums = [1,3,8,9,5]
	k = 4
	print(Solution1().maximumSubarraySum(nums, k))