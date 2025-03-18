# 相向双指针
# 1.反转字符串
class Solution1:
	def reverseString(self, s):
		left, right = 0, len(s) - 1
		while left < right:
			temp = s[left]
			s[left] = s[right]
			s[right] = temp
			left += 1
			right -= 1
		return s

class Solution2:
	def reverseString(self, s):
		n = len(s)
		left, right = 0, n - 1
		while left < right:
			temp_s = s[left]
			s[left] = s[right]
			s[right] = temp_s
			left += 1
			right -= 1
		return s

if __name__ == '__main__':
	s = "hello"
	cls = Solution2()
	print(cls.reverseString(list(s)))