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


# 3.我的日程安排表2
## 方法一：差分
from sortedcontainers import SortedDict

class MyCalendarTwo:

    def __init__(self):
        self.sd = SortedDict()

    def book(self, startTime: int, endTime: int) -> bool:
        self.sd[startTime] = self.sd.get(startTime, 0) + 1
        self.sd[endTime] = self.sd.get(endTime, 0) - 1
        s = 0
        for v in self.sd.values():
            s += v
            if s > 2:
                self.sd[startTime] -= 1
                self.sd[endTime] += 1
                return False
        return True

# 4.我的日程安排表3
class MyCalendarThree:
	def __init__(self):
		self.calendar = SortedDict()

	def book(self, startTime, endTime):
		self.calendar[startTime] = self.calendar.get(startTime, 0) + 1
		self.calendar[endTime] = self.calendar.get(endTime, 0) - 1
		s = 0
		ans = 0
		for v in self.caledar.values():
			s += v
			ans = max(ans, s)
		return ans

# 5.不含特殊楼层的最大连续楼层数
class Solution1:
	def maxConsecutive(self, bottom, top, special):
		new_arr = [bottom - 1] + special + [top + 1]
		new_arr.sort()
		ans = 0
		for i in range(1, len(new_arr)):
			ans = max(ans, new_arr[i] - new_arr[i - 1] - 1)
		return ans

# 6.按键变更的次数
class Solution1:
	def countKeyChanges(self, s):
		ans = 0
		n = len(s)
		for i in range(1, n):
			if s[i].lower() == s[i - 1].lower():
				continue
			ans += 1
		return ans




