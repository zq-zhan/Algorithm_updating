# 1.找到最常见的回答
class Solution1:
	def findCommonResponse(self, responses):
		dic_res = defaultdict(int)
		for response in responses:
			response = set(response)
			for x in response:
				dic_res[x] += 1
		max_cnt = max(dic_res.values())
		ans_lis = [char for char in dic_res.keys() if dic_res[char] == max_cnt]
		if len(ans_lis) == 1:
			return ans_lis[0]
		else:
			ans = ans_lis[0]
			for x in ans_lis:
				if x < ans:
					ans = x
			return ans

# 2.单位转换1
class Solution1:
	def baseUnitConversions(self, conversions):
		n = len(conversions)
		ans = [1] + [0] * n
		mod = 10 ** 9 + 7
		for i in range(n):
			now_conver = conversions[i]
			ans[now_conver[1]] = now_conver[2] * ans[now_conver[0]] % mod
		return ans

# 3.统计水平子串和垂直子串重叠格子的数目
class Solution:
	def countCells(self, grid, pattern):
		length = len(pattern)
		m, n = len(grid), len(grid[0])
		def check_row(i, j):
			for x in range(length):
				times = (j + x) // n
				mod = (j + x) % n
				if i + times <= m - 1 and grid[i + times][mod] == pattern[x]:
					continue
				else:
					return False
			return True
		def check_column(i, j):
			for x in range(length):
				times = (i + x) // m
				mod = (i + x) % m
				if j + times <= n - 1 and grid[mod][j + times] == pattern[x]:
					continue
				else:
					return False
			return True

		lis1 = [[0] * n for _ in range(m)]
		lis2 = [[0] * n for _ in range(m)]
		# ans = 0
		for i in range(m):
			for j in range(n):
				if grid[i][j] == pattern[0] and check_row(i, j):
					for x in range(length):
						times = (j + x) // n
						mod = (j + x) % n
						lis1[i + times][mod] = 1
				if grid[i][j] == pattern[0] and check_column(i, j):
					for x in range(length):
						times = (i + x) // m
						mod = (i + x) % m
						lis2[mod][j + times] = 1
			# for k in range(m):
			# 	if lis1[i][] == lis2[i][j] == 1:
			# 		ans += 1

		ans = 0
		for i in range(m):
			for j in range(n):
				if lis1[i][j] == lis2[i][j] == 1:
					ans += 1
		return ans

				
class Solution:
	def countCells(self, grid, pattern):
		length = len(pattern)
		m, n = len(grid), len(grid[0])
		def check_row(i, j):
			for x in range(length):
				times = (j + x) // n
				mod = (j + x) % n
				if i + times <= m - 1 and grid[i + times][mod] == pattern[x]:
					continue
				else:
					return False
			return True
		def check_column(i, j):
			for x in range(length):
				times = (i + x) // m
				mod = (i + x) % m
				if j + times <= n - 1 and grid[mod][j + times] == pattern[x]:
					continue
				else:
					return False
			return True

		lis1 = [[''] * n for _ in range(m)]
		# lis2 = [[0] * n for _ in range(m)]
		# ans = 0
		for i in range(m):
			for j in range(n):
				if grid[i][j] == pattern[0] and check_row(i, j):
					for x in range(length):
						times = (j + x) // n
						mod = (j + x) % n
						lis1[i + times][mod] += 'a'
				if grid[i][j] == pattern[0] and check_column(i, j):
					for x in range(length):
						times = (i + x) // m
						mod = (i + x) % m
						lis1[mod][j + times] += 'b'
			# for k in range(m):
			# 	if lis1[i][] == lis2[i][j] == 1:
			# 		ans += 1

		ans = 0
		for i in range(m):
			for j in range(n):
				if 'a' in lis1[i][j] and 'b' in lis1[i][j]:
					ans += 1
		return ans
