from collections import defaultdict, deque
from bisect import bisect_left, bisect_right


# class Router:
# 	def __init__(self, memoryLimit):
# 		self.arr = []
# 		self.memoryLimit = memoryLimit

# 	def addPacket(self, source, destination, timestamp):
# 		# if (source, timestamp) in self.dic_win[destination]:
# 		set_temp = set(self.arr)
# 		if (source, destination, timestamp) in set_temp:
# 			return False
# 		else:
# 			if self.memoryLimit == 0:
# 				self.arr.pop(0)
# 			else:
# 				self.memoryLimit -= 1
# 			self.arr.append((source, destination, timestamp))
# 			return True

# 	def forwardPacket(self):
# 		if len(self.arr) == 0:
# 			return []
# 		else:
# 			self.memoryLimit += 1
# 			return self.arr.pop(0)

# 	def getCount(self, destination, startTime, endTime):
# 		ans = 0
# 		for s, d, t in self.arr:
# 			if d == destination and startTime <= t <= endTime:
# 				ans += 1
# 		return ans
	

## 队列
class Router:
	def __init__(self, memoryLimit):
		self.set_temp = set()
		self.memoryLimit = memoryLimit
		self.dic_win = defaultdict(deque)
		self.deque_temp = deque()

	def addPacket(self, source, destination, timestamp):
		packet = (source, destination, timestamp)
		if packet in self.set_temp:
			return False
		if len(self.deque_temp) == self.memoryLimit:
			self.forwardPacket()

		self.set_temp.add(packet)
		self.dic_win[destination].append(timestamp)
		self.deque_temp.append(packet)
		return True

	def forwardPacket(self):
		if len(self.deque_temp) == 0:
			return []

		packet = self.deque_temp.popleft()
		self.set_temp.remove(packet)
		self.dic_win[packet[1]].popleft()
		return list(packet)

	def getCount(self, destination, startTime, endTime):
		nums = self.dic_win[destination]
		find_right = bisect_right(nums, endTime) - 1
		find_left = bisect_left(nums, startTime)
		return find_right - find_left + 1

if __name__ == '__main__':
	s = Router(3)
	print(s.addPacket(1, 4, 90))
	print(s.addPacket(2, 5, 90))
	print(s.addPacket(1, 4, 90))
	print(s.addPacket(3, 5, 95))
	print(s.addPacket(4, 5, 105))
	print(s.forwardPacket())
	print(s.addPacket(5, 2, 110))
	print(s.getCount(5, 100, 110))

	