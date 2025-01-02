# 2.完成旅途的最少时间
class Solution1:
	def minimumTime(self, time, totalTrips):
		left, right = 0, min(time) * totalTrips
		while left + 1 < right:
			mid = (left + right) // 2
			if sum(time[mid] // x for x in time) >= total:
				right = mid
			else:
				left = mid
		return right