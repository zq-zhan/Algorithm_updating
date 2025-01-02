# 13.统计同质子字符串的数目
class Solution1:
	def countHomogenous(self,s):
		ans = i = 0
		n = len(s)
		while i < n:
			start = i
			i += 1
			while i < n and s[i] == s[i - 1]:
				i += 1
			ans += (i - start) * (i - start + 1) // 2
		return ans % (10 ** 9 + 7) 