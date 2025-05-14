class Solution1:
	def longestSemiRepetitiveSubstring(self, s):
		ans = 1
		left = cnt = 0
		n = len(s)
		for right in range(1, n):
			if s[right] == s[right - 1]:
				cnt += 1
			while cnt > 1:
				if s[left] == s[left + 1]:
					cnt -= 1
				left += 1
			ans = max(ans, right - left + 1)
		return ans
	
if __name__ == '__main__':
	s = '11'
	print(Solution1().longestSemiRepetitiveSubstring(s))