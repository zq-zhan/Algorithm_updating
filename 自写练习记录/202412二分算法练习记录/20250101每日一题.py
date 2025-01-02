# 1、将日期转换为二进制表示
class Solution1:
	def convertDateToBinary(self, date):
		a_lis = date.split('-')
		for i in range(len(a_lis)):
			a_lis[i] = bin(a_lis[i])[2:]
		return '-'.join(a_lis)

# 2、我的日程安排表1
class MyCalendar:
	def __init__(self):
		self.caledar_dic = []

	def book(self, startTime, endTime):
		if len(self.caledar_dic) == 0:
			self.caledar_dic.append([startTime, endTime])
			return True
		caledar_dic = self.caledar_dic
		caledar_dic.sort(key = lambda x: x[0])
		for i in range(len(caledar_dic)):
			if caledar_dic[i][1] <= startTime:
				if i == len(caledar_dic) - 1:
					self.caledar_dic.append([startTime, endTime])
					return True
				continue
			else:
				if caledar_dic[i][0] >= endTime:
					self.caledar_dic.append([startTime, endTime])
					return True
				else:
					return False
## 二分法
class MyCalendar2:
	def __init__(self):
		self.calendar = []

	def book(self, start, end):
		left, right = -1, len(self.calendar)
		while left + 1 < right:
			mid = (left + right) // 2
			s, e = self.calendar[mid]
			if end <= s:
				right = mid
			elif start >= e:
				left = mid
			elif s < end and e > start:
				return False
		self.calendar.insert(left, (start, end))
		self.calendar.sort(key = lambda x: x[0])
		return True