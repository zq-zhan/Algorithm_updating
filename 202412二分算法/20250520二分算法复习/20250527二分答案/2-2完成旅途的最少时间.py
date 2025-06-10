class Solution:
	def minimumTime(self, time, totalTrips):
		left, right = 0, max(time) * totalTrips
		while left + 1 < right:
			mid = (left + right) // 2
			if sum(mid // x for x in time) >= totalTrips:
				right = mid
			else:
				left = mid
		return right
	
if __name__ == '__main__':
	time = [1, 2, 3]
	totalTrips = 5
	print(Solution().minimumTime(time, totalTrips))