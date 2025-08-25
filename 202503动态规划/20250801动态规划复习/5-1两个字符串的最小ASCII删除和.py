from functools import cache

class Solution:
	def minimumDeleteSum(self, s1, s2):
		n, m = len(s1), len(s2)
		@cache
		def dfs(i, j):
			if i < 0 and j < 0:
				return 0
			elif i < 0:
				return sum(ord(s2[k]) for k in range(j + 1))
			elif j < 0:
				return sum(ord(s1[k]) for k in range(i + 1))
			if s1[i] == s2[j]:
				return dfs(i - 1, j - 1)
			return min(dfs(i - 1, j) + ord(s1[i]), dfs(i, j - 1) + ord(s2[j]))
		return dfs(n - 1, m - 1)
	
if __name__ == '__main__':
	s1 = "sea"
	s2 = "eat"
	print(Solution().minimumDeleteSum(s1, s2))