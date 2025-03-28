from functools import cache

class Solution1:
	def minCostClimbingStairs(self, cost):
		cost.append(0)
		n = len(cost)
		@cache
		def dfs(i):
			if i < 0:
				return 0
			return min(dfs(i - 1) + cost[i - 1], dfs(i - 2) + cost[i - 2])
		return dfs(n - 1)
## 递推写法
class Solution2:
	def minCostClimbingStairs(self, cost):
		cost.append(0)
		f0 = f1 = 0
		for i in range(len(cost) - 1):
			new_f = min(f0 + cost[i], f1 + cost[i + 1])
			f0 = f1
			f1 = new_f
		return f1
	
class Solution3:
	def minCostClimbingStairs(self, cost):
		@cache
		def dfs(i):
			if i <= 1:
				return 0
			return min(dfs(i - 1) + cost[i - 1], dfs(i - 2) + cost[i - 2])
		return dfs(len(cost))
## 递推优化
class Solution4:
	def minCostClimbingStairs(self, cost):
		f0 = f1 = 0
		for i in range(2, len(cost) + 1):
			new_f = min(f0 + cost[i - 2], f1 + cost[i - 1])
			f0 = f1
			f1 = new_f
		return f1


if __name__ == '__main__':
	cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
	s = Solution4()
	print(s.minCostClimbingStairs(cost))