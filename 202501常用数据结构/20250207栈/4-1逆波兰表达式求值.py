class Solution1:
	def evalRPN(self, tokens):
		st = []
		for x in tokens:
			# st = []
			# ans = 0
			if x not in '+-*/':
				st.append(x)
			else:
				x2 = st.pop()
				x1 = st.pop()
				if x == '+':
					st.append(int(x1) + int(x2))
				elif x == '-':
					st.append(int(x1) - int(x2))
				elif x == '*':
					st.append(int(x1) * int(x2))
				else:
					st.append(int(x1) / int(x2))
		return int(st[-1])

if __name__ == '__main__':
	tokens = ["18"]
	s = Solution1()
	print(s.evalRPN(tokens))