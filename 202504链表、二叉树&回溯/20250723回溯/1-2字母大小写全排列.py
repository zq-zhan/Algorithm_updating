class Solution:
	def letterCasePermutation(self, s):
		ans = set()
		path = []
		n = len(s)
		def dfs(i):
			if i == n:
				ans.add(''.join(path))
				return

			path.append(s[i])  # 不转换
			dfs(i + 1)
			if s[i].isupper():
				path.append(s[i].lower())
				dfs(i + 1)  # 转换
				path.pop()
			elif s[i].islower():
				path.append(s[i].upper())
				dfs(i + 1)  # 转换
				path.pop()
			
			path.pop()
		dfs(0)
		return list(ans)
	
class Solution:
	def letterCasePermutation(self, s):
		ans = set()
		n = len(s)
		path = [''] * n
		def dfs(i):
			if i == n:
				ans.add(''.join(path))
				return

			path[i] = s[i]
			dfs(i + 1)
			if s[i].isupper():
				path[i] = s[i].lower()
				dfs(i + 1)  # 转换
			elif s[i].islower():
				path[i] = s[i].upper()
				dfs(i + 1)  # 转换
			
			# path.pop()
		dfs(0)
		return list(ans)
	
if __name__ == '__main__':
	s = 'a1b2'
	print(Solution().letterCasePermutation(s))