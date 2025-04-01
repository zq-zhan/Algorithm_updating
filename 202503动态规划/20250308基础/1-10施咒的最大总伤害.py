from functools import cache
from bisect import bisect_left, bisect_right
from collections import Counter,defaultdict

class Solution1:
	def maximumTotalDamage(self, power):
		n = max(power) + 1
		a = [0] * n
		for x in power:
			a[x] += x
		@cache
		def dfs(i):
			if i < 0:
				return 0
			return max(dfs(i - 1), dfs(i - 2), dfs(i - 3) + a[i])
		return dfs(n - 1)
## 递推写法
class Solution2:
	def maximumTotalDamage(self, power):
		n = max(power) + 1
		a = [0] * n
		for x in power:
			a[x] += x
		f = [0] * n
		f[0] = a[0]
		f[1] = max(a[0], a[1])
		f[2] = max(a[0], a[1], a[2])
		for i in range(3, n):
			f[i] = max(f[i - 1], f[i - 2], f[i - 3] + a[i])
		return f[-1] 		

class Solution3:
	def maximumTotalDamage(self, power):
		cnt = Counter(power)
		a = sorted(cnt.keys())
		@cache
		def dfs(i):
			if i < 0:
				return 0
			x = a[i]
			# j = i
			j = bisect_left(a, x - 2)
			# while j and a[j - 1] >= x - 2:
			# 	j -= 1
			return max(dfs(i - 1), dfs(j - 1) + x * cnt[x])
		return dfs(len(a) - 1)

class Solution4:
	def maximumTotalDamage(self, power):
		cnt = defaultdict(int)
		for x in power:
			cnt[x] += 1
		a = sorted(cnt.keys())
		f = [0] * (len(a) + 1)

		# j = 0
		for i, c in enumerate(a):
			# while a[j] < c - 2:
			# 	j += 1
			j = bisect_left(a, c - 2)
			f[i + 1] = max(f[i], f[j] + c * cnt[c])
		return f[-1]

	
class Solution5:
	def maximumTotalDamage(self, power):
		max_num = max(power) + 1
		a = [0] * max_num
		for x in power:
			a[x] += x
		@cache
		def dfs(i):
			if i < 0:
				return 0
			return max(dfs(i - 1), dfs(i - 3) + a[i])
		return dfs(max_num - 1)


if __name__ == '__main__':
	power = [7,1,6,3]
	print(Solution4().maximumTotalDamage(power))