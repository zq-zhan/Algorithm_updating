from functools import cache
from bisect import bisect_right

class Solution:  # 超时，复杂度O(n^2)
	def longestObstacleCourseAtEachPosition(self, obstacles):
		ans = []
		n = len(obstacles)
		@cache
		def dfs(i):
			res = 0
			for j in range(i):
				if obstacles[j] <= obstacles[i]:
					res = max(res, dfs(j))
			return res + 1
		for i in range(n):
			ans.append(dfs(i))
		return ans

## 二分 + 贪心
class Solution:
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
			ans.append(j + 1)  # 遍历到此时nums[i]、并以它结尾的元素在g列表中的位置，才为以nums[i]结尾的有效障碍跑长度
		return ans

if __name__ == '__main__':
	obstacles = [1,2,3,2]
	print(Solution().longestObstacleCourseAtEachPosition(obstacles))