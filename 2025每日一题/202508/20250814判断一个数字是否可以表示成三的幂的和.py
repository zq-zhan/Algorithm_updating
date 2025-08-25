from functools import cache

class Solution:
	def checkPowersOfThree(self, n):
		@cache
		def dfs(i, path):
			if path < 0 or i > n:
				return False
			elif path == 0:
				return True
			return dfs(i + 1, path - 3 ** i) or dfs(i + 1, path)
		ans = dfs(0, n)
		dfs.cache_clear()
		return ans
	
if __name__ == '__main__':
	n = 91
	print(Solution().checkPowersOfThree(n))