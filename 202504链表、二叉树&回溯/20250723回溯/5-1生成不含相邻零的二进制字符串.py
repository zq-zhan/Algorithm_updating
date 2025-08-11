class Solution:
	def validStrings(self, n):
		ans = []
		path = []
		def dfs(i):
			if i == n:
				if not path[-1] == path[-2] == '0':
					ans.append(''.join(path))
				return

			if len(path) >= 2 and path[-1] == path[-2] == '0':
				return

			path.append('1')  
			dfs(i + 1)
			path.pop()

			path.append('0')
			dfs(i + 1)
			path.pop()
		dfs(0)
		return ans
	
if __name__ == '__main__':
	n = 3
	print(Solution().validStrings(n))