from itertools import accumulate
from collections import defaultdict

class Solution:
	def carPooling(self, trips, capacity):
		mx = max(to for _, _, to in trips)
		new_arr = [0] * (mx + 1)
		for num, start, to in trips:
			new_arr[start] += num
			new_arr[to] -= num
		pre_s = list(accumulate(new_arr))
		return max(pre_s) <= capacity

## 排序哈希表解法
class Solution:
	def carPooling(self, trips, capacity):
		dic_win = defaultdict(int)
		for num, start, to in trips:
			dic_win[start] += num
			dic_win[to] -= num

		temp_s = 0
		for _, num in sorted(dic_win.items()):
			temp_s += num
			if temp_s > capacity:
				return False
		return True

if __name__ == '__main__':
	trips = [[2,1,5],[3,3,7]]
	capacity = 4
	print(Solution().carPooling(trips, capacity))