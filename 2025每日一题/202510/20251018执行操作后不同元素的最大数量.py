from math import inf

class Solution:
	def maxDistinctElements(self, nums, k):
		nums.sort()
		ans = 0
		pre = -inf
		for x in nums:
			temp = max(x - k, pre + 1)
			if temp <= x + k:
				ans += 1
				pre = temp
		return ans

	
if __name__ == '__main__':
	nums = [9,10,9]
	k = 0
	print(Solution().maxDistinctElements(nums, k))