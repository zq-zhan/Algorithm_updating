# 4.和可被k整除的子数组数目
from collections import defaultdict

## 思路：前缀和的差值可以被k整除—— 不同前缀和对k取模结果相等
class Solution1:
	def subarraysDivByK(self, nums, k):
		pre_sum = [0] * (len(nums) + 1)
		for i, c in enumerate(nums):
			pre_sum[i + 1] = pre_sum[i] + c

		ans = 0
		cnt = defaultdict(int)
		for sj in pre_sum:
			ans += cnt[sj % k]
			cnt[sj % k] += 1
		return ans
	
if __name__ == '__main__':
	nums = [4, 5, 0, -2, -3, 1]
	k = 5
	print(Solution1().subarraysDivByK(nums, k)) # Output: 7