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
	
if __name__ == '__main__':
	s = "(1+(2*3)+((8)/4))+1"
	print(Solution1().maxDepth(s))