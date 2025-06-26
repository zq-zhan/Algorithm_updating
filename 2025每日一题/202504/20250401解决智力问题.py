from functools import cache

class Solution1:
	def mostPoints(self, questions):
		n = len(questions)
		@cache
		def dfs(i):
			if i >= n:
				return 0
			return max(dfs(i + 1), dfs(i + questions[i][1] + 1) + questions[i][0])
		return dfs(0)
	
## 递推写法
class Solution2:
	def mostPoints(self, questions):
		n = len(questions)
		f = [0] * (n + 1)
		for i in range(n - 1, -1, -1):
			j = min(i + questions[i][1] + 1, n)
			f[i] = max(f[i + 1], f[j] + questions[i][0])
		return f[0]
		

if __name__ == '__main__':
    questions = [[3,2], [4,3], [4,4], [2,5]]
    s = Solution2()
    print(s.mostPoints(questions))