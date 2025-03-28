from functools import cache

class Solution1:
	def countHousePlacements(self, n):
		mod = (10 ** 9 + 7)
		@cache
		def dfs(i):
			if i < 0:
				return 0
			elif i == 0:
				return 1
			elif i == 1:
				return 2
			return dfs(i - 1) + dfs(i - 2)
		ans = dfs(n) % mod
		return (ans * ans) % mod
	
class Solution2:
	def countHousePlacements(self, n):
		mod = 10 ** 9 + 7
		@cache
		def dfs(i):
			if i == 0:
				return 1
			elif i == 1:
				return 2
			return (dfs(i - 1) + dfs(i - 2)) % mod
		ans = dfs(n) * dfs(n) % mod
		return ans
	
## 递推写法
class Solution3:
	def countHousePlacements(self, n):
		mod = 10 ** 9 + 7
		f0 = 1
		f1 = 2
		for _ in range(n - 1):
			new_f = (f0 + f1) % mod
			f0 = f1
			f1 = new_f
		return f1 * f1 % mod
	
if __name__ == '__main__':
	n = 2
	print(Solution3().countHousePlacements(n))