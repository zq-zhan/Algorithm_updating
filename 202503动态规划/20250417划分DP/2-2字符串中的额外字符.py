from functools import cache
from math import inf

class Solution1:
	def minExtraChar(self, s, dictionary):
		wordlen = set(map(len, dictionary))
		n = len(s)
		@cache
		def dfs(i):
			if i < 0:
				return 0
			# if i < min(wordlen) - 1:
			# 	return i + 1
			ans = dfs(i - 1) + 1
			# for length in wordlen:
			# 	if i > length - 1 and s[i - length + 1:i + 1] in dictionary:
			# 		ans = min(ans, dfs(i - length))
			for j in range(i + 1):  # 枚举左端点
				if s[j:i + 1] in dictionary:
					ans = min(ans, dfs(j - 1))
			return ans
		return dfs(n - 1)

class Solution2:
	def minExtraChar(self, s, dictionary):
		wordlen = set(map(len, dictionary))
		n = len(s)
		@cache
		def dfs(i):
			if i < 0:
				return 0
			if i < min(wordlen) - 1:
				return i + 1
			ans = dfs(i - 1) + 1  # 不选的时候，ans最大
			for length in wordlen:
				if i >= length - 1 and s[i - length + 1:i + 1] in dictionary:
					ans = min(ans, dfs(i - length))
			# for j in range(i + 1):  # 枚举左端点
			# 	if s[j:i + 1] in dictionary:
			# 		ans = min(ans, dfs(j - 1))
			return ans
		return dfs(n - 1)

class Solution3:
	def minExtraChar(self, s, dictionary):
		wordlen = set(map(len, dictionary))
		n = len(s)
		@cache
		def dfs(i):
			if i < 0:
				return 0
			if i < min(wordlen) - 1:
				return i + 1
			ans = inf
			for length in wordlen:
				if i >= length - 1 and s[i - length + 1:i + 1] in dictionary:
					ans = min(ans, dfs(i - length))
			ans = min(ans, dfs(i - 1) + 1)
			return ans
		return dfs(n - 1)

	
if __name__ == '__main__':
	s = 'leetscode'
	dictionary = ['leet', 'code', 'leetcode']
	print(Solution3().minExtraChar(s, dictionary))