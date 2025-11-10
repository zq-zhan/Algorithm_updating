# 1.20250901最大平均通过率
class Solution:
	def maxAverageRatio(self, classes, extraStudents):
		h = [((a - b)/(b * (b + 1)), a, b) for a, b in classes]
		heap.heapify(h)
		for _ in range(extraStudents):
			_, a, b = h[0]
			a += 1
			b += 1
			heap.heapreplace(h, ((a - b)/(b * (b + 1)), a, b))
		return sum(a / b for _, a, b in h) / len(h)

# 2.20250902人员站位的方案数1
class Solution:
	def numberOfPairs(self, points):
		points.sort(key = lambda x: (x[0], -x[1]))
		n = len(points)
		ans = 0
		for i, (x, y) in enumerate(points):
			pre_min_y = inf
			for j in range(i - 1, -1, -1):
				x1, y1 = points[j]
				if x1 <= x and y <= y1 < pre_min_y:
					pre_min_y = min(y1, pre_min_y)
					ans += 1
		return ans
	
# 3.20250903人员站位的方案数2
class Solution:
	def numberOfPairs(self, points):
		points.sort(key = lambda x:(x[0], -x[1]), reverse = True)
		n = len(points)
		ans = 0
		for i, (x, y) in enumerate(points):
			pre_min_y = inf
			for j in range(i + 1, n):
				x1, y1 = points[j]
				if x1 <= x and y <= y1 < pre_min_y:
					ans += 1
					pre_min_y = min(pre_min_y, y1)
				if y1 == pre_min_y:
					break
		return ans

# 4.20250904找到最近的人
class Solution:
	def findClosest(self, x, y, z):
		left = abs(x - z)
		right = abs(y - z)
		if left < right:
			return 1
		elif left > right:
			return 2
		else:
			return 0

# 5.20250905得到整数零需要执行的最少操作数
class Solution:
	def makeTheIntegerZero(self, num1, num2):
		for k in range(1, 61):  # k 不会超过 60（因为 2^60 已经非常大）
			x = num1 - k * num2
			# if x < k:
			# 	continue
			# # if x.bit_count() <= k:
			# if bin(x).count("1") <= k:
			# 	return k
			if x >= k and x.bit_count() <= k:
				return k
		return -1

# 6.20250906使数组元素都变为零的最少操作次数
## 解法一：超出时间限制
class Solution:
	def minOperations(self, queries):
		ans = 0
		for start, end in queries:
			temp_lis = [i for i in range(start, end + 1)]
			left, right = 0, end - start
			while left <= right:
				temp_lis[left] //= 4
				temp_lis[right] //= 4
				if temp_lis[left] == 0:
					left += 1
				if temp_lis[right] == 0:
					right -= 1
				ans += 1
		return ans
class Solution:  # 超时
	def minOperations(self, queries):
		ans = 0
		for start, end in queries:
			left = start
			right = end
			while start <= end:
				left //= 4
				right //= 4
				if left == 0:
					start += 1
					left = start
				if right == 0:
					end -= 1
					right = end
				if start == end:
					left //= 4
					right //= 4
				ans += 1
		return ans

# 7.20250907和为零的N个不同整数
class Solution:
	def sumZero(self, n):
		left = n // 2
		tag = n % 2
		ans = [x for x in range(1, left + 1)]
		ans.extend([-x for x in range(1, left + 1)])
		if tag:
			ans.append(0)
		return ans

# 8.20250908将整数转换为两个无零整数的和
class Solution:
	def getNoZeroIntegers(self, n):
		for x in range(1, n):
			# if str(n - x).count('0') == str(x).count('0') == 0:
			if '0' not in str(n - x) and '0' not in str(x):
				return [x, n - x]

# 9.20250909知道秘密的人数
## 灵神题解
class Solution:
	def peopleAwareOfSecret(self, n, delay, forget):
		MOD = 10 ** 9 + 7
		known = [0] * (n + 1)  # 表示恰好在第i天得知秘密的人数
		known[1] = 1

		for i in range(1, n + 1):
			known[i] %= MOD
			for j in range(i + delay, min(i + forget, n + 1)):
				known[j] += known[i]
		return sum(known[-forget:]) % MOD
## 前缀和写法
class Solution:
	def peopleAwareOfSecret(self, n, delay, forget):
		MOD = 10 ** 9 + 7
		s = [0] * (n + 1)  # known数组的前缀和
		s[1] = 1

		for j in range(2, n + 1):
			known = s[max(j - delay, 0)] - s[max(j - forget, 0)]
			s[j] = (s[j - 1] + known) % MOD
		# return (s[n] - s[-forget - 1]) % MOD
		return (s[n] - s[max(n - forget, 0)]) % MOD

# 10.20250910需要教语言的最少人数
class Solution:
	def minimumTeachings(self, n, languages, friendships):
		st = set()
		for x, y in friendships:
			if not bool(set(languages[x - 1]) & set(languages[y - 1])):  # 判断交集是否有元素
				st.add(x - 1)
				st.add(y - 1)

		total = len(st)
		cnt = [0] * (n + 1)
		for x in st:
			for l in languages[x]:
				cnt[l] += 1
		return total - max(cnt)  # 减掉会的最多的语言的人次，其他人就得都学这个语言

# 11.20250911将字符串中的元音字母排序
class Solution:
	def sortVowels(self, s):
		s = list(s)
		temp_lis = []
		temp_index = []
		for i, x in enumerate(s):
			if x in 'aeiouAEIOU':
				temp_lis.append(x)
				temp_index.append(i)
		temp_lis.sort()
		for i, index in enumerate(temp_index):
			s[index] = temp_lis[i]
		return ''.join(s)

# 12.20250912字符串元音游戏
class Solution:
	def doesAliceWin(self, s):
		# cnt_vowels = 0
		# for x in s:
		# 	if x in 'aeiou':
		# 		cnt_vowels += 1
		# return cnt_vowels != 0
		return any(c in s for c in 'aeiou')

# 13.20250913找到频率最高的元音和辅音
class Solution:
	def maxFreqSum(self, s):
		s = list(s)
		s.sort()
		cnt_vowels = cnt_consonant = 0
		left = 0
		for right, x in enumerate(s):
			if x == s[left]:
				continue
			if s[left] in 'aeiou':
				cnt_vowels = max(cnt_vowels, right - left)
			else:
				cnt_consonant = max(cnt_consonant, right - left)
			left = right
		if s[left] in 'aeiou':
			cnt_vowels = max(cnt_vowels, right - left + 1)
		else:
			cnt_consonant = max(cnt_consonant, right - left + 1)
		return cnt_vowels + cnt_consonant
## 灵神思路——用一个26维的列表存储每个字母出现的次数
class Solution:
	def maxFreqSum(self, s):
		cnt = [0] * 26
		cnt_vowels = cnt_consonant = 0
		for x in s:
			idx = ord(x) - ord('a')
			cnt[idx] += 1
			if x in 'aeiou':
				cnt_vowels = max(cnt_vowels, cnt[idx])
			else:
				cnt_consonant = max(cnt_consonant, cnt[idx])
		return cnt_vowels + cnt_consonant

# 20250914元音拼写检查器
class Solution:
	def spellchecker(self, wordlist, queries):
		wordlen_dic = defaultdict(list)
		for word in wordlist:
			wordlen_dic[len(word)].append(word)
		ans = []
		for querie in queries:
			m = len(querie)
			target_search = wordlen_dic[len(querie)]
			temp_ans = []
			for k, target_word in enumerate(target_search):
				if target_word == querie:
					temp_ans.append((0, k, target_word))
					break
				target_word_lis = list(target_word)
				querie_lis = list(querie)
				tag_all = True
				pre = 1
				for i in range(m):
					x = target_word_lis[i]
					y = querie_lis[i]
					if x != y:
						if x.lower() == y.lower():
							continue
						elif x in 'aeiouAEIOU' and y in 'aeiouAEIOU':
							pre = 2
							continue
						else:
							tag_all = False
							break
				if tag_all:
					temp_ans.append((pre, k, target_word))
			if temp_ans:
				temp_ans.sort()
				ans.append(temp_ans[0][2])
			else:
				ans.append('')
		return ans
## 灵神题解
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        origin = set(wordlist)
        lower_to_origin = {}
        vowel_to_origin = {}
        trans = str.maketrans("aeiou", "?????")  # 替换元音为 '?'

        for s in reversed(wordlist):
            lower = s.lower()
            lower_to_origin[lower] = s  # 例如 kite -> KiTe
            vowel_to_origin[lower.translate(trans)] = s  # 例如 k?t? -> KiTe

        for i, q in enumerate(queries):
            if q in origin:  # 完全匹配
                continue
            lower = q.lower()
            if lower in lower_to_origin:  # 不区分大小写的匹配
                queries[i] = lower_to_origin[lower]
            else:  # 不区分大小写+元音模糊匹配
                queries[i] = vowel_to_origin.get(lower.translate(trans), "")
        return queries

# 20250915可以输入的最大单词数
class Solution:
	def canBeTypedWords(self, text, brokenLetters):
		ans = 0
		for word in text.split(' '):
			tag = 1
			for broken in brokenLetters:
				if broken in word:
					tag = 0
					break
			ans += tag
		return ans
class Solution:
	def canBeTypedWords(self, text, brokenLetters):
		ans = 0
		for word in text.split(' '):
			if all(c not in brokenLetters for c in word):
				ans += 1
		return ans

# 20250916替换数组中的非互质数
class Solution:
	def replaceNonCoprimes(self, nums):
		def lcm(x, y):
			return abs(x * y) // gcd(x, y)
		ans = []
		pre = nums[0]
		for y in nums[1:]:
			temp_cal = gcd(pre, y)
			if temp_cal > 1:
				pre = lcm(pre, y)
			else:
				while ans and gcd(ans[-1], pre) > 1:
					pre = lcm(ans[-1], pre)
					ans.pop()
				ans.append(pre)
				pre = y
		while ans and gcd(ans[-1], pre) > 1:
			pre = lcm(ans[-1], pre)
			ans.pop()
		ans.append(pre)
		return ans
## 灵神思路
class Solution:
	def replaceNonCoprimes(self, nums):
		st = []
		for x in nums:
			while st and gcd(x, st[-1]) > 1:
				x = lcm(x, st.pop())
			st.append(x)
		return st

# 20250917设计数字容器系统
class NumberContainers:

	def __init__(self):
		self.target_dic = defaultdict(list)
		self.target_idx = defaultdict(int)

	def change(self, index: int, number: int):
		ori = self.target_idx[index]
		if ori:
			self.target_dic[ori].remove(index)
		self.target_idx[index] = number
		self.target_dic[number].append(index)

	def find(self, number: int):
		temp = self.target_dic[number]
		if not temp:
			return -1
		# temp.sort()
		ans = inf
		for idx in temp:
			if idx not in self.target_idx or self.target_idx[idx] == number:
				ans = min(ans, idx)
		return ans if ans < inf else -1
## 灵神题解
class NumberContainers:

	def __init__(self):
		self.target_dic = defaultdict(SortedSet)
		self.target_idx = defaultdict(int)

	def change(self, index: int, number: int):
		ori = self.target_idx.get(index, None)
		if ori is not None:
			self.target_dic[ori].discard(index)
		self.target_idx[index] = number
		self.target_dic[number].add(index)

	def find(self, number: int):   
		idx = self.target_dic[number]
		return idx[0] if idx else -1
class NumberContainers:

	def __init__(self):
		self.target_dic = defaultdict(list)
		self.target_idx = defaultdict(int)

	def change(self, index: int, number: int):
		self.target_idx[index] = number
		heapq.heappush(self.target_dic[number], index)

	def find(self, number: int): 
		temp = self.target_dic[number]
		while temp and self.target_idx[temp[0]] != number:  # 最新的idx对应的number不是当前target_number
			heapq.heappop(temp)  # 旧数据可以直接删除
		return temp[0] if temp else -1

# 20250918设计任务管理器
class TaskManager:

	def __init__(self, tasks):
		self.task_userId = defaultdict(int)
		self.new_task = []
		self.task_priority = defaultdict(int)
		self.remove_task = set()

		for userId, taskId, priority in tasks:
			self.task_userId[taskId] = userId
			self.task_priority[taskId] = priority
			heapq.heappush(self.new_task, (-priority, -taskId, userId))
			# self.new_task.append((-priority, -taskId, userId))

	def add(self, userId: int, taskId: int, priority: int):
		self.task_userId[taskId] = userId
		self.task_priority[taskId] = priority
		heapq.heappush(self.new_task, (-priority, -taskId, userId))
		# self.new_task.append((-priority, -taskId, userId))
		self.remove_task.remove(taskId)

	def edit(self, taskId: int, newPriority: int):
		self.task_priority[taskId] = newPriority
		userId = self.task_userId[taskId]
		heapq.heappush(self.new_task, (-newPriority, -taskId, userId))
		# self.new_task.append((-newPriority, -taskId, userId))

	def rmv(self, taskId: int):
		del self.task_priority[taskId]
		del self.task_userId[taskId]
		self.remove_task.add(taskId)

	def execTop(self) -> int:
		while self.new_task and -self.new_task[0][1] not in self.remove_task:
			priority, taskId, userId = heapq.heappop(self.new_task)
			if priority != self.task_priority[-taskId]:
				continue
			del self.task_priority[-taskId]
			del self.task_userId[-taskId]
			self.remove_task.add(-taskId)
			return userId
		return -1

class TaskManager:
    def __init__(self, tasks):
        self.mp = {taskId: (priority, userId) for userId, taskId, priority in tasks}
        self.h = [(-priority, -taskId, userId) for userId, taskId, priority in tasks]  # 取相反数，变成最大堆
        heapify(self.h)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.mp[taskId] = (priority, userId)
        heappush(self.h, (-priority, -taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        # 懒修改
        self.add(self.mp[taskId][1], taskId, newPriority)

    def rmv(self, taskId: int) -> None:
        # 懒删除
        self.mp[taskId] = (-1, -1)

    def execTop(self) -> int:
        while self.h:
            priority, taskId, userId = heappop(self.h)
            if self.mp[-taskId] == (-priority, userId):
                self.rmv(-taskId)
                return userId
            # else 货不对板，堆顶和 mp 中记录的不一样，说明堆顶数据已被修改或删除，不做处理
        return -1

# 20250918设计电子表格
class Spreadsheet:

	def __init__(self, rows: int):
		self.matrix = [[0] * 26 for _ in range(rows)] 

	def setCell(self, cell: str, value: int) -> None:
		col = ord(cell[0]) - ord('A')
		row = int(cell[1:]) - 1
		self.matrix[row][col] = value

	def resetCell(self, cell: str) -> None:
		self.setCell(cell, 0)

	def getValue(self, formula: str) -> int:
		formula = formula[1:].split('+')
		X = formula[0]
		Y = formula[-1]
		if X[0].isalpha():
			col1 = ord(X[0]) - ord('A')
			row1 = int(X[1:]) - 1
			new_x = self.matrix[row1][col1].copy()
		else:
			new_x = int(X)
		if Y[0].isalpha():
			col2 = ord(Y[0]) - ord('A')
			row2 = int(Y[1:]) - 1
			new_y = self.matrix[row2][col2].copy()
		else:
			new_y = int(Y)
		return new_x + new_y		
## 灵神题解   
class Spreadsheet:

	def __init__(self, rows: int):
		self.data = {}

	def setCell(self, cell, value):
		self.data[cell] = value

	def resetCell(self, cell):
		self.data.pop(cell, None)  # 字典中删除键，不存在则返回None否则报错

	def getValue(self, formula):
		ans = 0
		for cell in formula[1:].split('+'):
			ans += self.data.get(cell, 0) if cell[0].isupper() else int(cell)
		return ans

# 20250922最大频率元素计数
class Solution:
	def maxFrequencyElements(self, nums):
		nums_dic = Counter(nums)
		max_p = max(nums_dic.values())
		ans = 0
		for val, cnt in nums_dic.items():
			if cnt == max_p:
				ans += cnt
		return ans

# 20250923比较版本号
class Solution:
	def compareVersion(self, version1, version2):
		version1 = list(version1.split('.'))
		version2 = list(version2.split('.'))
		while version1 and int(version1[-1]) == 0:
			version1.pop()
		while version2 and int(version2[-1]) == 0:
			version2.pop()
		n, m = len(version1), len(version2)
		i = j = 0
		while i < n and j < m:
			x = int(version1[i])
			y = int(version2[j])
			if x == y:
				i += 1
				j += 1
				continue
			elif x < y:
				return -1
			else:
				return 1
		if i == n and j == m:
			return 0
		elif i < n and j == m:
			return 1
		else:
			return -1
## 灵神——库函数用法
class Solution:
	def compareVersion(self, version1, version2):
		a = map(int, version1.split('.'))
		b = map(int, version2.split('.'))
		for x, y in zip_longest(a, b, fillvalue = 0):
			if x != y:
				return -1 if x < y else 1
		return 0

# 20250924分数到小数
## 灵神题解——模拟长除法
## PS:
class Solution:
	def fractionToDecimal(self, numerator, denominator):
		sign = '-' if numerator * denominator < 0 else ''
		numerator = abs(numerator)
		denominator = abs(denominator)

		q, r = divmod(numerator, denominator)  # 初始整数部分q和余数r
		if r == 0:
			return sign + str(q)

		ans = [sign + str(q) + '.']
		r_to_pos = {r:1}
		while r:
			q, r = divmod(r * 10, denominator)
			ans.append(str(q))
			if r in r_to_pos:
				pos = r_to_pos[r]
				return f"{''.join(ans[:pos])}({''.join(ans[pos:])})"
			r_to_pos[r] = len(ans)
		return ''.join(ans)

# 20250925三角形最小路径和
class Solution:
	def minimumTotal(self, triangle):
		n = len(triangle)
		@cache
		def dfs(i, j):
			if i == n - 1:
				return triangle[i][j]
			# if j > i:
			# 	return inf
			return min(dfs(i + 1, j), dfs(i + 1, j + 1)) + triangle[i][j]
		return dfs(0, 0)

# 20250926有效三角形的个数
class Solution:
	def triangleNumber(self, nums):
		nums.sort()
		n = len(nums)
		ans = 0
		for k in range(2, n):
			left, right = 0, k - 1
			while left < right:
				if nums[left] + nums[right] > nums[k]:
					ans += right - left
					right -= 1
				else:
					left += 1
		return ans

# 20250929最大三角形面积
class Solution:
	def largestTriangleArea(self, points):
		# nums = points.copy()
		points.sort()
		n = len(points)
		ans = 0
		x, z = points[0], points[-1]
		for i in range(1, n - 1):
			y = points[i]
			a = z[0] - x[0]
			b = max(abs(x[1] - y[1]), abs(x[1] - z[1]), abs(y[1] - z[1]))
			area_1 = (y[0] - x[0]) * abs(y[1] - x[1])
## 灵神题解——1/2的平行四边形面积
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        ans = 0
        for p1, p2, p3 in combinations(points, 3):
            x1, y1 = p2[0] - p1[0], p2[1] - p1[1]
            x2, y2 = p3[0] - p1[0], p3[1] - p1[1]
            ans = max(ans, abs(x1 * y2 - y1 * x2))  # 注意这里没有除以 2
        return ans / 2

# 20250928三角形的最大周长
class Solution:
	def largestPerimeter(self, nums):
		ans = 0
		nums.sort(reverse = True)
		n = len(nums)
		for k in range(n - 2):
			if nums[k + 2] + nums[k + 1] > nums[k]:
				return nums[k + 2] + nums[k + 1] + nums[k]
		return 0
				
# 20250930数组的三角和
class Solution:
	def triangularSum(self, nums):
		while len(nums) > 1:
			n = len(nums)
			for i in range(n - 1):
				nums[i] = (nums[i + 1] + nums[i]) % 10
			nums.pop()
		return nums[-1]



