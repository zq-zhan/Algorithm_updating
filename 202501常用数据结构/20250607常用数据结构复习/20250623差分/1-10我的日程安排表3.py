from collections import defaultdict
from sortedcontainers import SortedDict

# class MyCalendarThree:

# 	def __init__(self):
# 		dic_win = defaultdict(int)
# 		self.dic_win = dic_win
	
# 	def book(self, startTime, endTime):
# 		self.dic_win[startTime] += 1
# 		self.dic_win[endTime] -= 1
# 		ans = temp_s = 0
# 		for order_time, num in sorted(self.dic_win.items()):
# 			temp_s += num
# 			ans = max(ans, temp_s)
# 		return ans

## 有序字典
class MyCalendarThree:

	def __init__(self):
		self.dic_win = SortedDict()

	def book(self, startTime, endTime):
		new_arr = self.dic_win
		new_arr[startTime] = new_arr.get(startTime, 0) + 1
		new_arr[endTime] = new_arr.get(endTime, 0) - 1
		ans = temp_s = 0
		for v in new_arr.values():
			temp_s += v
			ans = max(ans, temp_s)
		return ans


if __name__ == '__main__':
	obj = MyCalendarThree()
	print(obj.book(10, 20)) # 1
	print(obj.book(50, 60)) # 1
	print(obj.book(10, 40)) # 2
	print(obj.book(5, 15)) # 3
	print(obj.book(5, 10)) # 3
	print(obj.book(25, 55))