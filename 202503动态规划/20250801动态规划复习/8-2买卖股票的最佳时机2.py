from functools import cache

class Solution:
	def maxProfit(self, prices):
		n = len(prices)
		@cache
		def dfs(i, x):
			if i > n - 1:
				return 0
			if x != -1:
				return max(dfs(i, -1) + prices[i] - x, dfs(i + 1, x))
			return max(dfs(i + 1, prices[i]), dfs(i + 1, -1))
		return dfs(0, -1)

	
if __name__ == '__main__':
	prices = [2,1,2,0,1]
	print(Solution().maxProfit(prices))