# 4.我的日程安排表3
from sortedcontainers import SortedDict


class MyCalendarThree:
	def __init__(self):
		self.calendar = SortedDict()

	def book(self, startTime, endTime):
		self.calendar[startTime] = self.calendar.get(startTime, 0) + 1
		self.calendar[endTime] = self.calendar.get(endTime, 0) - 1
		s = 0
		ans = 0
		for v in self.calendar.values():
			s += v
			ans = max(ans, s)
		return ans

if __name__ == '__main__':
	calendar = MyCalendarThree()
	class1 = [10, 20]
	class2 = [50, 60]
	class3 = [10, 40]
	class4 = [5, 15]
	class5 = [5, 10]
	class6 = [25, 55]
	print(calendar.book(class1[0], class1[1])) # Output: 1
	print(calendar.book(class2[0], class2[1])) # Output: 1
	print(calendar.book(class3[0], class3[1])) # Output: 2
	print(calendar.book(class4[0], class4[1])) # Output: 3
	print(calendar.book(class5[0], class5[1])) # Output: 3
	print(calendar.book(class6[0], class6[1])) # Output: 3