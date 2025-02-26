# 3.基本计算器
class Solution1:
	def calculate(self, s):
		st = []
		temp_cal = ''
		for x in s:
			if x not in '+-*/':
				# st.append(x)
				if temp_cal == '*':
					st.append(int(st.pop()) * int(x))
				elif temp_cal == '/':
					st.append(int(st.pop()) / int(x))
				elif temp_cal == '+':
					st.append(x)
				elif temp_cal == '-':
					st.append(-int(x))
				else:
					st.append(x)
			else:
				temp_cal = x
		ans = 0
		for x in st:
			if int(x):
				ans += int(x)

		return ans
	
## 
class Solution(object):
    def calculate(self, s):
        res, num, sign = 0, 0, 1
        stack = []
        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)
            elif c == "+" or c == "-":
                res += sign * num
                num = 0
                sign = 1 if c == "+" else -1
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ")":
                res += sign * num
                num = 0
                res *= stack.pop()
                res += stack.pop()
        res += sign * num
        return res
	
if __name__ == '__main__':
	s = '2-1+(2*3-5)'
	print(Solution().calculate(s))