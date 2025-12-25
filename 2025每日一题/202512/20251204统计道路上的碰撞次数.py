class Solution:
	def countCollisions(self, directions):
		directions = list(directions)
		ans = 0
		cnt = 1
		n = len(directions)
		for i in range(n - 1):
			if directions[i] == 'R':
				if directions[i + 1] == 'L':
					ans += cnt + 1
					directions[i + 1] = 'S'
					cnt = 1
				elif directions[i + 1] == 'S':
					ans += cnt
					cnt = 1
				else:
					cnt += 1
			elif directions[i] == 'L':
				if directions[i + 1] == 'L':
					cnt += 1
				elif directions[i + 1] == 'S':
					cnt = 1
				else:
					cnt = 1
			else:
				if directions[i + 1] == 'L':
					ans += cnt
					directions[i + 1] = 'S'
		return ans
## 灵神题解
class Solution:
	def countCollisions(self, s):
		s = s.lstrip('L')
		s = s.rstrip('R')
		return len(s) - s.count('S')  # 两辆相反算两次，一辆撞静止算1次计在移动车上



# 栈模拟思路
class Solution:
	def countCollisions(self, s):
		st = []
		ans = 0
		for x in s:
			if x == 'L':
				if st:
					while st and st[-1] == 'R':
						ans += 1
						st.pop()
					ans += 1
					st.append('S')
			elif x == 'S':
				while st and st[-1] == 'R':
					ans += 1
					st.pop()
				st.append('S')
			else:
				st.append(x)
		return ans
	
if __name__ == '__main__':
	directions = "SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR"
	s = Solution()
	print(s.countCollisions(directions))