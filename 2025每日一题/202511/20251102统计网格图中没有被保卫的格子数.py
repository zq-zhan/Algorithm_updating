## 灵神题解
DIRS = (0, -1), (0, 1), (-1, 0), (1, 0)
class Solution:
	def countUnguarded(self, m, n, guards, walls):
		guarded = [[0] * n for _ in range(m)]

		for x, y in guards:
			guarded[x][y] = -1
		for x, y in walls:
			guarded[x][y] = -1

		# 遍历警卫
		for x0, y0 in guards:
			for dx, dy in DIRS:
				x, y = x0 + dx, y0 + dy
				while 0 <= x < m and 0 <= y < n and guarded[x][y] != -1:
					guarded[x][y] = 1 # 被保卫
					x += dx
					y += dy

		return sum(row.count(0) for row in guarded)

if __name__ == '__main__':
	m = 4
	n = 6
	guards = [[0,0],[1,1],[2,3]]
	walls = [[0,1],[2,2],[1,4]]
	print(Solution().countUnguarded(m, n, guards, walls)) # 7