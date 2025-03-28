# 3.完全平方数
from functools import cache
from math import inf
from math import isqrt

class Solution1:
	def numSquares(self, n):
		nums = [x for x in range(1, n + 1)]
		@cache
		def dfs(i, c):
			if i < 0:
				return 0 if c == 0 else inf
			if c < nums[i] ** 2:
				return dfs(i - 1, c)
			return min(dfs(i - 1, c), dfs(i, c - nums[i] ** 2) + 1)
		return dfs(n - 1, n)
## 内存优化
@cache
def dfs(i, c):
	if i == 0:
		return 0 if c == 0 else inf
	if c < i * i:
		return dfs(i - 1, c)
	return min(dfs(i - 1, c), dfs(i, c - i * i) + 1)
		
class Solution2:
	def numSquares(self, n):
		# nums = [x for x in range(1, n + 1)]
		return dfs(isqrt(n), n)

	
if __name__ == '__main__':
	n = 12
	s = Solution2()
	print(s.numSquares(n))