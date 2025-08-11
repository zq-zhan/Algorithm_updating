class Solution:
	def numOfUnplacedFruits(self, fruits, baskets):
		n = len(fruits)
		ans = 0
		for x in fruits:
			for i, y in enumerate(baskets):
				if x <= y:
					baskets[i] = 0
					break
			ans += 1 if x > y else 0
		return ans
		
	
if __name__ == '__main__':
	fruits = [3,6,1]
	baskets = [6,4,7]
	print(Solution().numOfUnplacedFruits(fruits, baskets))