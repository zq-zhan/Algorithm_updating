# 6.移山所需的最小秒数
from math import sqrt
import heapq


class Solution1:
	# def __init__(self):  # 无需如此，check已经是类方法
	# 	self.check = self

	def check(self, mountainHeight, workerTimes, mid):
		cum_sum = 0
		for x in workerTimes:
			# cnt = 1
			# temp_cum_sum = 0
			# while temp_cum_sum + x * cnt <= mid:
			# 	temp_cum_sum += x * cnt
			# 	cnt += 1
			# cum_sum += cnt - 1
			ans = (sqrt(1 + 8 * mid // x) - 1) // 2
			cum_sum += ans
		return cum_sum >= mountainHeight

	def minNumberOfSeconds(self, mountainHeight, workerTimes):
		# min_time = min(workerTimes)
		# cnt = 1
		# right_cnt = 0
		# while cnt <= mountainHeight:
		# 	right_cnt += min_time * cnt
		# 	cnt += 1
		left, right = 0, max(workerTimes) * mountainHeight * (1 + mountainHeight) // 2
		while left + 1 < right:
			mid = (left + right) // 2
			if self.check(mountainHeight, workerTimes, mid):
				right = mid
			else:
				left = mid
		return right





class Solution2:

	def check(self, mountainHeight, workerTimes, mid):
		cum_sum = 0
		for x in workerTimes:
			# cnt = 1
			# temp_cum_sum = 0
			# while temp_cum_sum + x * cnt <= mid:
			# 	temp_cum_sum += x * cnt
			# 	cnt += 1
			# cum_sum += cnt - 1
			ans = int((sqrt(mid * 2 / x * 4 + 1) - 1) / 2)
			if ans * (ans + 1) < mid:
				cum_sum += ans + 1
			else:
				cum_sum += ans
		return cum_sum >= mountainHeight

	def minNumberOfSeconds(self, mountainHeight, workerTimes):
		# min_time = min(workerTimes)
		# cnt = 1
		# right_cnt = 0
		# while cnt <= mountainHeight:
		# 	right_cnt += min_time * cnt
		# 	cnt += 1
		left, right = 0, max(workerTimes) * mountainHeight * (1 + mountainHeight) // 2
		while left + 1 < right:
			mid = (left + right) // 2
			if self.check(mountainHeight, workerTimes, mid):
				right = mid
			else:
				left = mid
		return right


# 13.移山所需的最少秒数
class Solution3:
	def minNumberOfSeconds(self, mountainHeight, workerTimes):
		def check(mid, workerTimes, mountainHeight):
			ans = 0
			for x in workerTimes:
				ans += (sqrt(1 + 8 * mid // x) - 1) // 2
			return ans >= mountainHeight


		left, right = 0, max(workerTimes) * (mountainHeight + 1) * mountainHeight // 2 + 1
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid, workerTimes, mountainHeight):
				right = mid
			else:
				left = mid
		return right
	
## 灵神方法二：最小堆模拟
## 灵神方法二：最小堆模拟
class Solution4:
	def minNumberOfSeconds(self, mountainHeight, workerTimes):
		h = [(t, t, t) for t in workerTimes]
		heapq.heapify(h)
		for _ in range(mountainHeight):
			nxt, delta, base = h[0]
			heapq.heapreplace(h, (nxt + delta + base, delta + base, base))
		return nxt



if __name__ == '__main__':
	mountainHeight = 4
	workerTimes = [2,1,1]
	cls = Solution4()
	print(cls.minNumberOfSeconds(mountainHeight, workerTimes))