# 1.用栈操作构建数组
class Solution1:
	def buildArray(self, target, n):
		ans = []
		max_num = min(n + 1, target[-1])
		for i in range(1, max_num):
			if i in target:
				ans.append('Push')
			else:
				ans.extend(['Push','Pop'])
		return ans

# 2.比较含退格的字符串
class Solution1:
	def backspaceCompare(self, s, t):
		new_s = []
		for x in s:
			# new_s += x
			if x == '#':
				if new_s:
					new_s.pop()
			else:
				new_s += x

		new_t = []
		for c in t:
			# new_t += c
			if c == '#':
				if new_t:
					new_t.pop()
			else:
				new_t += c

		return new_s == new_t
## 方法二：双指针（错解）
class Solution1:
	def backspaceCompare(self, s, t):
		s = list(s)
		t = list(t)
		p1, p2 = len(s) - 1, len(t) - 1

		while p1 >= 0 and p2 >= 0:
			cnt1 = cnt2 = 0
			while s[p1] == '#':
				cnt1 += 1
				p1 -= 1
			while t[p2] == '#':
				cnt2 += 1
				p2 -= 1

			if cnt1 > 0:
				if p1 - cnt1 >= 0:
					temp_s = s[p1 - cnt1]
					p1 -= cnt1 + 1
				else:
					p1 -= cnt1
			else:
				temp_s = s[p1]
				p1 -= 1

			if cnt2 > 0:
				if p2 - cnt2 >= 0:
					temp_t = t[p2 - cnt2]
					p2 -= cnt2 + 1
				else:
					p2 -= cnt1
			else:
				temp_t = t[p2]
				p2 -= 1

			if p1 >= 0 and p2 >= 0:
				if temp_s != temp_t:
					return False
				# else:
				# 	continue
			elif p1 < 0 and p2 < 0:
				continue
			else:
				return False

		return True

# 3.棒球比赛
class Solution1:
	def calPoints(self, ops):
		ans = []
		for x in ops:
			if x == 'C':
				ans.pop()
			elif x == 'D':
				ans.append(ans[-1] * 2)
			elif x == '+':
				ans.append(ans[-1] + ans[-2])
			else:
				ans.append(int(x))
		return sum(ans)

# 4.从字符串中移除星号
class Solution1:
	def removeStars(self, s):
		ans = []
		for char in s:
			if char == '*':
				ans.pop()
			else:
				ans.append(char)
		return ''.join(ans)

# 5.设计浏览器历史记录
class BrowserHistory:
	def __init__(self, homepage):
		self.s = []
		self.s.append(homepage)
		self.cnt = 0
		# self.cnt += 1

	def visit(self, url):
		while len(self.s) != self.cnt + 1:
			self.s.pop()
		self.s.append(url)
		self.cnt += 1

	def back(self, steps):
		# if self.cnt - steps >= 0:
		# 	temp_cnt = self.cnt - steps
		# 	self.cnt -= steps
		# 	return self.s[temp_cnt]
		# else:
		# 	self.cnt = 0
		# 	return self.s[0]
		self.cnt = max(self.cnt - steps, 0)
		return self.s[self.cnt]

	def forward(self, steps):
		# if self.cnt + forward <= len(self.s) - 1:
		# 	temp_cnt = self.cnt + forward
		# 	self.cnt += forward
		# 	return self.s[temp_cnt]
		# else:
		# 	self.cnt = len(self.s) - 1
		# 	return self.s[-1]
		self.cnt = min(self.cnt + steps, len(self.s) - 1)
		return self.s[self.cnt]


# 6.验证栈序列
class Solution1:
	def validateStackSequences(self, pushed, poped):
		ans = []
		p1 = p2 = 0
		n, m = len(pushed), len(poped)
		while p2 < m:
			while p1 < n and (not ans or ans[-1] != poped[p2]):
				ans.append(pushed[p1])
				p1 += 1
			if ans[-1] == poped[p2]:
				ans.pop()
			# p1 += 1
			p2 += 1
		return len(ans) == 0
## 
class Solution2:
	def validateStackSequences(self, pushed, poped):
		ans = []
		p2 = 0
		for num in pushed:
			ans.append(num)
			while ans and ans[-1] == poped[p2]:
				ans.pop()
				p2 += 1
		return not ans

# 7.计算字符串的镜像分数
class Solution1:
	def calculateScore(self, s):
		# start_a = ord('a')
		# end_z = ord('z')
		# distance = end_z - start_a + 1

		ans = 0
		ans_dic = defaultdict(list)
		for i, x in enumerate(s):
			position = ord(x) - ord('a')
			mirror_position = 26 - position - 1
			trans_char = chr(ord('a') + mirror_position)
			if trans_char not in ans_dic:
				ans_dic[x].append(i)
			else:
				ans += i - ans_dic[trans_char][-1]

				if len(ans_dic[trans_char]) > 1:
					# ans += ans_dic[trans_char][-1] - i
					ans_dic[trans_char].pop()
				else:
					del ans_dic[trans_char]
		return ans
## 灵神题解：26个栈
class Solution:
    def calculateScore(self, s):
        stk = [[] for _ in range(26)]
        ans = 0
        for i, c in enumerate(map(ord, s)):
            c -= ord('a')
            if stk[25 - c]:
                ans += i - stk[25 - c].pop()
            else:
                stk[c].append(i)
        return ans

# 8.简化路径
class Solution1:
	def simplifyPath(self, path):
		ans = ['/']
		p1, p2 = 0, 1
		n = len(path)
		sub_path = ''
		while p1 < n and p2 < n:
			sub_path += path[p2]
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
		ans_str = ''.join(ans)
		if ans_str[-1] == '/':
			return ans_str[:-1]
		else:
			return ans_str
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

# 9.删除星号以后字典序最小的字符串
## 灵神思路一
class Solution1:
	def clearStars(self, s):
		ans_lis = [[] for _ in range(26)]
		start_a = ord('a')
		for i, c in enumerate(s):
			if c != '*':
				ans_lis[ord(c) - start_a].append(i)
				continue
			for p in ans_lis:  # 删除该星号左边字典序最小的字符
				if p:
					p.pop()
					break
		return ''.join(s[i] for i in sorted(chain.from_iterable(ans_lis)))
# 思路二：
class Solution:
    def clearStars(self, s):
        s = list(s)
        st = [[] for _ in range(26)]
        for i, c in enumerate(s):
            if c != '*':
                st[ord(c) - ord('a')].append(i)
                continue
            for p in st:
                if p:
                    s[p.pop()] = '*'  # 删除后面的字符能使剩余字符尽量小
                    break
        return ''.join(c for c in s if c != '*')

# 10.最小栈
class MinStack():
	def __init__(self):
		self.ori_lis = []
		# self.min_num = inf

	def push(self, val):
		self.ori_lis.append(val)
		# self.min_num = min(self.min_num, val)

	def pop(self):
		self.ori_lis.pop()

	def top(self):
		return self.ori_lis[-1]

	def getMin(self):
		return min(self.ori_lis)
## 灵神思路：O(1)——前缀最小值
class MinStack:
	def __init__(self):
		self.st = [(0, inf)]  # 栈底哨兵

	def push(self, val):
		self.st.append((val, min(self.st[-1][1], val)))

	def pop(self):
		self.st.pop()

	def top(self):
		return self.st[-1][0]

	def getMin(self):
		return self.st[-1][1]

# 11.设计一个支持增量操作的栈
class CustomStack:
	def __init__(self, maxSize):
		self.maxSize = maxSize
		self.st = []

	def push(self, x):
		if len(self.st) < self.maxSize:
			self.st.append(x)

	def pop(self):
		if self.st:
			return self.st.pop()
		else:
			return -1

	def inc(self, k, val):
		# i = 0
		# while i < k and i < len(self.st):
		# 	self.st[i] += val
		# 	i += 1
		for i in range(0, min(k, len(self.st))):
			self.st[i] += val
## O(1)解
class CustomStack:
    def __init__(self, maxSize):
        self.stack = [0] * maxSize
        self.nums = [0] * maxSize
        self.size = maxSize - 1
        self.p = -1

    def push(self, x):
        if self.p != self.size:
            self.p += 1
            self.stack[self.p] = x

    def pop(self):
        if self.p == -1:
            return -1
        x, val = self.stack[self.p], self.nums[self.p]
        self.nums[self.p] = 0
        self.p -= 1
        if self.p != -1:
            self.nums[self.p] += val
        return x + val

    def increment(self, k, val):
        if self.p >= 0:
            k = min(self.p, k - 1)
            self.nums[k] += val
## 二维数组O(1)解
class CustomStack:
	def __init__(self, maxSize):
		self.stack = []
		self.length = 0
		self.maxSize = maxSize

	def push(self, x):
		if self.length < self.maxSize:
			self.length += 1
			self.stack.append([x, 0])

	def pop(self):
		if self.length == 0:
			return -1
		else:
			self.length -= 1
			num, add = self.stack.pop()
			if self.length > 0:
				self.stack[-1][1] += add
			return num + add

	def increment(self, k, val):
		if self.length > 0:
			if self.length < k:
				k = self.length
			self.stack[k - 1][1] += val


# 
class CustomStack:
	def __init__(self, maxSize):
		self.maxSize = maxSize
		self.st = []

	def push(self, x):
		if len(self.st) < self.maxSize:
			self.st.append([x, 0])

	def pop(self):
		if self.st:
			x, val = self.st.pop()
			if self.st:
				self.st[-1][1] += val
			return x + val
		else:
			return -1

	def increment(self, k, val):
		min_range = min(k, len(self.st))
		if self.st:
			self.st[min_range - 1][1] += val
















