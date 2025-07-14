from itertools import accumulate
import heapq

class Solution:
	def maxEvents(self, events):
		events.sort(key = lambda x:x[0])
		ans = [events[0]]
		n = len(events)
		for i in range(1, n):
			if events[i][0] >= ans[-1][1]:
				ans.append(events[i])
			else:
				ans[-1][1] = events[i][0]
				ans.append(events[i])
		return len(ans)

class Solution:
	def maxEvents(self, events):
		mx = max(x for _, x in events)
		groups = [[] for _ in range(mx + 1)]
		for e in events:
			groups[e[0]].append(e[1])
		ans = 0
		h = []
		for i, g in enumerate(groups):
			while h and h[0] < i:
				heapq.heappop(h)
			for end_day in g:
				heapq.heappush(h, end_day)
			if h:
				ans += 1
				heapq.heappop(h)
		return ans



if __name__ == '__main__':
	events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
	print(Solution().maxEvents(events))