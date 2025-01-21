# 5.回旋镖的数量
from collections import defaultdict


class Solution1:
	def numberOfBoomerangs(self, points):
		ans = 0
		for i, point1 in enumerate(points):
			cnt = defaultdict(int)
			for j, point2 in enumerate(points):
				dis = (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2
				ans += cnt[dis] * 2
				cnt[dis] += 1
		return ans



if __name__ == '__main__':
    points = [[0,0],[1,0],[2,0]]
    s = Solution1()
    print(s.numberOfBoomerangs(points))