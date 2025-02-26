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

if __name__ == '__main__':
	s = ""
	print(Solution1().removeOuterParentheses(s))