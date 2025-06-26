class Solution1:
	def numberOfSubstrings(self, s):
		dic_win = {'a':0, 'b':0, 'c':0}
		ans = left = 0
		for right, c in enumerate(s):
			dic_win[c] += 1
			while min(dic_win.values()) > 0:
				dic_win[s[left]] -= 1
				left += 1
			ans += left
		return ans
	
if __name__ == '__main__':
	s = 'abcabc'
	print(Solution1().numberOfSubstrings(s))