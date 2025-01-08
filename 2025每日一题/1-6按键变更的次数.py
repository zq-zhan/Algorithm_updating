# 6.按键变更的次数
class Solution1:
	def countKeyChanges(self, s):
		ans = 0
		n = len(s)
		for i in range(1, n):
			if s[i].lower() == s[i - 1].lower():
				continue
			ans += 1
		return ans

if __name__ == '__main__':
	s ='aAbBcC'
	cls = Solution1()
	print(cls.countKeyChanges(s))