class Solution:
	def maxBottlesDrunk(self, numBottles, numExchange):
		ans = numBottles
		while numBottles >= numExchange:
			numBottles -= numExchange
			numExchange += 1
			ans += 1
		return ans
	
if __name__ == '__main__':
	numBottles = 9
	numExchange = 3
	print(Solution().maxBottlesDrunk(numBottles, numExchange))