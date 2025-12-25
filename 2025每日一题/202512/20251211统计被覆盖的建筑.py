from collections import defaultdict

class Solution:
	def countCoveredBuildings(self, n, buildings):
		ans = 0
		mat = [[0] * n for _ in range(n)]
		for x, y in buildings:
			mat[x - 1][y - 1] = 1

		for x, y in buildings:
			if sum(mat[:][y - 1]) >= 3 and sum(mat[x - 1][:]) >= 3:
				ans += 1
		return ans

class Solution:
	def countCoveredBuildings(self, n, buildings):
		same_y_dic = defaultdict(list)
		buildings.sort()
		for x, y in buildings:
			same_y_dic[y].append((x, y))

		same_x_dic = defaultdict(list)
		buildings.sort(key = lambda x:x[1])
		for x, y in buildings:
			same_x_dic[x].append((x, y))

		ans = 0
		for y, lis in same_y_dic.items():
			if len(lis) >= 3:
				for x1, y1 in lis[1:-1]:
					same_x = set(same_x_dic[x1][1:-1])
					if (x1, y1) in same_x:
						ans += 1
		return ans

if __name__ == '__main__':
	n = 3
	buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]]
	print(Solution().countCoveredBuildings(n, buildings))