class RecentCounter:
	def __init__(self):
		self.queue = []

	def ping(self, t):
		self.queue.append(t)
		i = 0
		while self.queue[i] < t - 3000:
			i += 1
		return len(self.queue) - i
	
## 队列解法，因为pop(0)的复杂度是O(n)，需要移动后续元素向前填补空缺
class RecentCounter:
	def __init__(self):
		self.queue = deque()

	def ping(self, t):
		while self.queue and self.queue[0] < t - 3000:
			self.queue.popleft()
		self.queue.append(t)
		return len(self.queue)

if __name__ == '__main__':
	obj = RecentCounter()
	print(obj.ping(1)) # 1
	print(obj.ping(100)) # 2
	print(obj.ping(3001)) # 3
	print(obj.ping(3002)) # 3