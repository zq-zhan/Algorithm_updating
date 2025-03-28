from bisect import bisect_right

class Solution1:
	def asteroidsDestroyed(self, mass, asteroids):
		# n = len(asteroids)
		asteroids.sort()
		while len(asteroids) > 0:
			i = bisect_right(asteroids, mass) - 1
			if i < 0:
				return False
			mass += asteroids[i]
			asteroids.pop(i)
		return True
	
## 优化
class Solution2:
	def asteroidsDestroyed(self, mass, asteroids):
		# n = len(asteroids)
		asteroids.sort()
		for x in asteroids:
			if mass >= x:
				mass += x
			else:
				return False
		return True
	
if __name__ == '__main__':
	mass = 10
	asteroids = [3,9,19,5,21]
	print(Solution1().asteroidsDestroyed(mass, asteroids))