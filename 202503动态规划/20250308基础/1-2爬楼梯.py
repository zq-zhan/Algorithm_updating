# 2.爬楼梯
from functools import cache

class Solution1:
	def climbStairs(self, n):
		@cache
		def dfs(i):
			if i <= 1:
				return 1
			return dfs(i - 1) + dfs(i - 2)
		return dfs(n)

## 递推写法
class Solution2:
	def climbStairs(self, n):
		f = [0] * (n + 1)
		f[0] = 1
		f[1] = 1
		for i in range(2, n + 1):
			f[i] = f[i - 1] + f[i - 2]
		return f[n]
## 空间优化
class Solution3:
	def climbStairs(self, n):
		f0 = f1 = 1
		for _ in range(2, n + 1):
			new_f = f0 + f1
			f0 = f1
			f1 = new_f
		return new_f
		

if __name__ == '__main__':
	n = 4
	print(Solution3().climbStairs(n)) # Output: 2
