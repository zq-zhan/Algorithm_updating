# 20251116仅含1的子串数
class Solution:
	def numSub(self, s):
		MOD = 10 ** 9 + 7
		ans = 0
		left = 0
		s += '0'
		for right, x in enumerate(s):
			if x == 0:
				ans += (right - left) * (right - left + 1) // 2
				left = right + 1
		return ans % MOD
	
if __name__ == '__main__':
	s = ''