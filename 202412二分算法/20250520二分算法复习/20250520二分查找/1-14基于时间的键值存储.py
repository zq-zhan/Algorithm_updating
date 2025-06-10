from collections import defaultdict
from bisect import bisect_left

class TimeMap:

	def __init__(self):
		self.dic_win = defaultdict(list)


	def set(self, key, value, timestamp) -> None:
		self.dic_win[key].append((timestamp, value))


	def get(self, key, timestamp) -> str:
		find = bisect_left(self.dic_win[key], (timestamp + 1,)) - 1
		if find == -1:
			return ''
		else:
			return self.dic_win[key][find][1]



if __name__ == '__main__':
	s = TimeMap()
	s.set("foo", "bar", 1)
	print(s.get("foo", 1))
	print(s.get("foo", 3))
	s.set("foo", "bar2", 4)
	print(s.get("foo", 4))
	print(s.get("foo", 5))