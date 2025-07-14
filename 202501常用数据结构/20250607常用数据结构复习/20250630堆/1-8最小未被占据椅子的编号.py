import heapq

class Solution:
	def smallestChair(self, times, targetFriend):
		times = [(x, y, i) for i, (x, y) in enumerate(times)]
		heapq.heapify(times)
		pre_end = []
		# heapq.heapify(pre_end)
		ans = 0
		while times[0][2] != targetFriend:
			ans += 1
			_, end, _ = heapq.heappop(times)
			heapq.heappush(pre_end, end)
			while pre_end and pre_end[0] <= times[0][0]:
				heapq.heappop(pre_end)
				ans -= 1
		return ans

class Solution:
	def smallestChair(self, times, targetFriend):
		times = [(x, y, i) for i, (x, y) in enumerate(times)]
		heapq.heapify(times)
		pre_end = []
		# heapq.heapify(pre_end)
		ans = [0] 
		while times[0][2] != targetFriend:
			_, end, _ = heapq.heappop(times)
			index = heapq.heappop(ans)
			heapq.heappush(pre_end, (end, index))
			if not ans:
				heapq.heappush(ans, index + 1)
			while pre_end and pre_end[0][0] <= times[0][0]:
				heapq.heappush(ans, heapq.heappop(pre_end)[1])
		return ans[0]

	
if __name__ == '__main__':
	# times = [[33,35],[26,29],[9,28],[4,31],[8,10],[32,34],[15,24],[27,39],[14,36],[1,14],[25,39],[5,27],[6,15],[2,38],[19,36],[24,34],[3,26]]
    times = [[1,4],[2,3],[4,6]]
    targetFriend = 1
    print(Solution().smallestChair(times, targetFriend))