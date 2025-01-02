# 13.基于时间的键值存储
from collections import defaultdict
from bisect import bisect_right

class TimeMap:

	def __init__(self):
		pos = defaultdict(list)
		self.pos = pos
		# self.pos = defaultdict(list)


	def set(self, key: str, value: str, timestamp: int) -> None:
		pos = self.pos
		pos[key].append([timestamp,value])
		# self.pos[key].append([timestamp,value])

	def get(self, key: str, timestamp: int) -> str:
		arr = self.pos[key]
		if not arr or arr[0][0] > timestamp:
			return ''
		if arr[-1][0] <= timestamp:
			return arr[-1][1]
		nums = []
		for x in arr:
			nums.append(x[0])
		find = bisect_right(nums, timestamp) - 1
		if find == -1:
			return ''
		else:
			return arr[find][1]
		
if __name__ == '__main__':
	timeMap = TimeMap()
	timeMap.set("foo", "bar", 1)
	timeMap.set("foo", "baz", 2)
	timeMap.set("foo", "qux", 3)
	print(timeMap.get("foo", 1)) # Output: "bar"
	print(timeMap.get("foo", 4)) # Output: "baz"
	print(timeMap.get("foo", 5)) # Output: "qux"