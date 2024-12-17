# 13.最小差
from cmath import inf


class Solution1:
	def smallestDifference(self,a,b):
		a.sort()
		b.sort()
		p1 = p2 = 0
		n, m = len(a), len(b)
		ans = inf
		while p1 < n and p2 < m:
			ans = min(ans,abs(a[p1]-b[p2]))
			if a[p1] - b[p2] < 0:
				p1 += 1
			else:
				p2 += 1
		return ans
	
if __name__ == '__main__':
	a = [1,3,15,11,2]
	b = [23,127,235,19,8]
	s = Solution1()
	print(s.smallestDifference(a,b))