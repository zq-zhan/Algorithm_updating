# 11.将区间分为最小组数
from itertools import accumulate


class Solution1:
	def minGroups(self, intervals):
		max_num = max(end for _, end in intervals)
		d = [0] * (max_num + 2)
		for start, end in intervals:
			d[start] += 1
			d[end + 1] -= 1

		return max(list(accumulate(d)))
	
if __name__ == '__main__':
	intervals = [[5, 10], [6,8], [1,5], [2,3],[1,10]]
	cls = Solution1()
	print(cls.minGroups(intervals))