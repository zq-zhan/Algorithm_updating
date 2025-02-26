# 6.航班预订统计
from itertools import accumulate

class Solution1:
	def corpFlightBookings(self, booking, n):
		# max_end = max(last for _, last, _ in booking)
		d = [0] * (n + 2)
		for first, last, seat in booking:
			d[first] += seat
			d[last + 1] -= seat

		ans = list(accumulate(d))[1:-1]
		return ans
	
if __name__ == '__main__':
	booking = [[1,2,10],[2,3,20],[2,5,25]]
	n = 5
	s = Solution1()
	print(s.corpFlightBookings(booking, n))