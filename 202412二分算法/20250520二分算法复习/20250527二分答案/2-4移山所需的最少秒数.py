from math import sqrt
from heapq import heapify, heapreplace

class Solution1:
	def minNumberOfSeconds(self, mountainHeight, workerTimes):
		def check(target):
			ans = 0
			for x in workerTimes:
				ans += (sqrt(1 + 8 * target / x) - 1) // 2
			return ans >= mountainHeight

		mx = max(workerTimes)
		left, right = 0, mx * mountainHeight * (mountainHeight + 1) // 2
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				right = mid
			else:
				left = mid
		return right
	
## 灵神题解2——最小堆模拟
class Solution2:
	def minNumberOfSeconds(self, mountainHeight, workerTimes):
		h = [(t, t, t) for t in workerTimes]
		heapify(h)
		for _ in range(mountainHeight):
			nxt, delta, base = h[0]
			# 工作后总用时，当前工作用时，workerTimes[i]
			heapreplace(h, (nxt + delta + base, delta + base, base))
		return nxt
	
if __name__ == '__main__':
	mountainHeight = 10
	workerTimes = [3,2,2,4]
	print(Solution2().minNumberOfSeconds(mountainHeight, workerTimes))