class Solution:
	def areaOfMaxDiagonal(self, dimensions):
		ans = length = 0
		for x, y in dimensions:
			dig = x ** 2 + y ** 2
			if dig > length:
				length = dig
				ans = x * y
			elif dig == length:
				ans = max(ans, x * y)
		return ans
	
if __name__ == '__main__':
	dimensions = [[6,5],[8,6],[2,10],[8,1],[9,2],[3,5],[3,5]]
	print(Solution().areaOfMaxDiagonal(dimensions))