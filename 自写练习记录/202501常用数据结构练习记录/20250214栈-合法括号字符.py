# 1.有效的括号
class Solution1:
	def isValid(self, s):
		# ori_char = ['(', '[', '{']
		ori_dic = {'(':')', '[':']', '{':'}'}
		st = []
		for x in s:
			if x in ori_dic:
				st.append(x)
			else:
				if st:
					if ori_dic[st[-1]] != x:
						return False
					else:
						st.pop()
				else:
					return False
		return True and not st
## 灵神题解
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:  # s 长度必须是偶数
            return False
        mp = {'(': ')', '[': ']', '{': '}'}
        st = []
        for c in s:
            if c in mp:  # c 是左括号
                st.append(mp[c])  # 入栈对应的右括号
            elif not st or st.pop() != c:  # c 是右括号
                return False  # 没有左括号，或者左括号类型不对
        return not st  # 所有左括号必须匹配完毕

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

# 3. 删除最外层的括号
class Solution1:
	def removeOuterParentheses(self, s):
		ans = []
		cnt_left = 0
		cnt_right = 0
		for x in s:
			if cnt_left != 0:
				ans.append(x)
			cnt_left += 1 if x == '(' else 0
			cnt_right += 1 if x == ')' else 0
			if cnt_left != cnt_right:
				continue
			else:
				cnt_left = cnt_right = 0
				ans.pop()
		return ''.join(ans)

# 4.括号的最大嵌套深度
class Solution1:
	def maxDepth(self, s):
		ans = 0
		temp_deep = 0
		for x in s:
			if x == '(':
				temp_deep += 1
			elif x == ')':
				temp_deep -= 1
			ans = max(ans, temp_deep)
		return ans

# 5.反转每对括号间的子串
class Solution:
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
















