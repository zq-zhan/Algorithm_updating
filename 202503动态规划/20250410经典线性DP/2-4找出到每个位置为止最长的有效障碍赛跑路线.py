from functools import cache
from bisect import bisect_right

# 4.找出到每个位置为止最长的有效障碍赛跑路线
class Solution1:
	def longestObstacleCourseAtEachPosition(self, obstacles):
		n = len(obstacles)
		# @cache
		def dfs(i):
			ans = 0
			for j in range(i):
				if obstacles[j] <= obstacles[i]:
					ans = max(ans, dfs(j))
			return ans + 1
		ans = list(dfs(i) for i in range(n))
		return ans
	
## 二分 + 贪心
class Solution1:
	def longestObstacleCourseAtEachPosition(self, obstacles):
		n = len(obstacles)
		g = []
		ans = []
		for i, x in enumerate(obstacles):
			j = bisect_right(g, x)
			if j == len(g):
				g.append(x)
			else:
				g[j] = x
			ans.append(j + 1)
		return ans

	
if __name__ == '__main__':
	obstacles = [3,1,5,6,4,2]
	print(Solution1().longestObstacleCourseAtEachPosition(obstacles))
	