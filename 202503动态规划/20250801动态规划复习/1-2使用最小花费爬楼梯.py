from functools import cache

class Solution:
	def minCostClimbingStairs(self, cost):
		n = len(cost)
		# @cache
		def dfs(i):
			if i >= n:
				return 0
			return min(dfs(i + 1), dfs(i + 2)) + cost[i]
		return min(dfs(0), dfs(1))
	
if __name__ == '__main__':
	cost = [10, 15, 20]
	print(Solution().minCostClimbingStairs(cost))