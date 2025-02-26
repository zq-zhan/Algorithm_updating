# 2.比较含退格的字符串
class Solution1:
	def backspaceCompare(self, s, t):
		new_s = []
		for x in s:
			# new_s += x
			if x == '#':
				if new_s:
					new_s.pop()
			else:
				new_s += x

		new_t = []
		for c in t:
			# new_t += c
			if c == '#':
				if new_t:
					new_t.pop()
			else:
				new_t += c

		return new_s == new_t
	

## 方法二：双指针
class Solution2:
	def backspaceCompare(self, s, t):
		s = list(s)
		t = list(t)
		p1, p2 = len(s) - 1, len(t) - 1

		while p1 >= 0 and p2 >= 0:
			cnt1 = cnt2 = 0
			while s[p1] == '#':
				cnt1 += 1
				p1 -= 1
			while t[p2] == '#':
				cnt2 += 1
				p2 -= 1

			if cnt1 > 0:
				if p1 - cnt1 >= 0:
					temp_s = s[p1 - cnt1]
					p1 -= cnt1 + 1
				else:
					p1 -= cnt1
			else:
				temp_s = s[p1]
				p1 -= 1

			if cnt2 > 0:
				if p2 - cnt2 >= 0:
					temp_t = t[p2 - cnt2]
					p2 -= cnt2 + 1
				else:
					p2 -= cnt1
			else:
				temp_t = t[p2]
				p2 -= 1

			if p1 >= 0 and p2 >= 0:
				if temp_s != temp_t:
					return False
				# else:
				# 	continue
			elif p1 < 0 and p2 < 0:
				continue
			else:
				return False

		return True


	
if __name__ == '__main__':
	s = "ab#c"
	t = "ad#c"
	cls = Solution2()
	print(cls.backspaceCompare(s, t))