# 3.棒球比赛
class Solution1:
	def calPoints(self, ops):
		ans = []
		for x in ops:
			if x == 'C':
				ans.pop()
			elif x == 'D':
				ans.append(ans[-1] * 2)
			elif x == '+':
				ans.append(ans[-1] + ans[-2])
			else:
				ans.append(int(x))
		return sum(ans)
	
if __name__ == '__main__':
	cls = Solution1()
	print(cls.calPoints(['5', '2', 'C', 'D', '+'])) # 30