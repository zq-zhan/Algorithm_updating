from functools import cache
from math import inf

# 6.一和零
class Solution1:
	def findMaxForm(self, strs, m, n):
		cnt_0 = [s.count('0') for s in strs]
		@cache
		def dfs(i, m, n):
			if i < 0:
				return 0 if m >= 0 and n >= 0 else -inf
			x = cnt_0[i]
			y = len(strs[i]) - x
			return max(dfs(i - 1, m - x, n - y) + 1, dfs(i - 1, m, n))
		return dfs(len(strs) - 1, m, n)

class Solution2: 
	def findMaxForm(self, strs, m, n):
		cnt_0 = [s.count('0') for s in strs]
		@cache
		def dfs(i, m, n):
			if i < 0:
				return 0
			x = cnt_0[i]
			y = len(strs[i]) - x
			if m >= x and n >= y:
				return max(dfs(i - 1, m - x, n - y) + 1, dfs(i - 1, m, n))
			else:
				return dfs(i - 1, m, n)
		return dfs(len(strs) - 1, m, n)
	
if __name__ == '__main__':
	strs = ["10", "0001", "111001", "1", "0"]
	m = 5
	n = 3
	s = Solution2()
	print(s.findMaxForm(strs, m, n))