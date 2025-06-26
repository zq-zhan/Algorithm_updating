from functools import cache

class Solution1:
	def minimumDeleteSum(self, s1, s2):
		@cache
		def dfs(i, j):
			if i < 0:
				res = 0
				for x in s2[:j + 1]:
					res += ord(x)
				return res
			if j < 0:
				res = 0
				for x in s1[:i + 1]:
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



if __name__ == '__main__':
	s1 = "sea"
	s2 = "eat"
	print(Solution2().minimumDeleteSum(s1, s2))