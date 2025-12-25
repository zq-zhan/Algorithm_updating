class Solution:
	def countPalindromicSubsequence(self, s):
		ans = set()
		left, right = 0, len(s) - 1
		while left < right - 1:
			if s[left] == s[right]:
				for x in s[left + 1:right]:
					ans.add(s[left] + x + s[right])
			left += 1
		return len(ans)

if __name__ == '__main__':
	s = "bbcbaba"
	print(Solution().countPalindromicSubsequence(s))