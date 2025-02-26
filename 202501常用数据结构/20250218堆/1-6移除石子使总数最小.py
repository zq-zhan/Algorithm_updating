# 6.移除石子使总数最小
import heapq

class Solution1:
	def minStoneSum(self, piles, k):
		piles = [-x for x in piles]
		heapq.heapify(piles)
		for _ in range(k):
			heapq.heapreplace(piles, piles[0] + (-piles[0]) // 2)
		return -sum(piles)
	
if __name__ == '__main__':
	piles = [5, 4, 9]
	k = 2
	print(Solution1().minStoneSum(piles, k)) # Output: 12