class Solution1:
	def minimumLength(self, s):
		n = len(s)
		left, right = 0, n - 1
		while left < right:
			if s[left] != s[right]:
				break
			while left + 1 < right and s[left] == s[left + 1]:
				left += 1
			while left < right - 1 and s[right] == s[right - 1]:
				right -= 1
			left += 1
			right -= 1
		return right - left + 1

if __name__ == '__main__':
	s = "aabccabba"
	print(Solution1().minimumLength(s))