from math import inf
from functools import cache

class Solution:
	def maximumProfit(self, prices, k):
		n = len(prices)
		@cache
		def dfs(i, k, tag):
			if k < 0:
				return -inf
			if i == n:
				# return 0
				return -inf if tag else 0

			if tag == 0:
				return max(dfs(i + 1, k - 1, 1) - prices[i], dfs(i + 1, k, 0), dfs(i + 1, k - 1, 2) + prices[i])
			elif tag == 1:
				return max(dfs(i + 1, k, 1), dfs(i + 1, k - 1, 0) + prices[i])
			elif tag == 2:
				return max(dfs(i + 1, k, 2), dfs(i + 1, k - 1, 0) - prices[i])
		ans = dfs(0, k * 2, 0)
		dfs.cache_clear()
		return ans

class Solution:
	def maximumProfit(self, prices, k):
		n = len(prices)
		@cache
		def dfs(i, k, tag):
			if k < 0:
				return -inf
			if i == n:
				# return 0
				return -inf if tag else 0

			if tag == 0:
				return max(dfs(i + 1, k, 1) - prices[i], dfs(i + 1, k, 0), dfs(i + 1, k, 2) + prices[i])
			elif tag == 1:
				return max(dfs(i + 1, k, 1), dfs(i + 1, k - 1, 0) + prices[i])
			elif tag == 2:
				return max(dfs(i + 1, k, 2), dfs(i + 1, k - 1, 0) - prices[i])
		ans = dfs(0, k, 0)
		dfs.cache_clear()
		return ans

class Solution:
	def maximumProfit(self, prices, k):
		n = len(prices)
		@cache
		def dfs(i, j, tag):
			if j < 0:
				return -inf
			if i < 0:
				return -inf if tag else 0
			p = prices[i]
			if tag == 0:
				return max(dfs(i - 1, j, 0), dfs(i - 1, j, 1) + p, dfs(i - 1, j, 2) - p)
			elif tag == 1: # 做空交易
				return max(dfs(i - 1, j, 1), dfs(i - 1, j - 1, 0) - p)
			else: # 普通交易
				return max(dfs(i - 1, j, 2), dfs(i - 1, j - 1, 0) + p)
		ans = dfs(n - 1, k, 0)
		dfs.cache_clear()
		return ans

if __name__ == '__main__':
	prices = [1,7,9,8,2]
	k = 2
	print(Solution().maximumProfit(prices, k))