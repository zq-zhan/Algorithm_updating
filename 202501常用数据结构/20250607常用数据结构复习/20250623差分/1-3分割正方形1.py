
from collections import defaultdict
# from itertools import pairwise

from itertools import tee

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

## 浮点二分
class Solution:
	def separateSquares(self, squares):
		M = 100000
		total_area = sum(l * l for _, _, l in squares)

		def check(y):
			area = 0
			for _, yi, l in squares:
				if yi < y:
					area += l * min(y - yi, l)
			return area >= total_area / 2

		left = 0
		right = max_y = max(y + l for _, y, l in squares)
		for _ in range((max_y * M).bit_length()):  # n.bit_length() == floor(log2(n)) + 1（当 n > 0）
			mid = (left + right) / 2
			if check(mid):
				right = mid
			else:
				left = mid
		return (left + right) / 2
## 差分
class Solution:
    def separateSquares(self, separateSquares):
        tot_area = 0
        diff = defaultdict(int)
        for _, y, l in squares:
            tot_area += l * l
            diff[y] += l
            diff[y + l] -= l

        area = sum_l = 0
        for y, y2 in pairwise(sorted(diff)):
            sum_l += diff[y]  # 矩形底边长度之和
            area += sum_l * (y2 - y)  # 底边长 * 高 = 新增面积
            if area * 2 >= tot_area:
                return y2 - (area * 2 - tot_area) / (sum_l * 2)

if __name__ == '__main__':
	squares = [[0,0,2],[1,1,1]]
	print(Solution().separateSquares(squares))