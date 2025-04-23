from functools import cache

# 20250421统计隐藏数组数目
class Solution1:
	def numberOfArrays(self, differences, lower, upper):
		ans = True
		n = len(differences)
		@cache
		def dfs(i, c):
			if i < 1:
				return True
			if lower <= c - differences[i - 1] <= upper:
				return dfs(i - 1, c - differences[i - 1])
			else:
				return False

		return sum(int(dfs(n, x)) for x in range(lower, upper + 1))
			
## 灵神题解			
class Solution2:
	def numberOfArrays(self, differences, lower, upper):
		x = mi = mx = 0
		for d in differences:
			x += d
			mi = min(mi, x)
			mx = max(mx, x)
		return max(upper - lower - (mx - mi) + 1, 0)


if __name__ == '__main__':
	differences = [10881,46364,-73321,-8922]
	lower = -68286
	upper = 78748
	print(Solution2().numberOfArrays(differences, lower, upper))