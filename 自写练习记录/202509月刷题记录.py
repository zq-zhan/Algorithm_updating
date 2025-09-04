# 1.20250901最大平均通过率
class Solution:
	def maxAverageRatio(self, classes, extraStudents):
		h = [((a - b)/(b * (b + 1)), a, b) for a, b in classes]
		heap.heapify(h)
		for _ in range(extraStudents):
			_, a, b = h[0]
			a += 1
			b += 1
			heap.heapreplace(h, ((a - b)/(b * (b + 1)), a, b))
		return sum(a / b for _, a, b in h) / len(h)

# 2.20250902人员站位的方案数1
class Solution:
	def numberOfPairs(self, points):
		points.sort(key = lambda x: (x[0], -x[1]))
		n = len(points)
		ans = 0
		for i, (x, y) in enumerate(points):
			pre_min_y = inf
			for j in range(i - 1, -1, -1):
				x1, y1 = points[j]
				if x1 <= x and y <= y1 < pre_min_y:
					pre_min_y = min(y1, pre_min_y)
					ans += 1
		return ans
	
# 3.20250903人员站位的方案数2
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
				if y1 == pre_min_y:
					break
		return ans


