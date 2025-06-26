class Solution:
	def maxProfit(self, prices):
		buy = max(prices)
		sold = 0
		ans = 0
		for x in prices:
			if x < buy:
				buy = x
				sold = 0
				continue
			sold = max(sold, x)
			ans = max(sold - buy, ans)
		return ans
	
class Solution:
	def maxProfit(self, prices):
		buy = max(prices)
		ans = 0
		for sold in prices:
			ans = max(ans, sold - buy)
			buy = min(buy, sold)
		return ans

	
if __name__ == '__main__':
	prices = [3,2,6,5,0,3]
	print(Solution().maxProfit(prices))