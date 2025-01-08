# 1.范围内整数的最大得分
from math import inf


# class Solution1:
# 	def maxPossibleScore(self, start, d):
# 		def check(mx):

# 		left, right = 0, max(start)
# 		start.sort()

## 灵神题解
class Solution2:
	def maxPossibleScore(self, start, d):
		def check(score):
			x = -inf
			for s in start:
				x = max(x + score, s)
				if x > s + d:
					return False
			return True

		start.sort()
		left, right = 0, (start[-1] + d - start[0]) // (len(start) - 1) + 1
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				left = mid
			else:
				right = mid
		return left


if __name__ == '__main__':
	start = [6,0,3]
	d = 2
	cls = Solution2()
	print(cls.maxPossibleScore(start, d))