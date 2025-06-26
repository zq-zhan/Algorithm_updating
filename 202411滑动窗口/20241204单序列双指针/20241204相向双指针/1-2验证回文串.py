class Solution1:
	def isPalindrome(self, s):
		ori_s = []
		for x in s:
			if x.isalpha():
				ori_s.append(x.lower())
		n = len(ori_s)
		temp_s = ori_s.copy()
		left, right = 0, n - 1
		while left < right:
			temp_char = ori_s[left]
			ori_s[left] = ori_s[right]
			ori_s[right] = temp_char
			left += 1
			right -= 1
		return temp_s == ori_s

class Solution2:
	def isPalindrome(self, s):
		left, right = 0, len(s) - 1
		while left < right:
			while left < right and not s[left].isalnum():
				left += 1
			while left < right and not s[right].isalnum():
				right -= 1
			if s[left].lower() != s[right].lower():
				return False
			left += 1
			right -= 1
		return True

class Solution3:
	def isPalindrome(self, s):
		left, right = 0, len(s) - 1
		while left < right:
			while not s[left].isalpha():
				left += 1
			while not s[right].isalpha():
				right -= 1
			if s[left].lower() != s[right].lower():
				return False
			left += 1
			right -= 1
		return True


if __name__ == '__main__':
	s = '.,'
	print(Solution3().isPalindrome(s))