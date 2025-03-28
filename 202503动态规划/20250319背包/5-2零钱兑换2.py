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
	
if __name__ == '__main__':
	s = Solution1()
	amount = 5
	coins = [1, 2, 5]
	print(s.change(amount, coins))