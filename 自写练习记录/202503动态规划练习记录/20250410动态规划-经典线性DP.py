# 1.最长公共子序列
## 灵神题解
class Solution1:
	def longestCommonSubsequence(self, text1, text2):
		n, m = len(text1), len(text2)
		@cache
		def dfs(i, j):
			if i < 0 or j < 0:
				return 0
			if text1[i] == text2[j]:
				return dfs(i - 1, j - 1) + 1
			return max(dfs(i - 1, j), dfs(i, j - 1))
		return dfs(n - 1, m - 1)
## 递推写法
class Solution2:
	def longestCommonSubsequence(self, text1, text2):
		n, m = len(text1), len(text2)
		f = [[0] * (m + 1) for _ in range(n + 1)]
		for i, x in enumerate(text1):
			for j, y in enumerate(text2):
				f[i + 1][j + 1] = f[i][j] + 1 if x == y else max(f[i][j + 1], f[i + 1][j])
		return f[-1][-1]

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

# 3.两个字符串的最小ascii删除和
class Solution1:
	def minimumDeleteSum(self, s1, s2):
		@cache
		def dfs(i, j):
			if i < 0:
				res = 0
				for x in s2[:j]:
					res += ord(x)
				return res
			if j < 0:
				res = 0
				for x in s1[:j]:
					res += ord(x)
				return res
			if s1[i] == s2[j]:
				return dfs(i - 1, j - 1)
			return min(dfs(i - 1, j) + ord(s1[i]), dfs(i, j - 1) + ord(s2[j]))
		return dfs(len(s1) - 1, len(s2) - 1)
## 解法二
class Solution2:
	def minimumDeleteSum(self, s1, s2):
		s = list(map(ord, s1))
		t = list(map(ord, s2))
		@cache
		def dfs(i, j):
			if i < 0:
				return sum(t[:j + 1])
			if j < 0:
				return sum(s[:i + 1])
			if s[i] == t[j]:
				return dfs(i - 1, j - 1)
			return min(dfs(i - 1, j) + s[i], dfs(i, j - 1) + t[j])
		return dfs(len(s1) - 1, len(s2) - 1)



