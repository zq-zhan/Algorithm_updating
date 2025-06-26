from collections import defaultdict

class Solution:
	def countBadPairs(self, nums):
		# nums = [(val, i) for i, val in enumerate(nums)]
		ans = 0
		for i, x in enumerate(nums):
			for j in range(i + 1, len(nums)):
				if j - i != nums[j] - x:
					ans += 1
		return ans
## 解法2
class Solution:
	def countBadPairs(self, nums):
		dic_win = defaultdict(int)
		ans = 0
		n = len(nums)
		for i, x in enumerate(nums):
			if dic_win[x - i]:
				ans += dic_win[x - i]
			dic_win[x - i] += 1
		return n * (n - 1) // 2 - ans
	
if __name__ == '__main__':
	nums = [4,1,3,3]
	print(Solution().countBadPairs(nums))