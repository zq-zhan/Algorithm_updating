# 20251101从链表中移除在数组中存在的节点
class Solution:
	def modifiedList(self, nums, head):
		num_node = ListNode(0, next = head)
		cur = num_node
		nums = set(nums)
		while cur:
			if cur.next and cur.next.val in nums:
				cur.next = cur.next.next
			else:
				cur = cur.next
		return num_node.next

# 20251102统计网格图中没有被保卫的格子数
## 灵神题解
DIRS = (0, -1), (0, 1), (-1, 0), (1, 0)
class Solution:
	def countUnguarded(self, m, n, guards, walls):
		guarded = [[0] * n for _ in range(m)]

		for x, y in guards:
			guarded[x][y] = -1
		for x, y in walls:
			guarded[x][y] = -1

		# 遍历警卫
		for x0, y0 in guards:
			for dx, dy in DIRS:
				x, y = x0 + dx, y0 + dy
				while 0 <= x < m and 0 <= y < n and guarded[x][y] != -1:
					guarded[x][y] = 1 # 被保卫
					x += dx
					y += dy

		return sum(row.count(0) for row in guarded)

# 20251103使绳子变成彩色的最短时间
class Solution:
	def minCost(self, colors, neededTime):
		ans = 0
		n = len(colors)
		for i in range(1, n):
			if colors[i] == colors[i - 1]:
				if neededTime[i] < neededTime[i - 1]:
					ans += neededTime[i]
					neededTime[i] = neededTime[i - 1]
				else:
					ans += neededTime[i - 1]
		return ans

# 20251104计算子数组的x-sum
class Solution:
	def findXSum(self, nums, k, x):
		temp_dic = defaultdict(int)
		ans = []
		for i, num in enumerate(nums):
			temp_dic[num] += 1
			if sum(temp_dic.values()) < k:
				continue
			else:
				new_arr = [(cnt, key) for key, cnt in temp_dic.items()]
				new_arr.sort(reverse = True)
				temp_s = 0
				for j in range(min(x, len(new_arr))):
					temp_s += new_arr[j][0] * new_arr[j][1]
				ans.append(temp_s)
				temp_dic[nums[i - k + 1]] -= 1	
		return ans		

# 20251106电网维护
## 错解
class Solution:
	def processQueries(self, c, connections, queries):
		new_dic = defaultdict(list)
		for x, y in connections:
			new_dic[x].append(y)
			new_dic[y].append(x)

		ans = []
		remove_set = set()
		for tag, x in queries:
			if tag == 1:
				if x not in remove_set:
					ans.append(x)
					continue
				else:
					temp_lis = new_dic[x]
					temp_tag = False
					if temp_lis:
						temp_lis.sort()
						for y in temp_lis:
							if y not in remove_set:
								ans.append(y)
								temp_tag = True
								break
					if not temp_tag:
						ans.append(-1)
			else:
				remove_set.add(x)
		return ans
## 灵神题解
class Solution:
    def processQueries(self, c, connections, queries):
        g = [[] for _ in range(c + 1)]
        for x, y in connections:
            g[x].append(y)
            g[y].append(x)

        belong = [-1] * (c + 1)
        cc = 0  # 连通块编号

        def dfs(x: int) -> None:
            belong[x] = cc  # 记录节点 x 在哪个连通块
            for y in g[x]:
                if belong[y] < 0:
                    dfs(y)

        for i in range(1, c + 1):
            if belong[i] < 0:
                dfs(i)
                cc += 1

        # 记录每个节点的离线时间，初始为无穷大（始终在线）
        offline_time = [inf] * (c + 1)
        for i in range(len(queries) - 1, -1, -1):
            t, x = queries[i]
            if t == 2:
                offline_time[x] = i  # 记录离线时间

        # 每个连通块中仍在线的电站的最小编号
        mn = [inf] * cc
        for i in range(1, c + 1):
            if offline_time[i] == inf:  # 最终仍在线
                j = belong[i]
                mn[j] = min(mn[j], i)

        ans = []
        for i in range(len(queries) - 1, -1, -1):
            t, x = queries[i]
            j = belong[x]
            if t == 2:
                if offline_time[x] == i:
                    mn[j] = min(mn[j], x)  # 变回在线
            elif i < offline_time[x]:  # 已经在线（写 < 或者 <= 都可以）
                ans.append(x)
            elif mn[j] != inf:
                ans.append(mn[j])
            else:
                ans.append(-1)
        ans.reverse()
        return ans

# 20251110将所有元素变为0的最少操作次数
## 错解
class Solution:
	def minOperations(self, nums):
		ans = 0
		mn = min(nums)
		n = len(nums)
		if mn != 0:
			ans += 1
		nums = [mn] + nums
		for i in range(n + 1):
			if nums[i] == mn or nums[i] >= nums[i - 1]:
				continue
			ans += 1
		return ans
## 灵神题解
class Solution:
	def minOperations(self, nums):
		ans = 0
		st = []
		for x in nums:
			while st and x < st[-1]:
				st.pop()
				ans += 1
			if not st or x != st[-1]:
				st.append(x)
		return ans + len(st) - (st[0] == 0)

# 20251111一和零
class Solution:
	def findMaxForm(self, strs):
		strs_0 = []
		strs_1 = []
		for x in strs:
			zero_num = x.count('0')
			strs_0.append(zero_num)
			strs_1.append(len(x) - zero_num)
		@cache
		def dfs(i, x, y):
			if i < 0:
				return 0
			if x + strs_0[i] <= m and y + strs_1[i] <= n:
				return max(dfs(i - 1, x, y), dfs(i - 1, x + strs_0[i], y + strs_1[i]) + 1)
			return dfs(i - 1, x, y)
		return dfs(len(strs) - 1, 0, 0)

# 20251112使数组所有元素变成1的最少操作次数
class Solution:
	def minOperations(self, nums):
		tag = True
		cnt = 0
		n = len(nums)
		cnt_1 = nums.count(1)
		while tag:
			m = len(nums)
			for i in range(m - 1):
				temp = gcd(nums[i], nums[i + 1])
				nums[i] = temp
				if temp == 1:
					tag = False
					break
			if nums:
				nums.pop()
			else:
				return -1
			cnt += 1
		return n - cnt_1 + cnt - 1

# 20251113将1移动到末尾的最大操作次数
## 超时
class Solution:
	def maxOperations(self, s):
		s = list(map(int, s))
		cnt_1 = s.count(1)
		ans = 0
		n = len(s)
		while sum(s[-cnt_1:]) != cnt_1:
			tag = False
			for i in range(n - 1):
				if s[i] - s[i + 1] == 1:
					s[i + 1], s[i] = s[i], s[i + 1]
					tag = True
					ans += int(i == n - 2)
				else:
					if tag == True:
						ans += 1
						break
		return ans
## 灵神题解
class Solution:
	def maxOperations(self, s):
		ans = cnt1 = 0
		for i, c in enumerate(s):
			if c == '1':
				cnt1 += 1
			elif i > 0 and s[i - 1] == '1':
				ans += cnt1
		return ans

# 20251114子矩阵元素加1
class Solution:
	def rangeAddQueries(self, n, queries):
		mat = [[0] * n for _ in range(n)]
		for x1, y1, x2, y2 in queries:
			for i in range(x1, x2 + 1):
				for j in range(y1, y2 + 1):
					mat[i][j] += 1
		return mat
## 灵神题解——二维差分
class Solution:
	def rangeAddQueries(self, n, queries):
		diff = [[0] * (n + 2) for _ in range(n + 2)]
		for x1, y1, x2, y2 in queries:
			diff[x1 + 1][y1 + 1] += 1
			diff[x1 + 1][y2 + 2] -= 1
			diff[x2 + 2][y1 + 1] -= 1
			diff[x2 + 2][y2 + 2] += 1

		ans = [[0] * n for _ in range(n)]
		for i in range(n):
			for j in range(n):
				diff[i + 1][j + 1] += diff[i + 1][j] + diff[i][j + 1] - diff[i][j]
				ans[i][j] = diff[i + 1][j + 1]
		return ans

# 20251115统计1显著的字符串的数量
class Solution:
	def numberOfSubstrings(self, s):
		n = len(s)
		ans = 0
		for length in range(1, n + 1):
			for i in range(0, n - length + 1):
				cnt_1 = s[i:i + length].count('1')
				cnt_0 = length - cnt_1
				if cnt_1 >= cnt_0 ** 2:
					ans += 1
		return ans

# 20251116仅含1的子串数
class Solution:
	def numSub(self, s):
		MOD = 10 ** 9 + 7
		ans = 0
		left = 0
		s += '0'
		for right, x in enumerate(s):
			if x == 0:
				ans += (right - left) * (right - left + 1) // 2
				left = right + 1
		return ans % MOD

# 20251117是否所有1都至少相隔k个元素
class Solution:
	def kLengthApart(self, nums, k):
		pre = -1
		for i, x in enumerate(nums):
			if x == 1:
				if (pre != -1 and i - pre - 1 >= k) or pre == -1:
					pre = i
					continue
				else:
					return False
		return True

# 202511181比特与2比特字符
class Solution:
	def isOneBitCharacter(self, bits):
		cnt_1 = 0
		for x in bits[:-1]:
			if x == 0:
				cnt_1 = 0
			else:
				cnt_1 += 1
		return cnt_1 % 2 == 0

# 20251119将找到的值乘以2
class Solution:
	def findFinalValue(self, nums, original):
		nums.sort()
		for x in nums:
			if x == original:
				original *= 2
		return original
## 灵神解法——集合
class Solution:
	def findFinalValue(self, nums, original):
		st = set(nums)
		while original in st:
			original *= 2
		return original

# 只出现一次的数字3
class Solution:
	def singleNumber(self, nums):
		# 对所有数字进行异或运算
		xor_all = 0
		for num in nums:
			xor_all ^= num

		# 找异或结果中最右边的1
		rightmost_set_bit = 1
		while (xor_all & rightmost_set_bit) == 0:
			rightmost_set_bit <<= 1 # 左移1位，相当于乘以2

		# 将数字分成两组
		a = b = 0
		for num in nums:
			if num & rightmost_set_bit:
				a ^= num  # 同一组只有一个数出现一次其他都出现两次，故每一组的异或和就是答案
			else:
				b ^= num
		return [a, b]
## 灵神解法
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_all = reduce(xor, nums) # 对所有数异或和
        lowbit = xor_all & -xor_all  # 找到二进制最低位的不同点用来区分元素在哪一组

        ans = [0, 0]
        for x in nums:
            if (x & lowbit) == 0:  # x 在第一组
                ans[0] ^= x
            else:  # x 在第二组
                ans[1] ^= x
        return ans

# 20251120设置交集大小至少为2
## 灵神题解:栈+二分查找
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])
        # 栈中保存闭区间左右端点，栈底到栈顶的区间长度的和
        st = [(-2, -2, 0)]  # 哨兵，保证不和任何区间相交
        for start, end in intervals:
            _, r, s = st[bisect_left(st, (start,)) - 1]
            d = 2 - (st[-1][2] - s)  # 去掉运行中的时间点
            if start <= r:  # start 在区间 st[i] 内
                d -= r - start + 1  # 去掉运行中的时间点
            if d <= 0:
                continue
            while end - st[-1][1] <= d:  # 剩余的 d 填充区间后缀
                l, r, _ = st.pop()
                d += r - l + 1  # 合并区间
            st.append((end - d + 1, end, st[-1][2] + d))
        return st[-1][2]
## 排序+贪心，注意怎么排序！！
class Solution:
	def intersectionSizeTwo(self, intervals):
		intervals.sort(key = lambda x: (x[1], -x[0]))
		s = e = -1
		ans = 0
		for a, b in intervals:
			if a <= s:
				continue
			elif a > e:
				ans += 2
				s, e = b - 1, b
			else:
				ans += 1
				s, e = e, b
		return ans

# 20251121长度为3的不同回文子序列
class Solution:
	def countPalindromicSubsequence(self, s):
		ans = set()
		left, right = 0, len(s) - 1
		while left < right - 1:
			if s[left] == s[right]:
				for x in s[left + 1:right]:
					ans.add(s[left] + x + s[right])
			left += 1
		return len(ans)
## 枚举两侧
class Solution:
	def countPalindromicSubsequence(self, s):
		ans = 0
		for alpha in ascii_lowercase:
			i = s.find(alpha) # 最左边x的下标
			if i < 0:
				continue
			j = s.rfind(alpha) # 最右边x的下标
			ans += len(set(s[i + 1:j]))
		return ans
## 枚举中间 + 前后缀分解
class Solution:
	def countPalindromicSubsequence(self, s):
		suf_cnt = Counter(s[1:]) # 统计[1, n - 1]每个字母的个数
		pre_set = set()
		st = set()
		for i in range(1, len(s) - 1): # 枚举中间
			mid = s[i]
			suf_cnt[mid] -= 1
			if suf_cnt[mid] == 0:
				del suf_cnt[mid]
			pre_set.add(s[i - 1])
			for alpha in pre_set & suf_cnt.keys():
				st.add(alpha + mid)
		return len(st)

# 使所有元素都可以被3整除的最少操作数
class Solution:
	def minimumOperations(self, nums):
		# return sum(min(x % 3, 3 - x % 3) for x in nums)
		return sum(x % 3 != 0 for x in nums)

# 20251123可被三整除的最大和
## 错解！！！！
class Solution:
	def maxSumDivThree(self, nums):
		nums_dic = Counter(nums)
		ans = 0
		temp_mod_1 = []
		temp_mod_2 = []
		for key, value in nums_dic.items():
			if key % 3 == 0:
				ans += key * value
			elif key % 3 == 1:
				temp_mod_1.extend([key] * value)
			else:
				temp_mod_2.extend([key] * value)
		new_lis = []
		for x in temp_mod_1:
			new_lis.append((x, 2))
		for y in temp_mod_2:
			new_lis.append((x, 1))
		new_lis.sort(lambda x:x[0], reverse = True)
		pre = (0, 0)
		count_s = temp_s = 0
		for i, (x, y) in enemerate(new_lis):
			temp_s += x
			count_s += y
			if count_s % 3 == 0:
				ans += temp_s
				temp_s = count_s = 0
			elif count_s > 3:
## 灵神题解——贪心
class Solution:
	def maxSumDivThree(self, nums):
		s = sum(nums)
		if s % 3 == 0:
			return s
		a1 = sorted(x for x in nums if x % 3 == 1)
		a2 = sorted(x for x in nums if x % 3 == 2)
		if s % 3 == 2:
			a1, a2 = a2, a1
		ans = s - a1[0] if a1 else 0
		if len(a2) > 1:
			ans = max(ans, s - a2[0] - a2[1])
		return ans
## 动态规划
class Solution:
	def maxSumDivThree(self, nums):
		@cache
		def dfs(i, j):
			if i < 0:
				return 0 if j == 0 else -inf
			return max(dfs(i - 1, j), dfs(i - 1, (j + nums[i]) % 3) + nums[i])
		return dfs(len(nums) - 1, 0)

# 20251124可被5整除的二进制前缀
class Solution:
	def prefixesDivBy5(self, nums):
		s = 0
		ans = []
		for x in nums:
			s = (s * 2 + x) % 5
			ans.append(s == 0)
		return ans

# 20251125可被K整除的最小整数
class Solution:
	def smallestRepunitDivByK(self, k):
		if str(k)[-1] in ('2','4','5','6','8','0'):
			return -1
		pre = 1
		while True:
			if pre % k == 0:
				return len(str(pre))
			else:
				pre = pre * 10 + 1

## 灵神题解
class Solution:
	def smallestRepunitDivByK(self, k):
		seen = set()
		x = 1 % k
		while x and x not in seen:
			seen.add(x)
			x = (x * 10 + 1) % k
		return -1 if x else len(seen) + 1
## 解法二：
class Solution:
	def smallestRepunitDivByK(self, k):
		if k % 2 == 0 or k % 5 == 0:
			return -1
		x = 1 % k
		for i in count(1): # 必定有解
			if x == 0:
				return i
			x = (x * 10 + 1) % k

# 20251126矩阵中和能被K整除的路径
class Solution:
	def numberOfPaths(self, grid, k):
		MOD = 10 ** 9 + 7
		m, n = len(grid), len(grid[0])
		@cache
		def dfs(i, j, s):
			if i == m - 1 and j == n - 1:
				return int(s % k == 0)
			if i < m - 1 and j < n - 1:
				return dfs(i + 1, j, (s + grid[i + 1][j]) % k) + dfs(i, j + 1, (s + grid[i][j + 1]) % k)
			elif i < m - 1:
				return dfs(i + 1, j, (s + grid[i + 1][j]) % k)
			else:
				return dfs(i, j + 1, (s + grid[i][j + 1]) % k)

		ans = dfs(0, 0, grid[0][0]) % MOD
		dfs.cache_clear()
		return ans
## 灵神写法
class Solution:
	def numberOfPaths(self, grid, k):
		MOD = 10 ** 9 + 7
		m, n = len(grid), len(grid[0])

		@cache
		def dfs(i, j, pres):
			if i < 0 or j < 0:
				return 0
			pres = (s - grid[i][j]) % k
			if i == 0 and j == 0:
				return int(pres == 0)
			return (dfs(i - 1, j, pres) + dfs(i, j - 1, pres)) % MOD
		ans = dfs(m - 1, n - 1, 0)
		dfs.cache_clear()
		return ans

# 20251127长度可被K整除的子数组的最大元素和
## 超时
class Solution:
	def maxSubarraySum(self, nums, k):
		ans = -inf
		left = 0
		n = len(nums)
		while left < len(nums):
			temp_s = 0
			for right in range(left, n):
				temp_s += nums[right]
				if (right - left + 1) % k == 0:
					ans = max(temp_s, ans)
			left += 1
		return ans
## 灵神题解
class Solution:
	def maxSubarraySum(self, nums, k):
		pre = list(accumulate(nums, initial = 0))
		min_s = [inf] * k
		ans = -inf
		for j, s in enumerate(pre):
			i = j % k
			ans = max(ans, s - min_s[i])
			min_s[i] = min(min_s[i], s)
		return ans

# 20251129使数组和能被K整除的最少操作次数
class Solution:
	def minOperations(self, nums, k):
		return sum(nums) % k

# 20251130使数组和能被P整除
class Solution:
	def minSubarray(self, nums, p):
		target = sum(nums) % p
		if target % p == 0:
			return 0
		ans = n = len(nums)
		pre_s = 0
		temp_dic = defaultdict(int)
		temp_dic[0] = -1
		for i, x in enumerate(nums):
			pre_s += x
			temp_dic[pre_s % p] = i
			j = temp_dic.get((pre_s - target) % p, -n)
			ans = min(i - j, ans)
		return ans if ans < n else -1


		pre_s = list(accumulate(nums, initial = 0))
		s = pre_s[-1]
		if s % p == 0:
			return 0
		elif s < p:
			return -1
		ans = n = len(nums)
		temp_dic = defaultdict(int)
		for i, x in enumerate(pre_s):




