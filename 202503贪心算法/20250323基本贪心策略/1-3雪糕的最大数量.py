# 3.雪糕的最大数量
class Solution1:
	def maxIceCream(self, costs, coins):
		costs.sort()
		for i, c in enumerate(costs, 1):
			coins -= c
			if coins == 0:
				return i
			elif coins < 0:
				return i - 1
		return i