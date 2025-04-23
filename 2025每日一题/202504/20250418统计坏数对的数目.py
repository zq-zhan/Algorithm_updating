from collections import defaultdict
from math import comb

# 20250418统计坏数对的数目
class Solution1:  # 超出时间复杂度
	def countBadPairs(self, nums):
		ans = 0
		n = len(nums)
		for i in range(n - 1):
			for j in range(i + 1, n):
				if j - i != nums[j] - nums[i]:
					ans += 1
		return ans
## 灵神题解
class Solution2:
	def countBadPairs(self, nums):
		ans = comb(len(nums), 2)
		cnt = defaultdict(int)
		for i, c in enumerate(nums):
			ans -= cnt[c - i]
			cnt[c - i] += 1
		return ans

if __name__ == '__main__':
	nums = [4,1,3,3]
	print(Solution2().countBadPairs(nums))