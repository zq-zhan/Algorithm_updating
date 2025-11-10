from functools import cache
from collections import Counter

class Solution:
	def maximumTotalDamage(self, power):
		mx = max(power)
		new_power = [0] * (mx + 1)
		for x in power:
			new_power[x - 1] += x
		# @cache
		def dfs(i):
			if i < 0:
				return 0
			return max(dfs(i - 1), dfs(i - 3) + new_power[i])
		return dfs(mx)
	
## 灵神题解——值域打家劫舍
class Solution:
	def maximumTotalDamage(self, power):
		cnt = Counter(power)
		a = sorted(cnt)

		@cache
		def dfs(i):
			if i < 0:
				return 0
			x = a[i]
			j = i
			while j and a[j - 1] >= x - 2:
				j -= 1
			return max(dfs(i - 1), dfs(j - 1) + x * cnt[x])
		return dfs(len(a) - 1)

	
if __name__ == '__main__':
	power = [1,1,3,4]
	print(Solution().maximumTotalDamage(power))