# 一维差分（扫描线）
from itertools import accumulate
from collections import Counter

# 1.拼车
## 灵神题解1:复杂度O(n+U)，U为trips长度
class Solution1:
	def carPooling(self, trips, capacity):
		d = [0] * 1001
		for num, from_, to in trips:
			d[from_] += num
			d[to] -= num
		return all(s <= capacity for s in accumulate(d))
## 灵神题解2:哈希表+差分
class Solution2:
	def carPooling(self, trips, capacity):
		d = Counter()
		for num, from_, to in trips:
			d[from_] += num
			d[to] -= num

		s = 0
		for k in sorted(d):
			s += d[k]
			if s > capacity:
				return False
		return True

if __name__ == '__main__':
	capacity = 4
	trips = [[2,0,5],[3,3,7]]
	cls = Solution2()
	print(cls.carPooling(trips, capacity)) # True