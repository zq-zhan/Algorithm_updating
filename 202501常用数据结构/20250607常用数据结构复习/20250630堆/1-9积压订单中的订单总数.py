import heapq

class Solution:
	def getNumberOfBacklogOrders(self, orders):
		mod = 10 ** 9 + 7
		buy_lis = []
		sell_lis = []
		for price, amount, orderType in orders:
			if orderType == 0:  # 采购订单
				while sell_lis and amount and sell_lis[0][0] <= price:
					if sell_lis[0][1] <= amount:
						amount -= sell_lis[0][1]
						heapq.heappop(sell_lis)
					else:
						sell_lis[0][1] -= amount
						amount = 0
				if amount > 0:
					heapq.heappush(buy_lis, [-price, amount])
			else:
				while buy_lis and amount and -buy_lis[0][0] >= price:
					if buy_lis[0][1] <= amount:
						amount -= buy_lis[0][1]
						heapq.heappop(buy_lis)
					else:
						buy_lis[0][1] -= amount
						amount = 0
				if amount > 0:
					heapq.heappush(sell_lis, [price, amount])
		ans = 0
		for _, amount in buy_lis:
			ans += amount
		for _, amount in sell_lis:
			ans += amount
		return ans % mod
	
if __name__ == '__main__':
	orders = [[7,1000000000,1],[15,3,0],[5,999999995,0],[5,1,1]]
	s = Solution()
	print(s.getNumberOfBacklogOrders(orders))