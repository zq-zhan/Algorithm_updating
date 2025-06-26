# 20250114——超过阈值的最少操作次数
class Solution1:  # 复杂度：nlogn
	def minOperations(self, nums, k):
		nums.sort()
		ans = 0
		for x in nums:
			if x < k:
				ans += 1
			else:
				break
		return ans
## 灵神题解:复杂度：n
class Solution2:
	def minOperations(self, nums, k):
		return sum(x < k for x in nums)