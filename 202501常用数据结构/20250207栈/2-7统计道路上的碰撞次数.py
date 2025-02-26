# 7.统计道路上的碰撞次数
class Solution1:
	def countCollisions(self, directions):
		st = [0]
		ans = 0
		for x in directions:
			if st[-1] == 'L':
				if x == 'L':
					st.append(x)
				elif x == 'S':
					st.append('S')
					# ans += 1
				elif x == 'R':
					st.append(x)
			elif st[-1] == 'S':
				if x == 'L':
					st.append('S')
					ans += 1
				elif x == 'S':
					st.append(x)
				elif x == 'R':
					st.append(x)
			elif st[-1] == 'R':
				if x == 'L':
					if st[-2] == 'R':
						ans += 3
						st[-2] = st[-1] = 'S'
						st.append('S')
					else:
						ans += 2
						st[-1] = 'S'
						st.append('S')
				elif x == 'S':
					ans += 1
					st[-1] = 'S'
					st.append('S')
				elif x == 'R':
					st.append(x)
			else:
				st.append(x)
		return ans
	
## 灵神题解
class Solution2:
	def countCollisions(self, s):
		s = s.lstrip('L')
		s = s.rstrip('R')
		return len(s) - s.count('S')
	
# 栈模拟思路
class Solution3:
	def countCollisions(self, s):
		st = []
		ans = 0
		for x in directions:
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
	directions = "LLSRSSRSSLLSLLLRSLSRL"
	# directions = 'RLRSLL'
	s = Solution3()
	print(s.countCollisions(directions))