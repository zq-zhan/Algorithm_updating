# 5、找到最长的半重复子字符串
# 5、找到最长的半重复子字符串
class Solution1:
	def longestSemiRepetitiveSubstring(self, s):
		ans = left = 0
		temp_cnt = 0
		for right in range(1, len(s)):
			if s[right] == s[right - 1]:
				temp_cnt += 1
			while temp_cnt > 1:
				if s[left] == s[left + 1]:
					temp_cnt -= 1
				left += 1
			if temp_cnt <= 1:
				ans = max(ans, right - left + 1)
		return ans
	
if __name__ == '__main__':
	s = "0"
	cls = Solution1()
	print(cls.longestSemiRepetitiveSubstring(s))