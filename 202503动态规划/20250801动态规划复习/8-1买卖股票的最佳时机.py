from math import inf

class Solution:
	def maxProfit(self, prices):
		n = len(prices)
		suf_mx = [0] * (n + 1)
		for i in range(n - 1, -1, -1):
			suf_mx[i] = max(prices[i], suf_mx[i + 1])
		pre_min = inf
		ans  = 0
		for i, x in enumerate(prices):
			ans = max(ans, suf_mx[i] - pre_min)
			pre_min = min(pre_min, x)
		return ans
	
if __name__ == '__main__':
	prices = [7,1,5,3,6,4]
	print(Solution().maxProfit(prices))
