class Solution:
	def calPoints(self, ops):
		def check(num):
			try:
				float(num)
				return True
			except ValueError:
				return False
		ans = []
		for x in opt:
			if check(x):
				ans.append(int(x))
			elif x == '+':
				ans.append(ans[-1] + ans[-2])
			elif x == 'D':
				ans.append(ans[-1] * 2)
			else:
				ans.pop()
		return sum(ans)

	
if __name__ == '__main__':
	opt = ["5","-2","4","C","D","9","+","+"]
	s = Solution()
	print(s.calPoints(opt))