# 20250501你可以安排的最多任务数目
class Solution1:
	def maxTaskAssign(self, tasks, workers, pills, strength):
		tasks.sort()
		workers.sort(reverse = True)
		n, m = len(tasks), len(workers)
		@cache
		def dfs(i, j, c):
			if i >= n or j >= m:
				return 0
			if workers[j] >= tasks[i]:
				return dfs(i + 1, j + 1, c) + 1
			elif workers[j] < tasks[i] and c < pills and workers[j] + strength >= tasks[i]:
				return max(dfs(i + 1, j + 1, c + 1) + 1, dfs(i, j + 1, c))
			else:
				return dfs(i, j + 1, c)
		return dfs(0, 0, 0)
"""
本题核心在于想到对应的贪心策略
"""
## 灵神题解
class Solution2:
	def maxTaskAssign(self, tasks, workers, pills, strength):
		tasks.sort()
		workers.sort()

		def check(k):
			# 贪心思路：用最强的k名工人，完成最简单的k个任务，检查是否能完成
			i, p = 0, pills
			valid_task = deque()
			for w in workers[-k:]:
				while i < k and tasks[i] <= w + strength:
					valid_task.append(tasks[i])
					i += 1
				if not valid_task:
					return False
				if w >= valid_task[0]:
					valid_task.popleft()
					continue
				if p == 0:
					return False
				p -= 1
				valid_task.pop()
			return True

		left, right = 0, min(len(workers), len(tasks)) + 1
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				left = mid
			else:
				right = mid
		return left

# 20250502推多米诺
class Solution:
	def pushDominoes(self, deminoes):
		deminoes = list('L' + deminoes + 'R')
		n = len(deminoes)
		pre = 0
		ans = ''
		for i, c in enumerate(deminoes):
			if c == '.':
				continue
			elif c == deminoes[pre]:
				deminoes[pre + 1: i] = c * (i - pre - 1)
			elif c == 'L':
				m = (pre + i - 1) // 2
				deminoes[pre + 1:m + 1] = 'R' * (m - pre)
				m = (pre + i) // 2 + 1
				deminoes[m:i] = 'L' * (i - m)
			pre = i
		return ''.join(deminoes[1:-1])

# 20250503行相等的最少多米诺旋转
class Solution1:
	def minDominoRotations(self, tops, bottoms):
		ans = inf
		n = len(tops)
		for target in (tops[0], bottoms[0]):
			cnt_top = cnt_bottom = 0
			tag = True
			for i in range(n):
				if tops[i] == target and bottoms[i] == target:
					continue
				elif tops[i] != target and bottoms[i] != target:
					tag = False
					break
				elif tops[i] != target:
					cnt_top += 1
				elif bottoms[i] != target:
					cnt_bottom += 1

			if tag:
				ans = min(ans, cnt_top, cnt_bottom)
		return ans if ans < inf else -1

# 20250504等价多米诺骨牌对的数量
class Solution1:
	def numEquivDominoPairs(self, dominoes):
		ans = 0
		n = len(dominoes)
		for i in range(n):
			for j in range(i + 1, n):
				if dominoes[i] == dominoes[j] or dominoes[i][::-1] == dominoes[j]:
					ans += 1
		return ans
## 灵神题解
class Solution2:
	def numEquivDominoPairs(self, dominoes):
		ans = 0
		cnt = defaultdict(int)
		for d in dominoes:
			d = tuple(sorted(d))
			ans += cnt[d]
			cnt[d] += 1
		return ans

# 20250507到达最后一个房间的最少时间1
class Solution1:
	def minTimeToReach(self, moveTime):
		n, m = len(moveTime), len(moveTime[0])
		moveTime[0][0] = 0
		@cache
		def dfs(i, j):
			if i == 0 and j == 0:
				return moveTime[0][0]
			elif i < 0 or j < 0 or i >= n or j >= n:
				return inf
			temp_movetime = moveTime[i][j]
			return min(max(dfs(i - 1, j), temp_movetime),   # 会导致重复路径一直重复
					max(dfs(i, j - 1), temp_movetime),
					max(dfs(i + 1, j), temp_movetime),
					max(dfs(i, j + 1), temp_movetime)
					) + 1
		return dfs(n - 1, m - 1)
## 灵神题解
class Solution2:
	def minTimeToReach(self, moveTime):
		n, m = len(moveTime), len(moveTime[0])
		dis = [[inf] * m for _ in range(n)]
		dis[0][0] = 0
		h = [(0, 0, 0)]
		while True:
			d, i, j = heappop(h)
			if i == n - 1 and j == m - 1:
				return d
			if d > dis[i][j]:
				continue
			for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
				if 0 <= x < n and 0 <= y < m:
					new_dis = max(d, moveTime[x][y]) + 1
					if new_dis < dis[x][y]:
						dis[x][y] = new_dis
						heappush(h, (new_dis, x, y))

# 20250508到达最后一个房间的最少时间2
class Solution1:
	def minTimeToReach(self, moveTime):
		n, m = len(moveTime), len(moveTime[0])
		dis = [[inf] * m for _ in range(n)]
		dis[0][0] = 0
		h = [(0, 0, 0)]
		while True:
			d, i, j = heappop(h)
			if i == n - 1 and j == m - 1:
				return d
			if d > dis[i][j]:
				continue
			time = (i + j) % 2 + 1
			for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
				if 0 <= x < n and 0 <= y < m:
					new_dis = max(d, moveTime[x][y]) + time
					if new_dis < dis[x][y]:
						dis[x][y] = new_dis
						heappush(h, (new_dis, x, y))	

# 20250509统计平衡排列的数目
class Solution1:
	def countBalancedPermutations(self, num):
		s = sum(num)
		if s % 2 == 1:
			return 0
		target_num = len(num) // 2
		def dfs(i, c):
			if i < 0:
				return c == s // 2
			if c < s // 2:
				return dfs(i - 1, c - num[i]) or dfs(i - 1, c)
			elif c == s // 2:
				return dfs(i - 1, c)
			else:
				return False

# 20250510数组的最小相等和
class Solution1:
	def minSum(self, nums1, nums2):
		temp_s1 = sum(nums1)
		cnt_1 = nums1.count(0)

		temp_s2 = sum(nums2)
		cnt_2 = nums2.count(0)


		if cnt_1 > 0 and cnt_2 > 0:
			return max(temp_s1 + cnt_1, temp_s2 + cnt_2)
		elif cnt_1 > 0:
			if temp_s1 >= temp_s2:
				return -1
			else:
				if cnt_1 > temp_s2 - temp_s1:
					return -1
				else:
					return temp_s2
		elif cnt_2 > 0:
			if temp_s2 >= temp_s1:
				return -1
			else:
				if cnt_2 > temp_s1 - temp_s2:
					return -1
				else:
					return temp_s1
		else:
			if temp_s1 == temp_s2:
				return temp_s1
			else:
				return -1
## 优化题解
class Solution2:
	def minSum(self, nums1, nums2):
		s1, c1 = sum(nums1), nums1.count(0)
		s2, c2 = sum(nums2), nums2.count(0)

		b1 = s1 + c1
		b2 = s2 + c2
		t = max(b1, b2)

		if (c1 == 0 and b1 < t) or (c2 == 0 and b2 < t):
			return -1
		return t

# 20250511存在连续三个奇数的数组
class Solution1:
	def threeConsecutiveOdds(self, arr):
		cnt = 0
		for x in arr:
			if x % 2 == 1:
				cnt += 1
			else:
				cnt = 0
			if cnt >= 3:
				return True
		return False

# 20250512找出3位偶数
class Solution1:
	def findEvenNumbers(self, digits):
		n = len(digits)
		ans = set()
		for i, first_num in enumerate(digits):
			if first_num % 2:
				continue
			for j in range(n):
				if j == i:
					continue
				second_num = digits[j]
				for k in range(j + 1, n):
					if k == i:
						continue
					third_num = digits[k]
					if third_num != 0:
						ans.add(third_num * 100 + second_num * 10 + first_num)
					if second_num != 0:
						ans.add(second_num * 100 + third_num * 10 + first_num)
		return list(ans)
## 灵神思路：暴力枚举
class Solution1:
	def findEvenNumbers(self, digits):
		cnt_dic = Counter(digits)
		ans = []
		for i in range(100, 1000, 2):
			temp_num = Counter(map(int,str(i)))
			if all(cnt <= cnt_dic[val] for val, cnt in temp_num.items()):
				ans.append(temp_num)
		return ans

# 20250513字符串转换后的长度1
class Solution1:
	def lengthAfterTransformations(self, s, t):
		mod = 10 ** 9 + 7
		ord_a = ord('a')
		ans = ""
		times = t // 26
		cnt = t % 26
		while times > 0:
			for x in s:
				x = ch(ord(x) + 26)
				if ord(x) - ord_a > 0:
					s += 'b' 

# 20250515最长相邻不相等子序列
class Solution1:
	def getLongestSubsequence(self, words, groups):
		ans = []
		for i, c in enumerate(groups):
			if i == 0 or groups[i] != groups[i - 1]:
				ans.append(words[i])
		return ans

# 20250516最长相邻不相等子序列2
class Solution1:
	def getWordsInLongestSubsequence(self, words, groups):
		groups.sort()
		n = len(groups)
		pre_word = ''
		for i in range(n):
			if i == 0:
				pre_word = words[i]
				continue
			if i > 0 and groups[i] == groups[i - 1]:
				continue

			for j in range(len(pre_word)):


# 20250517颜色分类
class Solution1:
	def sortColors(self, nums):
		left = 0
		for target in (0, 1):
			right = left
			while right < len(nums):
				if nums[right] == target:
					nums[left], nums[right] = nums[right], nums[left]
					left += 1
				right += 1

# 20250519三角形类型
class Solution1:
	def triangleType(self, nums):
		nums.sort()
		if nums[0] + nums[1] <= nums[2]:
			return 'none'

		distinct_num = len(set(nums))
		if distinct_num == 1:
			return "equilateral"
		elif distinct_num == 2:
			return "isosceles"
		else:
			return "scalene"

					
# 20250520零数组变换1
class Solution1:  # 超时
	def isZeroArray(self, nums, queries):
		for left, right in queries:
			for i in range(left, right + 1):
				if nums[i] > 0:
					nums[i] -= 1
		return all(x == 0 for x in nums)
## 灵神题解——差分数组
class Solution2:
	def isZeroArray(self, nums, queries):
		diff = [0] * (len(nums) + 1)
		for left, right in queries:
			diff[left] -= 1
			diff[right + 1] += 1

		new_arr = list(accumulate(d))[:-1]
		return all(x + y <= 0 for x, y in zip(nums, new_arr))

# 20250521零数组变换2
class Solution1:  # O(nq)
	def minZeroArray(self, nums, queries):
		if sum(nums) == 0:
			return 0
		diff = [0] * (len(nums) + 1)
		ans = 0
		for left, right, val in queries:
			diff[left] -= val
			diff[right + 1] += val
			new_arr = list(accumulate(diff))[:-1]
			ans += 1
			if all(x + y <= 0 for x, y in zip(new_arr, nums)):
				return ans
		return -1
## 灵神题解——二分+差分
class Solution2:  # O(nlogq)
	def minZeroArray(self, nums, queries):
		def check(k):
			diff = [0] * (len(nums) + 1)
			for left, right, val in queries[:k]:
				diff[left] -= val
				diff[right + 1] += val
			for x, y in zip(nums, accumulate(diff)):
				if x + y > 0:
					return False
			return True

		n = len(queries)
		left, right = -1, n + 1
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				right = mid
			else:
				left = mid
		return right if right <= n else -1
## 灵神题解——双指针+差分
class Solution:
    def minZeroArray(self, nums, queries):
        diff = [0] * (len(nums) + 1)
        sum_d = k = 0
        for i, (x, d) in enumerate(zip(nums, diff)):
            sum_d += d
            while k < len(queries) and sum_d < x:  # 需要添加询问，把 x 减小
                l, r, val = queries[k]
                diff[l] += val
                diff[r + 1] -= val
                if l <= i <= r:  # x 在更新范围中
                    sum_d += val
                k += 1
            if sum_d < x:  # 无法更新
                return -1
        return k

# 20250527分类求和并作差
class Solution1:
	def differenceOfSums(self, n, m):
		ans = 0
		left, right = 1, n
		while left < right:
			if left % m != 0:
				ans += left
			else:
				ans -= left

			if right % m != 0:
				ans += right
			else:
				ans -= right
			left += 1
			right -= 1
		if left == right:
			ans += left if left % m != 0 else -left
		return ans
## 灵神思路
class Solution1:
	def differenceOfSums(self, n, m):
		return n * (n + 1) // 2 - n // m * (n // m + 1) * m


# 20250604从盒子中找出字典序最大的字符串1
class Solution1:
	def answerString(self, word, numFriends):
		if numFriends == 1:
			return word
		n = len(word)
		target_len = n - numFriends + 1
		ans = ''
		for i in range(n):
			ans = max(ans, word[i:i + target_len])
		return ans
## 灵神题解
class Solution:
    def answerString(self, s, numFriends):
        if numFriends == 1:
            return s
        n = len(s)
        i, j = 0, 1
        while j < n:
            k = 0
            while j + k < n and s[i + k] == s[j + k]:
                k += 1
            if j + k < n and s[i + k] < s[j + k]:
                i, j = j, max(j + 1, i + k + 1)
            else:
                j += k + 1
        return s[i: i + n - numFriends + 1]

# 20250606使用机器人打印字典序最小的字符串
class Solution:
	def robotWithString(self, s):
		mn = s[0]
		cnt = 1
		for i in range(1, len(s)):
			if s[i] < mn:
				cnt = 1
				mn = s[i]
			elif s[i] == mn:
				cnt += 1
			else:
				continue

		ans = ''
		for i in range(len(s)):
			if s[i] == mn:
				if cnt == 1:
					ans += s[i]
					break
				else:
					ans += s[i]
					cnt -= 1
			else:
				ans += s[i]
		return ans[::-1] + s[i:]
## 灵神题解
class Solution:
	def robotWithString(self, s):
		'''
		如果栈顶<=后缀s[i + 1:]中的最小值，就出栈
		'''
		n = len(s)
		# 计算后缀最小值
		suf_min = ['z'] * (n + 1)
		for i in range(n - 1, -1, -1):
			suf_min[i] = min(suf_min[i + 1], s[i])

		ans = []
		st = []
		for i, x in enumerate(s):
			st.append(x)
			while st and st[-1] <= suf_min[i + 1]:
				ans.append(st.pop())
		return ''.join(ans)

# 20250607删除星号以后字典序最小的字符串
class Solution1:
	def clearStars(self, s):
		s = list(s)
		st = [[] for _ in range(26)]
		for i, x in enumerate(s):
			if x != '*':
				st[ord(x) - ord('a')].append(i)
			else:
				for val in st:
					if val:
						s[val.pop()] = '*'
						break
		return ''.join(x for x in s if x != '*')

# 20250608字典序排数
class Solution1:
	def lexicalOrder(self, n):
		ans = []
		v = 1
		for _ in range(n):
			ans.append(v)
			if v * 10 <= n:
				v *= 10
			else:
				while v % 10 == 9 or v + 1 > n:
					v //= 10
				v += 1
		return ans
## 递归
class Solution:
	def lexicalOrder(self, n):
		ans = []

		def dfs(cur, limit):
			if cur > limit:
				return
			ans.append(cur)
			for i in range(10):
				dfs(cur * 10 + i, limit)

		for i in range(1, 10):
			dfs(i, n)
		return ans

class Solution:
	def findKthNumber(self, n: int, k: int) -> int:	
		ans = []
		v = 1
		for _ in range(n):
			ans.append(v)
			if len(ans) == k:
				return ans[-1]
			if v * 10 <= n:
				v *= 10
			else:
				while v % 10 == 9 or v + 1 > n:
					v //= 10
				v += 1
		return ans

# 20250610奇偶频次间的最大差值1
class Solution:
	def maxDifference(self, s):
		s_dic = Counter(s)
		mx = -inf
		mn = inf
		ans = 0
		for val in s_dic.values():
			if val % 2 == 1:
				mx = max(mx, val)
			else:
				mn = min(mn, val)
		return mx - mn
# 20250611奇偶频次间的最大差值2
class Solution:
	def maxDifference(self, s, k):
		dic_win = defaultdict(int)
		ans = 0
		for x in s:
			dic_win[x] += 1
			if 

# 20250612循环数组中相邻元素的最大差值
class Solution:
	def maxAdjacentDistance(self, nums):
		nums = nums + [nums[0]]
		ans = 0
		for i in range(1, len(nums)):
			ans = max(ans, abs(nums[i] - nums[i - 1]))
		return ans

# 20250613最小化数对的最大差值
class Solution:
	def minimizeMax(self, nums, p):  # O(nk)
		if 0 == p:
			return 0
		nums.sort()
		max_diff = nums[-1] - nums[0]
		
		for diff in range(max_diff + 1):
			i = cnt = 0
			while i < len(nums) - 1:
				if nums[i + 1] - nums[i] <= diff:
					cnt += 1
					if cnt == p:
						return diff
					i += 2
				else:
					i += 1
## 灵神二分
class Solution:
	def minimizeMax(self, nums, p):
		nums.sort()
		def check(target):
			cnt = i = 0
			while i < len(nums) - 1:
				if nums[i + 1] - nums[i] <= target:
					cnt += 1
					i += 2
				else:
					i += 1
			return cnt >= p

		left, right = -1, nums[-1] - nums[0]
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				right = mid
			else:
				left = mid
		return right

# 20250616增量元素之间的最大差值
class Solution:
	def maximumDifference(self, nums):
		ans = -1
		mn = inf
		for x in nums:
			ans = max(ans, x - mn)
			mn = min(mn, x)
		return ans if ans > 0 else -1

# 20250617统计有k个相等相邻元素的数组数目
class Solution:
	def countGoodArrays(self, n, m, k):
		mod = 10 ** 9 + 7
		ans = 0
		for key in range(n):
			cnt = m - k
## 灵神思路
class Solution:
	def countGoodArrays(self, n, m, k):
		mod = 10 **9 + 7
		return comb(n - 1, k) % mod * m * pow(m - 1, n - k - 1, mod) % mod

# 20250618划分数组并满足最大差限制
class Solution:
	def divideArray(self, nums, k):
		nums.sort()
		ans = []
		temp_ans = []
		for i in range(len(nums)):
			temp_ans.append(nums[i])
			if (i + 1) % 3 == 0:
				if temp_ans[-1] - temp_ans[0] > k:
					return []
				ans.append(temp_ans)
				temp_ans = []
		return ans

# 20250619划分数组使最大差为k
class Solution:
	def partitionArray(self, nums, k):
		nums.sort()
		# ans = 0
		# pre_mn = nums[0]
		# for i in range(1, len(nums)):
		# 	if nums[i] - pre_mn <= k:
		# 		continue
		# 	else:
		# 		pre_mn = nums[i]
		# 		ans += 1
		# return ans + 1
		ans = left = 0
		for right, x in enumerate(nums):
			if x - nums[left] <= k:
				continue
			else:
				left = right
				ans += 1
		return ans + 1

# 20250620最大曼哈顿距离
class Solution:
	def maxDistance(self, s, k):
		s = list(s)
		s_dic = Counter(s)
		if s_dic['N'] >= s_dic['S']:
			flag_1 = True
		if s_dic['W'] >= s_dic['W']:
			flag_2 = True

		result = ans = 0
		for i, x in enumerate(s):
			if x == 'N':
				if flag_1:
					ans += 1
				else:
					if k > 0:
						s[i] = 'S'
						k -= 1
						ans += 1
					else:
						ans -= 1
			elif x == 'S':
				if flag_1:
					if k > 0:
						s[i] = 'N'
						k -= 1
						ans += 1
					else:
						ans -= 1
				else:
					ans += 1
			elif x == 'W':
				if flag_2:
					ans += 1
				else:
					if k > 0:
						s[i] = 'E'
						k -= 1
						ans += 1
					else:
						ans -= 1
			elif x == 'E':
				if flag_2:
					if k > 0:
						s[i] = 'W'
						k -= 1
						ans += 1
					else:
						ans -= 1
				else:
					ans += 1
			result = max(result, ans)				
		return result
## 灵神题解1
class Solution:
	def maxDistance(self, s, k):
		ans = 0
		cnt = defaultdict(int)
		for ch in s:
			cnt[ch] += 1
			left = k
			def f(a, b):
				nonlocal left
				d = min(a, b, left)
				left -= d
				return abs(a - b) + 2 * d
			ans = max(ans, f(cnt['N'], cnt['S']) + f(cnt['E'], cnt['W']))
		return ans

# 20250621成为k特殊字符串需要删除的最少字符数
class Solution:
	def minimumDeletions(self, word, k):
		word_dic = Counter(word)
		word_cnt_lis = sorted(list(cnt for cnt in word_dic.values()))
		ans = left = 0
		for right, c in enumerate(word_cnt_lis):
			while abs(c - word_cnt_lis[left]) > k:
				ans += word_cnt_lis[left]
				left += 1
		return ans
## 灵神题解
class Solution:
    def minimumDeletions(self, word, k):
        cnt = sorted(Counter(word).values())
        max_save = 0
        for i, base in enumerate(cnt):
            s = sum(min(c, base + k) for c in cnt[i:])  # 至多保留 base+k 个
            max_save = max(max_save, s)
        return len(word) - max_save

# 20250622将字符串拆分为若干长度为k的组
class Solution:
	def divideString(self, s, k, fill):
		left = 0
		ans = []
		temp_s = ''
		for right, x in enumerate(s):
			temp_s += x
			if right - left + 1 < k:
				continue
			ans.append(temp_s)
			left = right + 1
			temp_s = ''
		if left < len(s):
			ans.append(temp_s + fill * (k - right + left - 1))
		return ans
## 灵神题解
class Solution:
	def divideString(self, s, k, fill):
		# n = len(s)
		# return [s[i:i + k] + fill * (k - n + i) for i in range(0, n, k)]  # 复杂度为O(n // k) * O(k) = O(n)
		## 先补全
		while len(s) % k != 0:
			s += fill
		return [s[i:i + k] for i in range(0, len(s), k)]

# 20250624找出数组中的所有k近邻下标
class Solution:
	def findKDistantIndices(self, nums, key, k):
		ans = set()
		n = len(nums)
		for i in range(n):
			if nums[i] == key:
				start = max(0, i - k)
				end = min(i + k, n - 1)
				for j in range(start, end + 1):
					ans.add(j)
				if end >= n:
					break
		return list(ans)
## 灵神题解
class Solution:
	def findKDistantIndices(self, nums, key, k):
		last = -inf
		for i in range(k - 1, -1, -1):
			if nums[i] == key:
				last = i
				break

		ans = []
		n = len(nums)
		for i in range(n):
			if i + k < n and nusm[i + k] == key:
				last = i + k
			if last >= i - k:
				ans.append(i)
		return ans

# 20250626小于等于k的最长二进制子序列
## 灵神题解——贪心
class Solution:
	def longestSubsequence(self, s, k):
		n, m = len(s), k.bit_length()
		if n < m:
			return n
		ans = m if int(s[-m:], 2) <= k else m - 1  # int(s, 2)是将二进制转换为对应的十进制整数
		return ans + s[:-m].count('0')
## 贪心思路：所有0的个数+倒序后最大能取到的1的个数
class Solution:
	def longestSubsequence(self, s, k):
		ans = s.count('0')
		total = 0
		for i, x in enumerate(s[::-1]):
			if x == '1':
				total += 1 << i
				if total <= k:
					ans += 1
				else:
					break
		return ans

## 子数组
class Solution:
	def longestSubsequence(self, s, k):
		n, m = len(s), k.bit_length()
		if n < m:
			return n
		ans = m - 1
		left = 0
		temp_s = ''
		for right, x in enumerate(s):
			temp_s += x
			if right - left + 1 < m:
				continue
			while int(temp_s, 2) > k:
				temp_s = temp_s[1:]
				left += 1
			ans = max(ans, right - left + 1)
		return ans






					
