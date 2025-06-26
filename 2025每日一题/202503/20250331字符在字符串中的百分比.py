# 20250331字符在字符串中的百分比
class Solution1:
	def percentageLetter(self, s, letter):
		ans = 0
		for x in s:
			ans += 1 if x == letter else 0
		return ans * 100 // len(s)
	
if __name__ == '__main__':
	s = 'foobar'
	letter = 'o'
	print(Solution1().percentageLetter(s, letter)) # Output: 33