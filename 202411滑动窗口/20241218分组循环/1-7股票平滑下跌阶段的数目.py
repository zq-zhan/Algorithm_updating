# 7.股票平滑下跌阶段的数目
class Solution1:
	def getDescentPeriods(self,prices):
		ans = 0
		left, right = 0, 1
		while right < len(prices):
			if prices[right - 1] - prices[right] != 1:
				ans += (right - left) * (right - left + 1) // 2
				left = right
			right += 1
		ans += (right - left) * (right - left + 1) // 2
		return ans

	
if __name__ == '__main__':
	# prices = [3,2,1,4]
	prices = [1]
	cls = Solution1()
	print(cls.getDescentPeriods(prices))