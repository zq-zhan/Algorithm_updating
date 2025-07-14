import heapq

class SeatManager:

	def __init__(self, n):
		self.pq = [1]
		heapq.heapify(self.pq)

	def reserve(self):
		x = heapq.heappop(self.pq)
		if not self.pq:
			heapq.heappush(self.pq, x + 1)
		return x

	def unreserve(self, seatNumber):
		heapq.heappush(self.pq, seatNumber)
		
if __name__ == '__main__':
	sm = SeatManager(5)
	print(sm.reserve())
	print(sm.reserve())
	sm.unreserve(2)
	print(sm.reserve())
	print(sm.reserve())
	print(sm.reserve())
	print(sm.reserve())
	sm.unreserve(5)