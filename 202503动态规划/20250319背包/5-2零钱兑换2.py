from functools import cache

class Solution1:
	def change(self, amount, coins):
		@cache
		def dfs(i, c):
			if i < 0:
				return 1 if c == 0 else 0
			if c < coins[i]:
				return dfs(i - 1, c)
			return dfs(i - 1, c) + dfs(i, c - coins[i])
		return dfs(len(coins) - 1, amount)
	
## 递推写法
class Solution2:
	def change(self, amount, coins):
		n = len(coins)
		f = [[0] * (amount + 1) for _ in range(n + 1)]
		f[0][0] = 1
		for i, x in enumerate(coins):
			for c in range(amount + 1):
				if c < x:
					f[i + 1][c] = f[i][c]
				else:
					f[i + 1][c] = f[i][c] + f[i + 1][c - x]
		return f[-1][-1]



if __name__ == '__main__':
	s = Solution1()
	amount = 5
	coins = [1, 2, 5]
	print(s.change(amount, coins))