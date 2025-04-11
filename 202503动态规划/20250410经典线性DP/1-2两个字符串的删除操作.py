from functools import cache

# 2.两个字符串的删除操作
class Solution1:
	def minDistance(self, word1, word2):
		@cache
		def dfs(i, j):
			if i < 0 or j < 0:
				return i + j + 2
			if word1[i] == word2[j]:
				return dfs(i - 1, j - 1)
			return min(dfs(i - 1, j) + 1, dfs(i, j - 1) + 1)
		return dfs(len(word1) - 1, len(word2) - 1)

if __name__ == '__main__':
	word1 = "leetcode"
	word2 = "etco"
	print(Solution1().minDistance(word1, word2))