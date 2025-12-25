from collections import defaultdict, Counter

class Solution:
	def countTrapezoids(self, points):
		MOD = 10 ** 9 + 7
		temp_dic = defaultdict(int)
		n = len(points)
		ans = 0
		for i in range(n):
			x1, y1 = points[i]
			for j in range(i, n):
				x2, y2 = points[j]
				if x1 != x2:
					k = (y2 - y1) / (x2 - x1)
					ans = (ans + temp_dic[k]) % MOD
					ans = (ans + temp_dic[-k]) % MOD
					temp_dic[k] += 1
					temp_dic[-k] += 1
		return ans
	
## 灵神题解
class Solution:
	def countTrapezoids(self, points):
		MOD = 10 ** 9 + 7
		cnt = Counter(p[1] for p in points)
		ans = s = 0
		for c in cnt.values():
			k = c * (c - 1) // 2
			ans += s * k
			s += k
		return ans % MOD

if __name__ == '__main__':
	points = [[0,0],[1,0],[0,1],[2,1]]
	print(Solution().countTrapezoids(points))