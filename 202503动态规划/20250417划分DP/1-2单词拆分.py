from functools import cache

# 2.单词拆分
class Solution1:
	def wordBreak(self, s, wordDict):
		wordlen = set(map(len, wordDict))
		@cache
		def dfs(i):
			if i < 0:
				return True
			if i < min(wordlen) - 1:
				return False
			res = False
			for length in wordlen:
				if i >= length - 1 and s[i - length + 1:i + 1] in wordDict:
					res |= dfs(i - length)
			return res
		return dfs(len(s) - 1)
	
if __name__ == '__main__':
	s = "leetcode"
	wordDict = ["leet", "code"]
	print(Solution1().wordBreak(s, wordDict))
    