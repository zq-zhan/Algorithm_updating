# 3.最长的字母序连续子字符串的长度
class Soluton1:
	def longestContinuousSubstring(self,s):
		ans = 1
		left, right = 0, 1
		while right < len(s):
			temp_chr = s[right-1]
			next_chr = chr(ord(temp_chr) + 1)
			if s[right] != next_chr:
				ans = max(ans, right - left)
				left = right
			right += 1
		return max(ans, right - left)
	
if __name__ == '__main__':
	s = 'abacaba'
	cls = Soluton1()
	print(cls.longestContinuousSubstring(s))