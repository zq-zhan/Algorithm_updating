class Solution:
	def numberOfBeams(self, bank):
		ans = pre = 0
		for x in bank:
			cnt = x.count('1')
			ans += pre * cnt
			if cnt > 0:
				pre = cnt
		return ans
	
if __name__ == '__main__':
	bank = ['011001', '000000', '010100', '001000']
	print(Solution().numberOfBeams(bank))