from itertools import accumulate

class Solution:
	def corpFlightBookings(self, bookings, n):
		ans = [0] * (n + 1)
		for first, last, seats in bookings:
			ans[first - 1] += seats
			ans[last] -= seats
		return list(accumulate(ans))[:-1]

if __name__ == '__main__':
	bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
	n = 5
	print(Solution().corpFlightBookings(bookings, n))