# 12. 字母移位2
from itertools import accumulate

class Solution1:
	def shiftingLetters(self, s, shifts):
		d = [0] * (len(s) + 1)
		for start, end, direction in shifts:
			if direction == 0:
				d[start] -= 1
				d[end + 1] += 1
			else:
				d[start] += 1
				d[end + 1] -= 1

		ans = list(accumulate(d))[:-1]
		ans_char = ''
		ord_a = ord('a')
		for i, c in enumerate(ans):
			ans_char += chr((ord(s[i]) - ord_a + c) % 26 + ord_a)
		return ans_char
	
if __name__ == '__main__':
	s = "abc"
	shifts = [[0, 1, 0], [1, 2, 1], [0, 2, 1]]
	print(Solution1().shiftingLetters(s, shifts))