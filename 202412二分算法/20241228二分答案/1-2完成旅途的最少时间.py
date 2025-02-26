# 2.完成旅途的最少时间
class Solution1:
	def minimumTime(self, time, totalTrips):
		left, right = 0, min(time) * totalTrips
		while left + 1 < right:
			mid = (left + right) // 2
			if sum(time[mid] // x for x in time) >= totalTrips:
				right = mid
			else:
				left = mid
		return right
	
class Solution2:
	def minimumTime(self, time, totalTrips):
		left = 0
		right = totalTrips * min(time) + 1
		while left + 1 < right:
			mid = (left + right) // 2
			if sum(mid // x for x in time) >= totalTrips:
				right = mid
			else:
				left = mid
		return right
	
if __name__ == '__main__':
	time = [1,2,3]
	totalTrips = 5
	print(Solution2().minimumTime(time, totalTrips))