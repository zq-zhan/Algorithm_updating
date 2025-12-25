from functools import cache

class Solution:
	def findMaxForm(self, strs, m, n):
		strs_0 = []
		strs_1 = []
		for x in strs:
			zero_num = x.count('0')
			strs_0.append(zero_num)
			strs_1.append(len(x) - zero_num)
		@cache
		def dfs(i, x, y):
			if i < 0:
				return 0
			if x + strs_0[i] <= m and y + strs_1[i] <= n:
				return max(dfs(i - 1, x, y), dfs(i - 1, x + strs_0[i], y + strs_1[i]) + 1)
			return dfs(i - 1, x, y)
		return dfs(len(strs) - 1, 0, 0)

if __name__ == '__main__':
	strs = ["10", "0001", "111001", "1", "0"]
	m = 5
	n = 3
	print(Solution().findMaxForm(strs, m, n))