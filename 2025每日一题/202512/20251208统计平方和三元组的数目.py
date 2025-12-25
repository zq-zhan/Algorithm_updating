from math import isqrt

class Solution:
	def countTriples(self, n):
		ans = 0
		for i in range(1, n):
			for j in range(i + 1, n):
				x = i ** 2 + j ** 2
				if x <= n ** 2 and isqrt(x) ** 2 == x:
					ans += 2
				elif x > n ** 2:
					break
		return ans
	
if __name__ == '__main__':
	n = 5
	print(Solution().countTriples(n))