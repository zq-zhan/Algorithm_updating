import math

class Solution:
	def isPowerOfThree(self, n):
		if n <= 0:
			return False
		target = int(math.log(n, 3))
		for i in range(target + 1):
			if 3 ** i == n:
				return True
		return False


if __name__ == '__main__':
	n = 9
	print(Solution().isPowerOfThree(n))