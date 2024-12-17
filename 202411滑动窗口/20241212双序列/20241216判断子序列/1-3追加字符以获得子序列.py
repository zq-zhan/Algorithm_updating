# 3.追加字符以获得子序列
class Solution1:
	def appendCharacters(self,s,t):
		p1 = p2 = 0
		n, m = len(s),len(t)
		while p1 < n and p2 < m:
			if s[p1] != t[p2]:
				p1 += 1
			else:
				p1 += 1
				p2 += 1
		return m - p2 

if __name__ == '__main__':
	s = "abc"
	t = "ahbgdc"
	print(Solution1().appendCharacters(s,t))
	char_lis=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']