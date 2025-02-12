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
## 优化 利用哨兵减少判断条件
class Solution1:
	def minLength(self, s):
		st = [0]
		for x in s:
			if (st[-1] == 'A' and x == 'B') or (st[-1] == 'C' and x == 'D'):
				st.pop()
			else:
				st.append(x)
		return len(st) - 1