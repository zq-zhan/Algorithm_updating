from functools import cache

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

if __name__ == '__main__':
	text1 = "abcde"
	text2 = "ace"
	print(Solution1().longestCommonSubsequence(text1, text2))