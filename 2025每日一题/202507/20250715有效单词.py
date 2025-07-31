class Solution:
	def isValid(self, word):
		cnt1 = cnt2 = 0   # 记录元音字母个数
		if len(word) < 3:
			return False
		for x in word:
			if not x.isdigit() and not x.isalpha():
				return False
			if x.isalpha():
				if x in 'aeiouAEIOU':
					cnt1 += 1
				else:
					cnt2 += 1
		return True if cnt1 > 0 and cnt2 > 0 else False
	
if __name__ == '__main__':
	word = "234Adas"
	print(Solution().isValid(word))