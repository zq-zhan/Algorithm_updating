from collections import defaultdict

class Solution1:
	def maxPointsInsideSquare(self, points, s):
		ans = 0
		def check(target):
			temp_ans = 0
			for _, value in dic_win.items():
				cnt = 0
				for x, y in value:
					if abs(x) <= target and abs(y) <= target:
						cnt += 1
						if cnt > 1:
							return False
				if cnt == 1:
					temp_ans += 1
			nonlocal ans
			ans = max(ans, temp_ans)
			return True


		mx_right = mn_right = 0
		dic_win = defaultdict(list)
		for i, x in enumerate(s):
			dic_win[x].append(points[i])
			mx_right = max(mx_right, points[i][0], points[i][1])
			mn_right = min(mn_right, points[i][0], points[i][1])

		left, right = -1, (mx_right - mn_right + 1)
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				left = mid
			else:
				right = mid
		return ans
	
if __name__ == '__main__':
	points = [[0,1],[0,0]]
	s = "aa"
	print(Solution1().maxPointsInsideSquare(points, s))