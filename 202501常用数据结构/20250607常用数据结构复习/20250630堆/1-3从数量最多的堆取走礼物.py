from math import isqrt
import heapq

class Solution:
	def pickGifts(self, gifts, k):
		gifts = [-x for x in gifts]
		heapq.heapify(gifts)
		for _ in range(k):
			mn = heapq.heappop(gifts)
			heapq.heappush(gifts, -isqrt(-mn))
		return -sum(gifts)
	
if __name__ == '__main__':
	gifts = [25,64,9,4,100]
	print(Solution().pickGifts(gifts, 4))