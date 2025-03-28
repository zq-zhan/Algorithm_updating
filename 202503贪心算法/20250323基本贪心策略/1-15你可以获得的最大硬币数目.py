# 15.你可以获得的最大硬币数目
class Solution1:
	def maxCoins(self, piles):
		ans = 0
		piles.sort(reverse = True)
		while len(piles) > 0:
			piles.pop(0)
			ans += piles.pop(0)
			piles.pop(-1)
		return ans
	
if __name__ == '__main__':
	piles = [2,4,1,2,7,8]
	s = Solution1()
	print(s.maxCoins(piles))