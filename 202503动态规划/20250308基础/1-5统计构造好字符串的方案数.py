# 5.统计构造好字符串的方案数
from functools import cache

class Solution1:
	def countGoodStrings(self, low, high, zero, one):
		@cache
		def dfs(i):
			if i == 0:
				return 1
			elif i < 0:
				return 0
			return dfs(i - zero) + dfs(i - one)
		ans = 0
		for num in range(low, high + 1):
			ans += dfs(num)
		return ans
	
## 递推写法
class Solution2:
	def countGoodStrings(self, low, high, zero, one):
		ans = 0
		for num in range(low, high + 1):
			f = [0] * (num + 1)
			f[0] = 1
			for i in range(1, num + 1):
				f[i] += f[i - zero] if i >= zero else 0
				f[i] += f[i - one] if i >= one else 0
			ans += f[-1]
		return ans % (10 ** 9 + 7)
	
if __name__ == '__main__':
	s = Solution1()
	print(s.countGoodStrings(3, 3, 1, 1))