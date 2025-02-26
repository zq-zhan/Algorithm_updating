# 4.检查替换后的词是否有效
class Solution1:
	def isValid(self, s):
		st = [0, 0]
		for x in s:
			if st[-2] == 'a' and st[-1] == 'b' and x == 'c':
				for i in range(2):
					st.pop()
			else:
				st.append(x)
		return len(st) == 2
	
if __name__ == '__main__':
	s = 'aabcbc'
	print(Solution1().isValid(s))