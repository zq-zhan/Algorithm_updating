from math import gcd
from collections import defaultdict

class Solution:
	def countBeautifulPairs(self, nums):
		ans = 0
		dic_win = defaultdict(int)
		for j, x in enumerate(nums):
			for i in range(1, 10):
				if gcd(i, x % 10) == 1:
					ans += dic_win[i]
			while x >= 10:
				x //= 10
			dic_win[x] += 1
		return ans

	
if __name__ == '__main__':
	nums = [31,25,72,79,74]
	print(Solution().countBeautifulPairs(nums))