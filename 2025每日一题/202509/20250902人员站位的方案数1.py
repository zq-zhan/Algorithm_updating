from math import inf

# class Solution:
# 	def numberOfPairs(self, points):
# 		points.sort(key = lambda x: (x[0], -x[1]))
# 		n = len(points)
# 		ans = 0
# 		for i, (x, y) in enumerate(points):
# 			pre_min_y = inf
# 			for j in range(i - 1, -1, -1):
# 				x1, y1 = points[j]
# 				if x1 <= x and y <= y1 < pre_min_y:
# 					pre_min_y = min(y1, pre_min_y)
# 					ans += 1
# 		return ans
	
class Solution:
	def numberOfPairs(self, points):
		points.sort(key = lambda x:(x[0], -x[1]), reverse = True)
		n = len(points)
		ans = 0
		for i, (x, y) in enumerate(points):
			pre_min_y = inf
			for j in range(i + 1, n):
				x1, y1 = points[j]
				if x1 <= x and y <= y1 < pre_min_y:
					ans += 1
					pre_min_y = min(pre_min_y, y1)
				if y == pre_min_y:
					break
		return ans
	

if __name__ == '__main__':
	points = [[0,3],[5,4],[6,2]]
	print(Solution().numberOfPairs(points))