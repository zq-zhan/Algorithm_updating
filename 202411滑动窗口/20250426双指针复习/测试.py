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
		ans = 0
		for i in range(m):
			for j in range(n):
				if check_row(i, j):
					for x in range(length):
						times = (j + x) // n
						mod = (j + x) % n
						lis1[i + times][mod] = 1
				if check_column(i, j):
					for x in range(length):
						times = (i + x) // m
						mod = (i + x) % m
						lis2[mod][j + times] = 1
				if lis1[i][j] == lis2[i][j] == 1:
					ans += 1

		# ans = 0
		# for i in range(m):
		# 	for j in range(n):
		# 		if lis1[i][j] == lis2[i][j] == 1:
		# 			ans += 1
		return ans
	
class Solution2:
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

if __name__ == '__main__':
	grid = [["c","a","a","a"],["a","a","b","a"],["b","b","a","a"],["a","a","b","a"]]
	pattern = "aba"
	print(Solution2().countCells(grid, pattern))