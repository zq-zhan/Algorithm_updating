# 4.无限集中的最小数字
import heapq
from sortedcontainers import SortedSet
			
# 4.无限集中的最小数字
# class SmallestInfiniteSet:  # 堆解法
# 	def __init__(self):
# 		self.heap_lis = [i + 1 for i in range(1000)]  # list(range(1, 1001))
# 		heapq.heapify(self.heap_lis)

# 	def popSmallest(self):
# 		return heapq.heappop(self.heap_lis)

# 	def addBack(self, num):
# 		if num not in self.heap_lis:
# 			heapq.heappush(self.heap_lis, num)
## 有序集合做法
class SmallestInfiniteSet:
	def __init__(self):
		self.s = SortedSet(range(1, 1001))

	def popSmallest(self):
		x = self.s[0]
		self.s.remove(x)
		return x

	def addBack(self, num):
		self.s.add(num)
			
if __name__ == '__main__':
	s = SmallestInfiniteSet()
	s.addBack(2)
	print(s.popSmallest())
	print(s.popSmallest())
	print(s.popSmallest())
	s.addBack(1)
	print(s.popSmallest())
	print(s.popSmallest())
	print(s.popSmallest())