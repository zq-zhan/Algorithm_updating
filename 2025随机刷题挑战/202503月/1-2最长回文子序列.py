class Solution1:  # 记忆化搜索
	def longestPalindromeSubseq(self, s):
		@cache
		def dfs(i, j):  # s[i]到s[j]的最长回文子序列长度
			if i > j:  # 空串
				return 0
			elif i == j:  # 只有一个字符
				return 1
			elif s[i] == s[j]:
				return dfs(i + 1, j - 1) + 2
			else:
				return max(dfs(i + 1, j), dfs(i, j - 1))
		return dfs(0, len(s) - 1)
class Solution2:  # 递归写法
	def longestPalindromeSubseq(self, s):
		n = len(s)
		f = [[0] * n for _ in range(n)]
		for i in range(n - 1, -1, -1):
			f[i][i] = 1
			for j in range(i + 1, n):
				if s[i] == s[j]:
					f[i][j] = f[i + 1][j - 1] + 2
				else:
					f[i][j] = max(f[i + 1][j], f[i][j - 1])
		return f[0][n - 1]
	
if __name__ == '__main__':
	s = "bbbab"
	print(Solution2().longestPalindromeSubseq(s))