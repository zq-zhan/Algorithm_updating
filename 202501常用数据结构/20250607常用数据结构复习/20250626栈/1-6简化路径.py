class Solution:
	def simplifyPath(self, path):
		path += '/'
		ans = []
		temp_s = ''
		for x in path:
			temp_s += x
			if temp_s == './':
				temp_s = ''
				continue
			elif temp_s == '../':
				if ans[-1] != '/':
					ans.pop()
				temp_s = ''
			elif x == '/': 
				if not ans or temp_s != '/':
					ans.append(temp_s)
				temp_s = ''
		ans = ''.join(ans)
		return ans[:-1] if len(ans) > 1 else ans

## 灵神题解
class Solution:
	def simplifyPath(self, path):
		stk = []
		for s in path.split('/'):
			if s == '' or s == '.':
				continue
			elif s != '..':
				stk.append(s)
			elif stk:
				stk.pop()
		return '/' + '/'.join(stk)
	
if __name__ == '__main__':
	path = "/a/../../b/../c//.//"
	print(Solution().simplifyPath(path))