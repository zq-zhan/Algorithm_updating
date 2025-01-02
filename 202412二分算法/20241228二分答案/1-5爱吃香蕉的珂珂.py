# 5.爱吃香蕉的珂珂
class Solution1:
	def minEatingSpeed(self, piles, h):
		left, right = 0, max(piles)
		while left + 1 < right:
			mid = (left + right) // 2
			if sum((x - 1) // mid for x in piles) <= h - len(piles):
				right = mid
			else:
				left = mid
		return right