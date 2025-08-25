from functools import cache

class Solution:
	def numOfSubsequences(self, s):
		t = "LCT"
		@cache
		def dfs(i, j, tag):
			if j < 0:
				return 1
			if i < 0:
				return 0
			res = 0
			if s[i] == t[j]:
				res += dfs(i - 1, j - 1, tag)
			if tag:
				res = max(res, dfs(i, j - 1, False))
			res = max(res, dfs(i - 1, j, tag))
			return res  
		return dfs(len(s) - 1, 2, True)

if __name__ == '__main__':
	s = "LMCT"
	print(Solution().numOfSubsequences(s))