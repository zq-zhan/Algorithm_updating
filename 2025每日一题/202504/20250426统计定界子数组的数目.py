from collections import defaultdict
from math import inf

class Solution1:  # 暴力解法
	def countSubarrays(self, nums, minK, maxK):
		ans = 0
		n = len(nums)
		for left in range(n):
			mn = inf
			mx = 0
			for right in range(left, n):
				mn = min(nums[right], mn)
				mx = max(nums[right], mx)
				if mn == minK and mx == maxK:
					ans += 1
		return ans
## 
class Solution2:
	def countSubarrays(self, nums, minK, maxK):
		ans = 0
		minI = maxI = i0 = -1
		for right, c in enumerate(nums):
			if c == minK:
				minI = right
			if c == maxK:
				maxI = right
			if not minK <= c <= maxK:
				i0 = right
			ans += max(min(minI, maxI) - i0, 0)
		return ans
	
if __name__ == '__main__':
	nums = [1,3,5,2,7,5]
	minK = 1
	maxK = 5
	print(Solution2().countSubarrays(nums, minK, maxK))