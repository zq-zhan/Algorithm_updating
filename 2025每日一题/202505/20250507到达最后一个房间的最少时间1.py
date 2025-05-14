from functools import cache
from math import inf
import heapq

# 20250507到达最后一个房间的最少时间1
class Solution1:
	def minTimeToReach(self, moveTime):
		n, m = len(moveTime), len(moveTime[0])
		moveTime[0][0] = 0
		@cache
		def dfs(i, j):
			if i == 0 and j == 0:
				return moveTime[0][0]
			elif i < 0 or j < 0 or i >= n or j >= m:
				return inf
			temp_movetime = moveTime[i][j]
			return min(max(dfs(i - 1, j), temp_movetime), 
					max(dfs(i, j - 1), temp_movetime),
					max(dfs(i + 1, j), temp_movetime),
					max(dfs(i, j + 1), temp_movetime)
					) + 1
		return dfs(n - 1, m - 1)
	
## 灵神题解
class Solution2:
	def minTimeToReach(self, moveTime):
		n, m = len(moveTime), len(moveTime[0])
		dis = [[inf] * m for _ in range(n)]
		dis[0][0] = 0
		h = [(0, 0, 0)]
		while True:
			d, i, j = heapq.heappop(h)
			if i == n - 1 and j == m - 1:
				return d
			if d > dis[i][j]:
				continue
			for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
				if 0 <= x < n and 0 <= y < m:
					new_dis = max(d, moveTime[x][y]) + 1
					if new_dis < dis[x][y]:
						dis[x][y] = new_dis
						heapq.heappush(h, (new_dis, x, y))

	
if __name__ == '__main__':
	moveTime = [[94,79,62,27,69,84],[6,32,11,82,42,30]]
	print(Solution2().minTimeToReach(moveTime)) 