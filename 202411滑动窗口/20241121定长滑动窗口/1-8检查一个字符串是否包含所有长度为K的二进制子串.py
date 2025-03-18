# 5.检查一个字符串是否包含所有长度为K的二进制子串
class Solution1:
	def hasAllCodes(sefl, s, k):
		set_win = set()
		temp_win = ''
		for left, x in enumerate(s):
			temp_win += x
			if left >= k - 1:
				set_win.add(temp_win)
				temp_win = temp_win[1:]
		if len(set_win) == 2 ** k:
			return True
		else:
			return False
		
if __name__ == '__main__':
	s = "00110110"
	k = 2
	print(Solution1().hasAllCodes(s, k))