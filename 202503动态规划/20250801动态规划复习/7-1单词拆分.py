from functools import cache

class Solution:
	def wordBreak(self, s, wordDict):
		wordDict = set(wordDict)
		wordLen = set(list(map(len, wordDict)))
		@cache
		def dfs(i):
			if i < 0:
				return True
			elif i == 0:
				return s[0] in wordDict
			res = False
			for length in wordLen:
				res |= dfs(i - length) and s[i - length + 1:i + 1] in wordDict
			return res
		return dfs(len(s) - 1)
	
if __name__ == '__main__':
	s = "a"
	wordDict = ["a"]
	print(Solution().wordBreak(s, wordDict))