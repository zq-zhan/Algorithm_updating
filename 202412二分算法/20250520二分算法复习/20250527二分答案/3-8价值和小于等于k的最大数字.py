from math import isqrt

class Solution:
	def findMaximumNumber(self, k, x):
		def check(target):
			ans = 0
			for num in range(1, mid + 1):
				bin_num = bin(num)[2:]
				ans += sum([int(bin_num[i]) for i in range(0, len(bin_num), x)])
				if ans > k:
					return False
			return True

		left, right = 1, (isqrt(1 + 8 * k) - 1) // 2
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				left = mid
			else:
				right = mid
		return left
	
if __name__ == '__main__':
	print(Solution().findMaximumNumber(9, 1))