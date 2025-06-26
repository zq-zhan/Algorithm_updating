from collections import defaultdict

class Solution:
	def countNicePairs(self, nums):
		mod = 10 ** 9 + 7
		def rev(x):
			x = str(x)[::-1]
			return int(x)
		ans = 0
		dic_win = defaultdict(int)
		for x in nums:
			rev_x = rev(x)
			ans += dic_win[x - rev_x]
			dic_win[x - rev_x] += 1
		return ans % mod
	
if __name__ == '__main__':
	nums = [42,11,1,97]
	print(Solution().countNicePairs(nums))