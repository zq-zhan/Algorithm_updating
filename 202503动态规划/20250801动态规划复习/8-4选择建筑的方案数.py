from functools import cache

class Solution:  # 超出内存，恰好为k的买卖股票
	def numberOfWays(self, s):
		n = len(s)
		@cache
		def dfs(i, j, x):
			if j < 0:
				return 0
			if i < 0:
				return int(j == 0)
			if s[i] == x:
				return dfs(i - 1, j, x)
			return dfs(i - 1, j, x) + dfs(i - 1, j - 1, s[i])
		return dfs(n - 1, 3, -1)
## 灵神题解——前后缀分解
class Solution:
	def numberOfWays(self, s):
		n = len(s)
		pre_0 = [0] * (n + 1)
		suf_0 = [0] * (n + 1)
		pre_1 = [0] * (n + 1)
		suf_1 = [0] * (n + 1)
		for i in range(n):
			pre_0[i + 1] = pre_0[i] + int(s[i] == '0')
			pre_1[i + 1] = pre_1[i] + int(s[i] == '1')
		for i in range(n - 1, -1, -1):
			suf_0[i] = suf_0[i + 1] + int(s[i] == '0')
			suf_1[i] = suf_1[i + 1] + int(s[i] == '1')
		ans = 0
		for i, x in enumerate(s):
			if x == '1':
				ans += pre_0[i] * suf_0[i + 1]
			else:
				ans += pre_1[i] * suf_1[i + 1]
		return ans
		# tot_0 = s.count('0')
		# ans = c0 = 0
		# for i, x in enumerate(s):
		# 	if x == '1':
		# 		ans += c0 * (total - c0)
		# 	else:
		# 		c1 = i - c0
		# 		ans += c1 * (len(s) - tot_0 - c1)
		# 		c0 += 1
		# return ans
		
if __name__ == '__main__':
	s = "001101"
	print(Solution().numberOfWays(s))