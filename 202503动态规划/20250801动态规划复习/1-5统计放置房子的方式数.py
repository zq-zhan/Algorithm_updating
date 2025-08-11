from functools import cache

class Solution:
	def countHousePlacements(self, n):
		mod = 10 ** 9 + 7
		# @cache
		def dfs(i):
			if i < 0:
				return 1
			return dfs(i - 1) + dfs(i - 2)
		ans = dfs(n - 1)
		return ans ** 2 % mod
	
if __name__ == '__main__':
	n = 1
	print(Solution().countHousePlacements(n))