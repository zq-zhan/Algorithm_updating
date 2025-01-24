# 3.检查是否区域内所有整数都被覆盖
from itertools import accumulate

class Solution1:
	def isCovered(self, ranges, left, right):
		max_num = max(end for _, end in ranges)
		d = [0] * (max_num + 2)
		for start, end in ranges:
			d[start] += 1
			d[end + 1] -= 1

		a = list(accumulate(d))
		# return all(x > 0 for x in a[left:right + 1])
		return right - left + 1 == sum(x > 0 for x in a[left:right + 1])
	
class Solution2:
	def isCovered(self, ranges, left, right):
		# max_num = max(end for _, end in ranges)
		d = [0] * (50 + 2)
		for start, end in ranges:
			d[start] += 1
			d[end + 1] -= 1

		a = list(accumulate(d))
		return all(x > 0 for x in a[left:right + 1])
		# return right - left + 1 == sum(x > 0 for x in a[left:right + 1])
        
	
if __name__ == '__main__':
	s = Solution2()
	ranges = [[1, 1]]
	left = 50
	right = 50
	print(s.isCovered(ranges, left, right))