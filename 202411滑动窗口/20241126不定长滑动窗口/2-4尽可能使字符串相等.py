# 4、尽可能使字符串相等
class Solution1:
	def equalSubstring(self, s, t, maxCost):
		ans = left = 0
		for right, c in enumerate(s):
			maxCost -= abs(ord(s[right]) - ord(t[right]))
			while maxCost < 0:
				maxCost += abs(ord(s[left]) - ord(t[left]))
				left += 1
			ans = max(ans, right - left + 1)
		return ans