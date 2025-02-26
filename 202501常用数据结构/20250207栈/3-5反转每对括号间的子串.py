# 5.反转每对括号间的子串
class Solution1:
    def reverseParentheses(self, s):
        stack = []
        for c in s:
            if c != ')':
                stack.append(c)
            elif c == ')':
                tmp = []
                # 注意stack不为空才可以读取栈顶
                while stack and stack[-1] != '(':
                    tmp.append(stack.pop())
                if stack:
                    stack.pop() # 将左括号抛出
                stack += tmp
        return "".join(stack)
    
class Solution2:
	def reverseParentheses(self, s):
		st = []
		for x in s:
			if x != ')':
				st.append(x)
			else:
				temp_lis = []
				while st and st[-1] != '(':
					temp_lis.append(st.pop())
				if st:
					st.pop()  # 移除左括号
				st.extend(temp_lis)
		return ''.join(st)
	
if __name__ == '__main__':
	s = "(ed(et(oc))el)"
	print(Solution2().reverseParentheses(s))