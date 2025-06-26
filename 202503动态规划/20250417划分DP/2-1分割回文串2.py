from functools import cache
from math import inf

#################### 最优划分 ###############
# 1.分割回文串2
class Solution1:
	def minCut(self, s):
		n = len(s)
		def dfs(i):
			if i <= 0:
				return 0
			res = 0
			for j in range(i + 1, n):
				if s[j:n] != s[j:n][::-1]:
					res += dfs()
			return 
## 灵神题解
class Solution2:
	def minCut(self, s):
		@cache
		def is_palindrome(l, r):
			if l >= r:
				return True
			return s[l] == s[r] and is_palindrome(l + 1, r - 1)
		@cache
		def dfs(r):
			if is_palindrome(0, r):
				return 0
			res = inf
			for l in range(1, r + 1):  # 枚举分割位置
				if is_palindrome(l, r):
					res = min(res, dfs(l - 1) + 1)
			return res
		return dfs(len(s) - 1)
	
if __name__ == '__main__':
	s = "aab"
	print(Solution2().minCut(s))