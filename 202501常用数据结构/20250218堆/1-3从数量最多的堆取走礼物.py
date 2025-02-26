# 3.从数量最多的堆取走礼物
import heapq
from math import sqrt

class Solution1:
	def pickGifts(self, gifts, k):
		gifts = [-x for x in gifts]
		heapq.heapify(gifts)
		# ans = sum(gifts)
		for i in range(k):
			push_gift = heapq.heappop(gifts)
			heapq.heappush(gifts, -int(sqrt(-push_gift)))
		return sum(-x for x in gifts)

if __name__ == '__main__':
	gifts = [25,64,9,4,100]
	k = 4
	print(Solution1().pickGifts(gifts, k))