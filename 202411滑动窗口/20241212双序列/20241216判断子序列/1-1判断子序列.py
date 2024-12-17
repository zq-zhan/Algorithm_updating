# 1.判断子序列
class Solution1:
	def isSubsequence(self,s,t):
		p1 = p2 = 0
		n, m = len(s), len(t)
		while p1 < n and p2 < m:
			if t[p2]!=s[p1]:
				p2 += 1
			else:
				p1 += 1
				p2 += 1
		return True if p1 == n else False
	
if __name__ == '__main__':
	s = "abc"
	t = "ahbgdc"
	print(Solution1().isSubsequence(s,t))