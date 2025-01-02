# 8.修车的最少时间
from math import floor, isqrt


class Solution1:
	def check(self, ranks, cars, mid):
		ans = sum(isqrt(mid // x) for x in ranks)
		return ans >= cars
	def repairCars(self, ranks, cars):
		left, right = 0, min(ranks) * cars * cars
		while left + 1 < right:
			mid = (left + right) // 2
			if self.check(ranks, cars, mid):
				right = mid
			else:
				left = mid
		return right
	
if __name__ == '__main__':
	ranks = [4,2,3,1]
	cars = 10
	cls = Solution1()
	print(cls.repairCars(ranks, cars))