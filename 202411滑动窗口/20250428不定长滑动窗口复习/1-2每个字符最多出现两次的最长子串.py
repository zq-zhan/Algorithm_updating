from collections import defaultdict

class Solution1:
	def maximumLengthSubstring(self, s):
		ans = left = 0
		dic_win = defaultdict(int)
		for right, c in enumerate(s):
			dic_win[c] += 1
			while dic_win[c] > 2:
				if dic_win[s[left]] == 1:
					del dic_win[s[left]]
				else:
					dic_win[s[left]] -= 1
				left += 1
			ans = max(ans, right - left + 1)
		return ans
	
if __name__ == '__main__':
	s = 'bcbbbcba'
	print(Solution1().maximumLengthSubstring(s))