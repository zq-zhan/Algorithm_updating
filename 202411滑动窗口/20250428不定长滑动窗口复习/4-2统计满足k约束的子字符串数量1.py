class Solution1:
	def countKConstraintSubstrings(self, s, k):
		cnt_0 = cnt_1 = ans = left = 0
		for right, c in enumerate(s):
			if c == '0':
				cnt_0 += 1
			else:
				cnt_1 += 1
			while cnt_0 > k and cnt_1 > k:
				if s[left] == '0':
					cnt_0 -= 1
				else:
					cnt_1 -= 1
				left += 1
			ans += right - left + 1
		return ans
	
if __name__ == '__main__':
	s = "10101"
	k = 1
	print(Solution1().countKConstraintSubstrings(s, k))