class Solution:
	def letterCombinations(self, digits):
		n = len(digits)
		if n == 0:
			return []

		mapping = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
		ans = []
		path = [''] * n
		def dfs(i):
			if i == n:
				ans.append(''.join(path))
				return 
			for c in mapping[int(digits[i])]:
				path[i] = c
				dfs(i + 1)
		dfs(0)
		return ans
	
if __name__ == '__main__':
	digits = '23'
	print(Solution().letterCombinations(digits))