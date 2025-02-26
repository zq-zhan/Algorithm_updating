# 1.删除子串后字符串的最小长度
class Solution1:
	def minLength(self, s):
		st = []
		for x in s:
			if st and ((st[-1] == 'A' and x == 'B') or (st[-1] == 'C' and x == 'D')):
				st.pop()
			else:
				st.append(x)
		return len(st)
## 优化 利用哨兵减少判断条件
class Solution1:
	def minLength(self, s):
		st = [0]
		for x in s:
			if (st[-1] == 'A' and x == 'B') or (st[-1] == 'C' and x == 'D'):
				st.pop()
			else:
				st.append(x)
		return len(st) - 1


# 2.删除字符串中所有相邻重复项
class Solution1:
	def removeDuplicates(self, s):
		st = []
		for x in s:
			if st and x == st[-1]:
				st.pop()
			else:
				st.append(x)
		return ''.join(st)

# 3.整理字符串
class Solution1:
	def makeGood(self, s):
		st = []
		for x in s:
			tag_x = 1 if x.isupper() else -1
			if st:
				if st[-1].isupper():
					tag_st = 1
				else:
					tag_st = -1
			if st and tag_x * tag_st == -1 and x.lower() == st[-1].lower():
				st.pop()
			else:
				st.append(x)
		return st
## 优化
class Solution2:
	def makeGood(self, s):
		st = []
		for x in s:
			if st and abs(ord(x) - ord(st[-1])) == ord('a') - ord('A'):
				st.pop()
			else:
				st.append(x)
		return ''.join(st)

# 4.检查替换后的词是否有效
class Solution1:
	def isValid(self, s):
		st = [0, 0]
		for x in s:
			if st[-2] == 'a' and st[-1] == 'b' and x == 'c':
				for i in range(2):
					st.pop()
			else:
				st.append(x)
		return len(st) == 2


# 5.美化数组的最少删除数
class Solution1:
	def minDeletion(self, nums):
		# n = len(nums)
		ans = 0
		st = []
		for c in nums:
			if st and (len(st) - 1) % 2 == 0 and st[-1] == c:
				# st.pop()
				ans += 1
			else:
				st.append(c)
		return ans + len(st) % 2
# 优化掉栈
class Solution2:
	def minDeletion(self, nums):
		ans, length = 0, -1
		before_chr = 'a'
		for c in nums:
			if length % 2 == 0 and before_chr == c:
				ans += 1
				# length -= 1
			else:
				before_chr = c
				length += 1
		return ans + (length + 1) % 2

# 6.删除字符串中的所有相邻重复项2
class Solution1:
	def removeDuplicates(self, s, k):
		st = []
		# cnt = 1
		for x in s:
			if len(st) >= k - 1:
				temp_str = ''.join(st[-(k - 1):])
				if temp_str == x * (k - 1):
					for i in range(k - 1):
						st.pop()
				else:
					st.append(x)
			else:
				st.append(x)
		return ''.join(st)
## 二维数组
class Solution2:
	def removeDuplicates(self, s, k):
		n = len(s)
		st = []
		for c in s:
			if not st or st[-1][0] != c:
				st.append([c, 1])
			elif st[-1][1] + 1 < k:
				st[-1][1] += 1
			else:
				st.pop()
		ans = ''
		for c, l in st:
			ans += c * l
		return ans

# 7.统计道路上的碰撞次数
class Solution1:  # 错解
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
		return len(s) - s.count('S')  # 剩下非停止的车都会被撞，且由于每辆车只会被撞一次（撞一次变为‘S'），所以对每个不为S的计数即可
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
