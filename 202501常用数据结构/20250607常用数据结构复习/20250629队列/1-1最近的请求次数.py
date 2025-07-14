from collections import deque

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
	print(obj.ping(3003)) 