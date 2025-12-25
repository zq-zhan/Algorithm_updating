from functools import cache
from bisect import bisect_left

class Solution:
	def maxTwoEvents(self, events):
		events.sort()
		n = len(events)
		@cache
		def dfs(i, end, cnt):
			if cnt >= 2 or i == n:
				return 0
			if end >= events[i][0]:
				return dfs(i + 1, end, cnt)
			return max(dfs(i + 1, end, cnt), dfs(i + 1, max(end, events[i][1]), cnt + 1) + events[i][2])
		return dfs(0, 0, 0)

## 灵神题解
class Solution:
	def maxTwoEvents(self, events):
		events.sort(key = lambda x:x[1])

		st = [(0, 0)]
		ans = 0
		for start, end, val in events:
			i = bisect_left(st, (start,)) - 1 # 二分查找最后一个结束时间<start_time的活动
			ans = max(ans, st[i][1] + val)
			if val > st[-1][1]:
				st.append((end, val))
		return ans

if __name__ == '__main__':
	events = [[10,83,53],[63,87,45],[97,100,32],[51,61,16]]
	print(Solution().maxTwoEvents(events))