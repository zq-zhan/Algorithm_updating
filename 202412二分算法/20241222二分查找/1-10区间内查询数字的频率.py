# 10.区间内查询数字的频率
## 灵神思路
from bisect import bisect_left, bisect_right
from collections import defaultdict


class RangeFreqQuery:
	def __init__(self,arr):
		pos = defaultdict(list)
		for i, x in enumerate(arr):
			pos[x].append(i)  # 保存目标值的下标
		self.pos = pos
	def query(self,left,right,value):
		a = self.pos[value]
		left_bound = bisect_left(a, left)
		right_bound = bisect_left(a, right + 1)
		return right_bound - left_bound
	
if __name__ == '__main__':
	arr = [12,33,4,56,22,2,34,33,22,12,34,56]
	obj = RangeFreqQuery(arr)
	print(obj.query(1,2,4)) 
	print(obj.query(0,11,33)) 