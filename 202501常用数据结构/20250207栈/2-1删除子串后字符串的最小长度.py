# 1.删除子串后字符串的最小长度
class Solution1:
	def minLength(self, s):
		st = []
		for x in s:
			if st and ((st[-1] == 'A' and x == 'B') or (st[-1] == 'C' and x == 'D')):
				st.pop()
			else:
				st.append(x)
		return len(st)

class Solution2:
	def minLength(self, s):
		st = [0]
		for x in s:
			if (st[-1] == 'A' and x == 'B') or (st[-1] == 'C' and x == 'D'):
				st.pop()
			else:
				st.append(x)
		return len(st) - 1

if __name__ == '__main__':
	s = 'ABFCACDB'
	sol = Solution2()
	print(sol.minLength(s))