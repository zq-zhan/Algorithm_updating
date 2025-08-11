class Solution:
	def generate(self, numRows):
		ans = [[1]]
		for i in range(2, numRows + 1):
			path = [0] * i
			for j in range(0, i):
				if j == 0:
					path[j] = ans[-1][0]
				elif j == i - 1:
					path[j] = ans[-1][-1]
				else:
					path[j] = ans[-1][j - 1] + ans[-1][j]
			ans.append(path)
		return ans
	
## 灵神题解
class Solution:
	def generate(self, numRows):
		ans = [[1] * (i + 1) for i in range(numRows)]
		for i in range(2, numRows):
			for j in range(1, i):
				ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]
		return ans
	
if __name__ == '__main__':
	numRows = 5
	print(Solution().generate(numRows))