# 2.删除字符串中所有相邻重复项
class Solution1:
	def removeDuplicates(self, s):
		st = []
		for x in s:
			if st and x == st[-1]:
				st.pop()
			else:
				st.append(x)
		return ''.join(st)
	
if __name__ == '__main__':
	s = 'abbaca'
	print(Solution1().removeDuplicates(s))