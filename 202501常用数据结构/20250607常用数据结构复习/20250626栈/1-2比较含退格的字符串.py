class Solution1:
	def backspaceCompare(self,s,t):
		n = len(s)
		m = len(t)
		p1, p2 = n-1 ,m-1
		cnt1 = 0
		cnt2 = 0
		while p1 >= 0 or p2 >= 0:
			while p1 >= 0:
				if s[p1] == '#':
					cnt1 += 1
					p1 -= 1
				elif cnt1 > 0:
					cnt1 -= 1
					p1 -= 1
				else:
					break
			while p2 >= 0:
				if t[p2] == '#':
					cnt2 += 1
					p2 -= 1
				elif cnt2 > 0:
					cnt2 -= 1
					p2 -= 1
				else:
					break
			if p1 >= 0 and p2 >= 0:
				if s[p1] != t[p2]:
					return False
			elif p1 >=0 or p2 >= 0:
				return False
			p1 -= 1
			p2 -= 1
		return True
	
## 栈解法
class Solution:
	def backspaceCompare(self, s, t):
		def trans(substr):
			s_lis = []
			for x in substr:
				if x != '#':
					s_lis.append(x)
				elif len(s_lis):
					s_lis.pop()
			return s_lis
		return trans(s) == trans(t)
	
if __name__ == '__main__':
	s = "ab##"
	t = "c#d#"
	print(Solution1().backspaceCompare(s, t))