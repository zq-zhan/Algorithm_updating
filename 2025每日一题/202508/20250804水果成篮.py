from functools import cache

class Solution:
	def totalFruit(self, fruits):
		n = len(fruits)
		path = set()
		# ans = 0
		@cache
		def dfs(i, pre1, pre2):
			if i < 0:
				return 0
			ori1 = pre1
			ori2 = pre2
			x = fruits[i]
			if pre1 != -1 and pre2 != -1 and x != pre1 != pre2:
				return 0
			if pre1 == -1:
				pre1 = x
			elif pre2 == -1:
				pre2 = x
			return max(dfs(i - 1, pre1, pre2) + 1, dfs(i - 1, ori1, ori2))
		return dfs(n - 1, -1, -1)	
	
if __name__ == '__main__':
	fruits = [1,2,1]
	print(Solution().totalFruit(fruits))
	