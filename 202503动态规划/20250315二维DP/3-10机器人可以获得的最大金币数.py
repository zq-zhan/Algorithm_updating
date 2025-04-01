import heapq
from functools import cache
from math import inf

# 7.机器人可以获得的最大金币数
class Solution1:
	def maximumAmount(self, coins):
		c_lis = [0, 0]
		heapq.heapify(c_lis)
		n, m = len(coins), len(coins[0])
		@cache
		def dfs(i, j, c_lis):
			if i < 0 or j < 0:
				return -inf
			elif i == 0 and j == 0:
				if coins[0][0] >= 0:
					return coins[0][0]
				else:
					heapq.heappush(c_lis, -coins[0][0])
					return -heapq.heappop(c_lis)
			if coins[i][j] >= 0:
				return max(dfs(i - 1, j, c_lis), dfs(i, j - 1, c_lis)) + coins[i][j]
			else:
				heapq.heappush(c_lis, -coins[i][j])
				x = -heapq.heappop(c_lis)
				return max(dfs(i - 1, j, c_lis), dfs(i, j - 1, c_lis)) + x
		return dfs(n - 1, m - 1, c_lis)
	
## 灵神题解
class Solution2:  # 错解
	def maximumAmount(self, coins):
		n, m = len(coins), len(coins[0])
		@cache
		def dfs(i, j, k):
			if i < 0 or j < 0:
				return -inf
			elif i == 0 and j == 0:
				if k > 0:
					return max(coins[0][0], 0)
				else:
					return coins[0][0]
			if k > 0 and coins[i][j] < 0:
				return max(
					max(dfs(i - 1, j, k), dfs(i, j - 1, k)) + coins[i][j],
					max(dfs(i - 1, j, k - 1), dfs(i, j - 1, k - 1))
					)
			else:
				return max(dfs(i - 1, j, k), dfs(i, j - 1, k)) + coins[i][j]
		return dfs(n - 1, m - 1, 2)

## 递推写法
class Solution3:  
	def maximumAmount(self, coins):
		n, m = len(coins), len(coins[0])
		f = [[[-inf] * 3 for _ in range(m + 1)] for _ in range(n + 1)]
		f[0][1] = [0] * 3
		for i in range(n):
			for j, x in enumerate(coins[i]):
				f[i + 1][j + 1][0] = max(f[i][j + 1][0], f[i + 1][j][0]) + coins[i][j]  # 必须选
				f[i + 1][j + 1][1] = max(
					max(f[i][j + 1][1], f[i + 1][j][1]) + coins[i][j],  # 选
					max(f[i][j + 1][0], f[i + 1][j][0])  # 不选
					)
				f[i + 1][j + 1][2] = max(
					max(f[i][j + 1][2], f[i + 1][j][2]) + coins[i][j],  # 选
					max(f[i][j + 1][1], f[i + 1][j][1])  # 不选
					)
		return f[-1][-1][2]

if __name__ == '__main__':
	coins = [[0,1,-1],[1,-2,3],[2,-3,4]]
	print(Solution3().maximumAmount(coins))