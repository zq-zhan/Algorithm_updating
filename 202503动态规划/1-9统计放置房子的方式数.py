from functools import cache

class Solution1:
	def countHousePlacements(self, n):
		mod = (10 ** 9 + 7)
		@cache
		def dfs(i):
			if i < 0:
				return 0
			elif i == 0:
				return 1
			elif i == 1:
				return 2
			return dfs(i - 1) + dfs(i - 2)
		ans = dfs(n) % mod
		return (ans * ans) % mod
	
if __name__ == '__main__':
	n = 2
	print(Solution1().countHousePlacements(n))