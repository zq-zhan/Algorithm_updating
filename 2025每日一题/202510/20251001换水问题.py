# 20251001换水问题
class Solution:
	def numWaterBottles(self, numBottles, numExchange):
		ans = numBottles
		while numBottles >= numExchange:
			ans += numBottles // numExchange
			numBottles = numBottles // numExchange + numBottles % numExchange
		return ans
	
if __name__ == '__main__':
	numBottles = 12
	numExchange = 4
	print(Solution().numWaterBottles(numBottles, numExchange)) # Output: 13