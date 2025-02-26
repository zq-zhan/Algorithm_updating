# 8.简化路径
class Solution1:
	def simplifyPath(self, path):
		ans = ['/']
		p1, p2 = 0, 1
		n = len(path)
		sub_path = ''
		while p1 < n and p2 < n:
			sub_path += str(path[p2])
			if path[p2] != '/':
				p2 += 1
				continue
			else:
				if sub_path != '/':
					ans.append(sub_path)
				elif sub_path == '../':
					ans.pop()
				sub_path = ''	
				p1 = p2
				p2 += 1
		return ''.join(ans)
	

## 灵神思路
class Solution2:
	def simplifyPath(self, path):
		ans = ['/']
		for sub_str in path.split('/'):
			if sub_str == '..':
				ans.pop()
			elif sub_str == '':
				continue
			else:
				ans.append(sub_str + '/')
		ans_str = ''.join(ans)
		if ans_str[-1] == '/':
			return ans_str[:-1]
		else:
			return ans_str
	

class Solution:
    def simplifyPath(self, path):
        stk = []
        for s in path.split('/'):
            if s == "" or s == ".":
                continue
            if s != "..":
                stk.append(s)
            elif stk:
                stk.pop()
        return '/' + '/'.join(stk)

if __name__ == '__main__':
	path = "/../"
	print(Solution().simplifyPath(path))