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

if __name__ == '__main__':
	s = '('
	print(Solution1().isValid(s))