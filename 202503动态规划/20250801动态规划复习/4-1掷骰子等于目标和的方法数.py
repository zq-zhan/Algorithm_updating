from functools import cache

class Solution:  # 每组恰好选1个
	def numRollsToTarget(self, n, k, target):
		MOD = 10 ** 9 + 7
		@cache
		def dfs(i, path):
			# if i > 0 and path <= 0:
			# 	return 0
			if i == 0:
				return int(path == 0)
			res = 0
			for x in range(1, k + 1):
				if path < x:
					break
				res = (res + dfs(i - 1, path - x)) % MOD
			return res
		return dfs(n, target)
	
if __name__ == '__main__':
	n = 2
	k = 6
	target = 6
	print(Solution().numRollsToTarget(n, k, target))