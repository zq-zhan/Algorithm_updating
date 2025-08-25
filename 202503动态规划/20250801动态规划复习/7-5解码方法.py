from functools import cache

class Solution:
	def numDecodings(self, s):
		if s.startswith('0'):
			return 0
		@cache
		def dfs(i):
			if i < 0:
				return 0
			res = 0
			for j in range(i + 1):
				if s[j] != '0' and int(s[j:i + 1]) < 27:
					res = max(res, dfs(j - 1) + 1)
			return res
		return dfs(len(s) - 1)
	
if __name__ == '__main__':
	s = "27"
	print(Solution().numDecodings(s))