# 4.从字符串中移除星号
class Solution1:
	def removeStars(self, s):
		ans = []
		for char in s:
			if char == '*':
				ans.pop()
			else:
				ans += char
		return ''.join(ans)
	
if __name__ == '__main__':
	s = 'leet**cod*e'
	cls = Solution1()
	print(cls.removeStars(s))