from functools import cache
from math import inf

class Solution1:
	def coinChange(self, coins, amount):
		@cache
		def dfs(i, c):
			if i < 0:
				return 0 if c == 0 else inf
			if c < coins[i]:
				return dfs(i - 1, c)
			return min(dfs(i - 1, c), dfs(i, c - coins[i]) + 1)
		ans = dfs(len(coins) - 1, amount)
		return ans if ans < inf else -1
	
## 递推写法
class Solution2:
	def coinChange(self, coins, amount):
		n = len(coins)
		f = [[inf] * (amount + 1) for _ in range(n + 1)]
		f[0][0] = 0
		for i, x in enumerate(coins):
			for c in range(amount + 1):
				if c >= x:
					f[i + 1][c] = min(f[i][c], f[i + 1][c - x] + 1)
				else:
					f[i + 1][c] = f[i][c]
		ans = f[n][amount] 
		return ans if ans < inf else -1
	
## 优化为一维
class Solution3:
	def coinChange(self, coins, amount):
		n = len(coins)
		f = [0] + [inf] * amount
		for x in coins:
			for c in range(x, amount + 1):
				f[c] = min(f[c], f[c - x] + 1)
		return f[-1] if f[-1] < inf else -1
	
class Solution1:
	def coinChange(self, coins, amount):
		@cache
		def dfs(i, c):
			if i < 0:
				return 0 if c == 0 else inf
			if coins[i] > c:
				return dfs(i - 1, c)
			return min(dfs(i - 1, c), dfs(i, c - coins[i]) + 1)
		ans = dfs(len(coins) - 1, amount)
		return ans if ans < inf else -1

if __name__ == '__main__':
	coins = [1, 2, 5]
	amount = 11
	s = Solution4()
	print(s.coinChange(coins, amount))