# 3.可互换矩形的组数
from collections import defaultdict


class Solution1:
	def interchangeableRectangles(self, rectangles):
		ans = 0
		idx = defaultdict(int)
		for j, rectangle in enumerate(rectangles):
			bili = rectangle[0] / rectangle[1]
			if bili in idx:
				# ans += idx[bili]
				ans += idx[bili]
			idx[bili] += 1
		return ans
	
if __name__ == '__main__':
	rectangles = [[1,7],[2,8],[8,8],[2,5],[2,8],[7,4]]
	print(Solution1().interchangeableRectangles(rectangles)) # Output: 3