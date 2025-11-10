from itertools import accumulate
from collections import defaultdict

class Solution:
	def maxFrequency(self, nums, k, numOperations):
		mn, mx = min(nums), max(nums)
		n = mx - mn + 1
		m = 2 * k
		new_lis = [0] * n
		for x in nums:
			new_lis[x - mn] += 1
		pre_s = list(accumulate(new_lis))
		pre_s = [0] * k + pre_s + [pre_s[-1]] * k
		ans = max(new_lis)
		for mid in range(k, n + k):
			cnt = min(pre_s[mid + k] - pre_s[mid - k], numOperations)
			ans = max(cnt, ans)
		return ans

## 灵神题解
class Solution:
	def maxFrequency(self, nums, k, numOperations):
		cnt = defaultdict(int)
		diff = defaultdict(int)
		for x in nums:
			cnt[x] += 1
			diff[x]
			diff[x - k] += 1
			diff[x + k + 1] -= 1

		ans = sum_d = 0
		for x, d in sorted(diff.items()):
			sum_d += d
			ans = max(ans, min(sum_d, cnt[x] + numOperations))
		return ans


if __name__ == '__main__':
	nums = [23,54]
	k = 77
	numOperations = 1
	print(Solution().maxFrequency(nums, k, numOperations))