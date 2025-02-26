# 3.整理字符串
class Solution1:
	def makeGood(self, s):
		st = []
		for x in s:
			tag_x = 1 if x.isupper() else -1
			if st:
				if st[-1].isupper():
					tag_st = 1
				else:
					tag_st = -1
			if st and tag_x * tag_st == -1 and x.lower() == st[-1].lower():
				st.pop()
			else:
				st.append(x)
		return ''.join(st)
	
## 优化
class Solution2:
	def makeGood(self, s):
		st = []
		for x in s:
			if st and abs(ord(x) - ord(st[-1])) == ord('a') - ord('A'):
				st.pop()
			else:
				st.append(x)
		return ''.join(st)
	
if __name__ == '__main__':
	s = "leEeetcode"
	# s = "abBAcC"
	print(Solution2().makeGood(s))