# 2.分配给商店的最多商品的最小值
class Solution1:
	def minimizedMaximum(self, n, quantities):
		def check(mx):
			ans = 0
			for x in quantities:
				ans += (x - 1) // mx + 1
			return ans <= n

		right = sum(quantities)
		left = (right - 1) // n
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				right = mid
			else:
				left = mid
		return right