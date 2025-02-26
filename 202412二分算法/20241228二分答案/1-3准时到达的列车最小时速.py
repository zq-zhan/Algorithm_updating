# 3.准时到达的列车最小时速
class Solution1:
	def minSpeedOnTime(self, dist, hour):
		left, right = 0, max(dist) + 1
		while left + 1 < right:
			mid = (left + right) // 2
			if sum((x - 1) // mid for x in dist[:-1]) + dist[-1] / mid <= hour - len(dist) + 1:
				right = mid
			else:
				left = mid
		if right >= max(dist):
			return -1
		return right
	
## 灵神思路
class Solution2:
	def minSpeedOnTime(self, dist, hour):
		n = len(dist)
		h100 = round(hour * 100)  # 去除浮点数影响
		if h100 <= (n - 1) * 100:  # 前面n-1个站至少花费n-1个小时，且还有最后一个站
			return -1

		max_dist = max(dist)
		if h100 <= n * 100:  # hour <= n的情况
			return max(max_dist, (dist[-1] * 100 - 1) // (h100 - (n - 1) * 100) + 1)

		def check(v):
			t = n - 1  # n-1个1
			for x in dist[:-1]:
				t += (x - 1) // v
			return (t * v + dist[-1]) * 100 <= h100 * v

		left, right = 0, max_dist
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				right = mid
			else:
				left = mid
		return right
	
class Solution3:
	def minSpeedOnTime(self, dist, hours):
		left, right = 0, sum(dist)
		while left + 1 < right:
			mid = (left + right) // 2
			if sum((x - 1) // mid + 1 for x in dist) <= hour:
				right = mid
			else:
				left = mid
		return right

if __name__ == '__main__':
	dist = [1,3,2]
	hour = 2.7
	cls = Solution1()
	print(cls.minSpeedOnTime(dist, hour))