# 10.我的日程安排表3
from sortedcontainers import SortedDict


class MyCalendarThree:
	def __init__(self):
		self.calendar = SortedDict()
		# self.new_dict = self.calendar

	def book(self, startTime, endTime):
		new_arr = self.calendar  # 在修改new_arr时，也会修改self.calendar，除非用copy()拷贝，则对new_arr的修改不会改变self.calendar
		new_arr[startTime] = new_arr.get(startTime, 0) + 1
		new_arr[endTime] = new_arr.get(endTime, 0) - 1 

		s = ans = 0
		for v in new_arr.values():
			s += v
			ans = max(ans, s)
		return ans
	
if __name__ == '__main__':
	cls = MyCalendarThree()
	print(cls.book(10, 20)) # 1
	print(cls.book(50, 60)) # 1
	print(cls.book(10, 40)) # 2
	print(cls.book(5, 15)) # 3
	print(cls.book(5, 10)) # 3
	print(cls.book(25, 55)) # 3