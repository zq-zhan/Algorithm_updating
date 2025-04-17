from functools import cache
from bisect import bisect_left

## 灵神题解
class Solution1:
	def lengthOfLIS(self, nums):
		@cache
		def dfs(i):
			ans = 0
			for j in range(i):
				if nums[j] < nums[i]:
					ans = max(ans, dfs(j))
			return ans + 1
		return max(dfs(i) for i in range(len(nums)))


## 枚举选哪个
class Solution2:
	def lengthOfLIS(self, nums):
		@cache
		def dfs(i):
			ans = max((dfs(j) for j in range(i) if nums[j] < nums[i]), default=0)
			return ans + 1  # 1表示选入的nums[i]
		return max(dfs(i) for i in range(len(nums)))

## 二分+贪心
class Solution3:
	def lengthOfLIS(self, nums):
		ans = []
		for x in nums:
			j = bisect_left(ans, x)
			if j == len(ans):
				ans.append(x)
			else:
				ans[j] = x
		return len(ans)  # 如果必须以nums中最后一个元素为终点，则为j+1
'''
len(ans)是整个数组nums中最长递增子序列的长度，
而j + 1是在遍历时，以nums[i]为终点的最长递增子序列的长度
'''

## 用LCS求LIS  —— 超时
class Solution4:
	def lengthOfLIS(self, nums):
		nums2 = sorted(set(nums))
		@cache
		def dfs(i, j):
			if i < 0 or j < 0:
				return 0
			if nums[i] == nums2[j]:
				return dfs(i - 1, j - 1) + 1
			return max(dfs(i - 1, j), dfs(i, j - 1))
		return dfs(len(nums) - 1, len(nums2) - 1)
	
if __name__ == '__main__':
	nums = [10,9,2,5,3,7,101,18]
	print(Solution3().lengthOfLIS(nums)) # Output: 4