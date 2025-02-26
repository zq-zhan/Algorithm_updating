# 1.逆波兰表达式求值
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

# 2.笨阶乘
class Solution1:
	def clumsy(self, n):
		num_lis = [i for i in range(n, 0, -1)]
		st = []
		ans = 0
		for i, c in enumerate(num_lis):
			if (i + 1) % 4 == 0:
				ans += c
			else:
				st.append(c)

			if len(st) < 3:
				continue
			else:
				temp_result = int(st[-3] * st[-2] / st[-1])
				if ans == 0:
					ans += temp_result
				else:
					ans -= temp_result
				st = []

		# temp_result = 1
		# for x in st:
		# 	temp_result *= x

		# if len(st) == 1:
		# 	ans -= 1
		# elif len(st) == 2:
		# 	ans -= 2
		if n < 3:
			return len(st)
		else:
			return ans - len(st)
## 思路二：优化 
class Solution2:
	def clumsy(self, n):
		cnt = 0
		st = [n]
		for i in range(n - 1, 0, -1):
			if cnt % 4 == 0:
				st.append(st.pop() * i)
			elif cnt % 4 == 1:
				st.append(int(st.pop() / i))
			elif cnt % 4== 2:
				st.append(i)
			elif cnt % 4== 3:
				st.append(-i)
			cnt += 1
		return sum(st)

# 3.基本计算器
class Solution1:  # 错解
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
				elif temp_cal in '()':
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
## 递归
class Solution2:
	def calculate(self, s):
		s = s.replace(' ','')
		s = s.replace(')','+)') + '+'

		def dfs(i):
			st = []
			pre_sign = '+'
			num = 0
			j = i
			while j < len(s):
				c = s[j]
				if c.isdigit():
					num = 

