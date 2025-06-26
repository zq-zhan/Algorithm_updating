from math import inf

# 20250503行相等的最少多米诺旋转
class Solution1:
	def minDominoRotations(self, tops, bottoms):
		ans = inf
		n = len(tops)
		for target in (tops[0], bottoms[0]):
			cnt_top = cnt_bottom = 0
			tag = True
			for i in range(n):
				if tops[i] == target and bottoms[i] == target:
					continue
				elif tops[i] != target and bottoms[i] != target:
					tag = False
					break
				elif tops[i] != target:
					cnt_top += 1
				elif bottoms[i] != target:
					cnt_bottom += 1

			if tag:
				ans = min(ans, cnt_top, cnt_bottom)
		return ans if ans < inf else -1

	
if __name__ == '__main__':
	tops = [2,1,2,4,2,2]
	bottoms = [5,2,6,2,3,2]
	print(Solution1().minDominoRotations(tops, bottoms)) # Output: 2
