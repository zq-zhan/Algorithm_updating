# 6.删除字符串中的所有相邻重复项2
class Solution1:
	def removeDuplicates(self, s, k):
		st = []
		# cnt = 1
		for x in s:
			if len(st) >= k - 1:
				temp_str = ''.join(st[-(k - 1):])
				if temp_str == x * (k - 1):
					for i in range(k - 1):
						st.pop()
				else:
					st.append(x)
			else:
				st.append(x)
		return ''.join(st)
## 二维数组
class Solution2:
	def removeDuplicates(self, s, k):
		# n = len(s)
		st = []
		for c in s:
			if not st or st[-1][0] != c:
				st.append([c, 1])
			elif st[-1][1] + 1 < k:
				st[-1][1] += 1
			else:
				st.pop()
		ans = ''
		for c, l in st:
			ans += c * l
		return ans
	

	
if __name__ == '__main__':
	s = "deeedbbcccbdaa"
	k = 3
	print(Solution2().removeDuplicates(s, k))