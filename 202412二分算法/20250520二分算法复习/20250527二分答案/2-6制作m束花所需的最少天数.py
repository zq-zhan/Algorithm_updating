from bisect import bisect_right

class Solution1:
	def minDays(self, bloomDay, m, k):
		if len(bloomDay) < m * k:
			return -1

		def check(target):
			ans = cnt = 0
			for x in bloomDay:
				if x <= target:
					cnt += 1
					if cnt >= k:
						ans += 1
						cnt = 0
						if ans >= m:
							return True
				else:
					cnt = 0
			return False

		left, right = min(bloomDay) - 1, max(bloomDay)
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				right = mid
			else:
				left = mid
		return right
	
if __name__ == '__main__':
	bloomDay = [7,7,7,7,12,7,7]
	m = 2
	k = 3
	print(Solution1().minDays(bloomDay, m, k))