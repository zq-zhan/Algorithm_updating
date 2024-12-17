# 11.比较含退格的字符串
class Solution1:  # 错解
	def backspaceCompare(self,s,t):
		s = list(s)
		t = list(t)
		n = len(s)
		m = len(t)
		p1, p2 = n-1 ,m-1
		while p1 > 0:
			while p1 >= 0 and s[p1] != '#':
				p1 -= 1
				continue
			cnt = 0
			while p1 >= 0 and s[p1] == '#':
				cnt += 1
				s[p1] = ''
				p1 -= 1
			s[p1-cnt+1:p1+1]=['']*cnt
		while p2 > 0:
			while p2 >= 0 and t[p2] != '#':
				p2 -= 1
				continue
			cnt = 0
			while p2 >= 0 and t[p2] == '#':
				cnt += 1
				t[p2] = ''
				p2 -= 1
			t[p2-cnt+1:p2+1]=['']*cnt
		return s==t
class Solution2:
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


if __name__ == '__main__':
	s = "a##c"
	t = "#a#c"
	cls = Solution1()
	print(cls.backspaceCompare(s,t))