from functools import cache
from math import inf

class Solution:
	def minimumBeautifulSubstrings(self, s):
		@cache
		def check(x):
			for i in range(x + 1):
				if 5 ** i == x:
					return True
				elif 5 ** i > x:
					break
			return False
		@cache
		def dfs(i):
			if i < 0:
				return 0
			res = inf
			for j in range(i + 1):
				x = int(s[j:i + 1], 2)
				if s[j] and check(x):
					res = min(res, dfs(j - 1) + 1)
			return res
		ans = dfs(len(s) - 1)
		return ans if ans < inf else -1
	
if __name__ == '__main__':
	s = "1011"
	print(Solution().minimumBeautifulSubstrings(s))