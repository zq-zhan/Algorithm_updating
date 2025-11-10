from functools import cache
from math import inf

class Solution:
	def minimumTotal(self, triangle):
		n = len(triangle)
		@cache
		def dfs(i, j):
			if i == n:
				return 0
			if j > i:
				return inf
			return min(dfs(i + 1, j), dfs(i + 1, j + 1)) + triangle[i][j]
		return dfs(0, 0)
	
if __name__ == '__main__':
	triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
	s = Solution()
	print(s.minimumTotal(triangle))