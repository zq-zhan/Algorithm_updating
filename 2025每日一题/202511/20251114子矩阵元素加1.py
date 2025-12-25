class Solution:
	def rangeAddQueries(self, n, queries):
		mat = [[0] * n for _ in range(n)]
		for x1, y1, x2, y2 in queries:
			for i in range(x1, x2 + 1):
				for j in range(y1, y2 + 1):
					mat[i][j] += 1
		return mat
	
## 灵神题解——二维差分
class Solution:
	def rangeAddQueries(self, n, queries):
		diff = [[0] * (n + 2) for _ in range(n + 2)]
		for x1, y1, x2, y2 in queries:
			diff[x1 + 1][y1 + 1] += 1
			diff[x1 + 1][y2 + 2] -= 1
			diff[x2 + 2][y1 + 1] -= 1
			diff[x2 + 2][y2 + 2] += 1

		ans = [[0] * n for _ in range(n)]
		for i in range(n):
			for j in range(n):
				diff[i + 1][j + 1] += diff[i + 1][j] + diff[i][j + 1] - diff[i][j]
				ans[i][j] = diff[i + 1][j + 1]
		return ans

if __name__ == '__main__':
	n = 3
	queries = [[1,1,2,2],[0,0,1,1]]
	print(Solution().rangeAddQueries(n, queries))