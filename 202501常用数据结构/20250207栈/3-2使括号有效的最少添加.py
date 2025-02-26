# 2.使括号有效的最少添加
class Solution1:
	def minAddToMakeValid(self, s):
		st = []
		# ans = 0
		for x in s:
			if x == '(':
				st.append(x)
			else:
				if st and st[-1] == '(':
					st.pop()
				else:
					st.append(x)
					# ans += 1
		return len(st)
	
if __name__ == '__main__':
	s = ')))'
	print(Solution1().minAddToMakeValid(s)) # 1