class Solution:
	def minimizedMaximum(self, n, quantities):
		def check(target):
			cnt = 0
			for x in quantities:
				while x > 0:
					cnt += 1
					x -= target
					if cnt > n:
						return False
			return True

		left, right = min(quantities) // n - 1, max(quantities)
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				right = mid
			else:
				left = mid
		return right