# 1.爬楼梯
class Solution4:
	def climbStairs(self, n):
		@cache
		def dfs(i):
			if i <= 1:
				return 1
			return dfs(i - 1) + dfs(i - 2)
		return dfs(n)
## 递推优化
class Solution5:
	def climbStairs(self, n):
		f0 = 1 
		f1 = 1
		for i in range(2, n + 1):
			new_f = f0 + f1
			f0 = f1
			f1 = new_f
		return f1

# 2.使用最小花费爬楼梯
class Solution1:
	def minCostClimbingStairs(self, cost):
		@cache
		def dfs(i):
			if i <= 1:
				return 0
			return min(dfs(i - 1) + cost[i - 1], dfs(i - 2) + cost[i - 2])
		return dfs(len(cost))
## 递推优化
class Solution1:
	def minCostClimbingStairs(self, cost):
		f0 = f1 = 0
		for i in range(2, len(cost) + 1):
			new_f = min(f0 + cost[i - 2], f1 + cost[i - 1])
			f0 = f1
			f1 = new_f
		return f1

# 3.组合总和4
class Solution1:  # 错解：顺序不同为相同1
	def combinationSum4(self, nums, target):
		@cache
		def dfs(i, c):
			if i < 0:
				return 1 if c == 0 else 0
			return dfs(i - 1, c) + dfs(i, c - nums[i])
		return dfs(len(nums) - 1, target)
## 灵神题解
class Solution1:
	def combinationSum4(self, nums, target):
		@cache
		def dfs(i):
			if i == 0:
				return 1
			return sum(dfs(i - x) for x in nums if x <= i)
		return dfs(target)

# 4.统计构造好字符串的方案数
class Solution1:
	def countGoodStrings(self, low, high, zero, one):
		mod = (10 ** 9) + 7
		@cache
		def dfs(i):
			if i == 0:
				return 1
			elif i < 0:
				return 0
			return (dfs(i - zero) + dfs(i - one)) % mod
		return sum(dfs(x) for x in range(high, low - 1, -1)) % mod
## 灵神递推写法
class Solution1:
	def countGoodStrings(self, low, high, zero, one):
		mod = (10 ** 9) + 7
		f = [1] + [0] * high
		for i in range(1, high + 1):
			if i >= zero:
				f[i] = f[i - zero]
			if i >= one:
				f[i] = (f[i] + f[i - one]) % mod
		return sum(f[low:]) % mod

# 5.统计打字方案数
class Solution3:
	def countTexts(self, pressedKeys):
		mod = 10 ** 9 + 7
		press_lis = []
		left = 0
		n = len(pressedKeys)
		for right in range(n - 1):
			if pressedKeys[right] == pressedKeys[right + 1]:
				continue
			press_lis.append([pressedKeys[left], right - left + 1])
			left = right + 1
		press_lis.append([pressedKeys[left], n - left + 1])
		@cache
		def dfs(i, x):
			if i < 0:
				return 0
			elif i == 0:
				return 1
			return sum(dfs(i - y, x) for y in range(1, x + 1)) % mod
		ans = 1
		for x, cnt in press_lis:
			if x in ['7','9']:
				ans = ans * dfs(cnt, 4) % mod
			else:
				ans = ans * dfs(cnt, 3) % mod
		return ans

# 6.打家劫舍
class Solution1:
	def rob(self, nums):
		@cache
		def dfs(i):
			if i < 0:
				return 0
			return max(dfs(i - 1), dfs(i - 2) + nums[i])
		return dfs(len(nums) - 1)
## 递推写法
class Solution2:
	def rob(self, nums):
		f = [0, 0] + [0] * len(nums)
		for i, c in enumerate(nums):
			f[i + 2] = max(f[i + 1], f[i] + nums[i])
		return f[-1]
## 递推写法空间优化
class Solution3:
	def rob(self, nums):
		f0 = f1 = 0
		for x in nums:
			new_f = max(f1, f0 + x)
			f0 = f1
			f1 = new_f
		return f1

# 7.删除并获得点数 —— 值域打家劫舍
class Solution1:
	def deleteAndEarn(self, nums):
		n = max(nums) + 1
		a = [0] * n
		for x in nums:
			a[x] += x
		@cache
		def dfs(i):
			if i < 0:
				return 0
			return max(dfs(i - 1), dfs(i - 2) + a[i])
		return dfs(n - 1)

# 8.统计放置房子的方式数
class Solution1:
	def countHousePlacements(self, n):
		mod = 10 ** 9 + 7
		@cache
		def dfs(i):
			if i == 0:
				return 1
			elif i == 1:
				return 2
			return (dfs(i - 1) + dfs(i - 2)) % mod
		ans = dfs(n) * dfs(n) % mod
		return ans
## 递推写法
class Solution2:
	def countHousePlacements(self, n):
		mod = 10 ** 9 + 7
		f0 = 1
		f1 = 2
		for _ in range(n - 2):
			new_f = (f0 + f1) % mod
			f0 = f1
			f1 = new_f
		return f1 * f1 % mod

# 9.打家劫舍2
class Solution2:
	def rob(self, nums):
		def rob_w(arr):
			n = len(arr)
			@cache
			def dfs(i):
				if i < 0:
					return 0
				return max(dfs(i - 1), dfs(i - 2) + arr[i])
			return dfs(n - 1)
		return max(nums[-1] + rob_w(nums[1:-1]), rob_w(nums[:-1]))

# 10.施咒的最大总伤害
class Solution1:
	def maximumTotalDamage(self, power):
		max_num = max(power) + 1
		a = [0] * max_num
		for x in power:
			a[x] += 10
		@cache
		def dfs(i):
			if i < 0:
				return 0
			return max(dfs(i - 1), dfs(i - 2), dfs(i - 3) + a[i])
		return dfs(max_num - 1)
class Solution3:
	def maximumTotalDamage(self, power):
		cnt = Counter(power)
		a = sorted(cnt.keys())
		@cache
		def dfs(i):
			if i < 0:
				return 0
			x = a[i]
			# j = i
			j = bisect_left(a, x - 2)
			# while j and a[j - 1] >= x - 2:
			# 	j -= 1
			return max(dfs(i - 1), dfs(j - 1) + x * cnt[x])
		return dfs(len(a) - 1)

# 11.最大子数组和
## 递归写法
class Solution1:
	def maxSubArray(self, nums):
		@cache
		def dfs(i):
			if i < 0:
				return 0
			return max(dfs(i - 1), 0) + nums[i]
		n = len(nums)
		return max(dfs(x) for x in range(n))
## 递推写法
class Solution2:
	def maxSubArray(self, nums):
		f0 = 0
		ans = -inf
		for i, c in enumerate(nums):
			# new_f = max(f0, 0) + c
			# f0 = new_f
			f0 = max(f0, 0) + c
			ans = max(ans, f0)
		return ans

## 前缀和写法
class Solution3:
	def maxSubArray(self, nums):
		pre_s = [0] * (len(nums) + 1)
		# for i, c in enumerate(nums):
		# 	pre_s[i + 1] = pre_s[i] + x
		ans = -inf
		temp_s = 0
		for i, c in enumerate(nums):
			temp_s += c
			ans = max(ans, temp_s - min(pre_s))
			# pre_s[i + 1] = pre_s[i] + c
			pre_s[i + 1] = temp_s
		return ans
## 前缀和写法优化
class Solution4:
	def maxSubArray(self, nums):
		ans = -inf
		min_pre_sum = 0
		temp_sum = 0
		for i, x in enumerate(nums):
			temp_sum += x
			ans = max(ans, temp_sum - min_pre_sum)
			min_pre_sum = min(min_pre_sum, temp_sum)
		return ans

# 12.找到最大开销的子字符串
class Solution1:
	def maximumCostSubstring(self, s, chars, vals):
		ori_a = ord('a') - 1
		chars_dic = defaultdict(int)
		for i, x in enumerate(chars):
			chars_dic[x] = vals[i]
		@cache
		def dfs(i):
			if i < 0:
				return 0
			if s[i] in chars:
				return max(dfs(i - 1), 0) + chars_dic[s[i]]
			else:
				return max(dfs(i - 1), 0) + ord(s[i]) - ori_a
		n = len(s)
		return max(dfs(x) for x in range(-1, n))
## 递推写法
class Solution2:
	def maximumCostSubstring(self, s, chars, vals):
		ori_a = ord('a') - 1
		chars_dic = defaultdict(int)
		for i, x in enumerate(chars):
			chars_dic[x] = vals[i]
		f0 = 0
		ans = 0
		for x in s:
			temp_num = ord(x) - ori_a if x not in chars else chars_dic[x]
			f0 = max(f0, 0) + temp_num
			ans = max(ans, f0)
		return ans
## 前缀和写法
class Solution3:
	def maximumCostSubstring(self, s, chars, vals):
		ori_a = ord('a') - 1
		chars_dic = defaultdict(int)
		for i, x in enumerate(chars):
			chars_dic[x] = vals[i]
		min_pre_sum = 0
		ans = 0
		temp_s = 0
		for x in s:
			temp_s += ord(x) - ori_a if x not in chars else chars_dic[x]
			ans = max(ans, temp_s - min_pre_sum)
			min_pre_sum = min(min_pre_sum, temp_s)
		return ans

# 13.k次串联后最大子数组之和
class Solution1:  # ——超出内存限制
	def kConcatenationMaxSum(self, arr, k):
		# new_arr = []
		# for _ in range(k):
		# 	new_arr.extend(arr)
		n = len(arr)
		mod = (10 ** 9) + 7
		@cache
		def dfs(i):
			if i < 0:
				return 0
			return max(dfs(i - 1), 0) + arr[i % n]
		return max(dfs(x) for x in range(-1, n * k)) % mod

## 前缀和写法——超出内存限制
class Solution2:
	def kConcatenationMaxSum(self, arr, k):
		mod = 10 ** 9 + 7
		n = len(arr)
		min_pre_sum = 0
		ans = 0
		temp_s = 0
		for i in range(n * k):
			temp_s += arr[i % n]
			ans = max(temp_s - min_pre_sum, ans)
			min_pre_sum = min(min_pre_sum, temp_s)
		return ans % mod
## 前缀和写法优化
class Solution3:
	def kConcatenationMaxSum(self, arr, k):
		mod = 10 ** 9 + 7
		s, max_s = 0, 0
		for x in arr * min(2, k):
			s = x if s < 0 else s + x  # 前缀和
			max_s = max(max_s, s)
		if k <= 2:
			return max_s % mod
		return (max(sum(arr), 0) * (k - 2) + max_s) % mod
## 前缀和写法优化2
class Solution3:
	def kConcatenationMaxSum(self, arr, k):
		mod = 10 ** 9 + 7
		min_pre_sum = 0
		ans = 0
		temp_s = 0
		for x in arr * min(k, 2):
			temp_s += x
			ans = max(ans, temp_s - min_pre_sum)
			min_pre_sum = min(min_pre_sum, temp_s)
		if k <= 2:
			return ans % mod
		return (max(sum(arr), 0) * (k - 2) + ans) % mod


## 递归写法
class Solution4:
	def kConcatenationMaxSum(self, arr, k):
		mod = 10 ** 9 + 7
		s = sum(arr)

		def maxSub(arr):
			n = len(arr)
			@cache
			def dfs(i):
				if i < 0:
					return 0
				return max(dfs(i - 1), 0) + arr[i]
			return max(dfs(x) for x in range(n))

		if k == 1:
			return max(0, maxSub(arr)) % mod
		else:
			return max(maxSub(arr + arr) + max(0, (k - 2) * s), 0) % mod

## 递推
class Solution4:
	def kConcatenationMaxSum(self, arr, k):
		mod = 10 ** 9 + 7
		s = sum(arr)

		def max_ditui(arr):
			f0 = 0
			ans = 0
			for x in arr:
				f0 = max(f0, 0) + x
				ans = max(f0, ans)
			return ans

		if k <= 2:
			return max(0, max_ditui(arr * k)) % mod
		else:
			return max(max_ditui(arr * 2) + max(0, (k - 2) * s), 0) % mod

############### 2.网格图DP
# 1.最小路径和
class Solution3:
	def minPathSum(self, grid):
		m, n = len(grid), len(grid[0])
		@cache
		def dfs(i, j):
			if i < 0 or j < 0:
				return inf
			elif i == 0 and j == 0:
				return grid[0][0]
			return min(dfs(i - 1, j), dfs(i, j - 1)) + grid[i][j]
		return dfs(m - 1, n - 1)
## 递推写法
class Solution1:
	def minPathSum(self, grid):
		m, n = len(grid), len(grid[0])
		f = [[inf] * (n + 1) for _ in range(m + 1)]
		for i, row in enumerate(grid):
			for j, x in enumerate(row):
				if i == j == 0:
					f[1][1] = x
				else:
					f[i + 1][j + 1] = min(f[i + 1][j], f[i][j + 1]) + x
		return f[-1][-1]

# 2.不同路径
class Solution1:
	def uniquePaths(self, m, n):
		@cache
		def dfs(i, j):
			if i < 0 or j < 0:
				return 0
			elif i == 0 and j == 0:
				return 1
			return dfs(i - 1, j) + dfs(i, j - 1)
		return dfs(m - 1, n - 1)
## 递推写法
class Solution2:
	def uniquePaths(self, m, n):
		f = [[0] * (n + 1) for _ in range(m + 1)]
		for i in range(m):
			for j in range(n):
				if i == 0 and j == 0:
					f[1][1] = 1
				else:
					f[i + 1][j + 1] = f[i][j + 1] + f[i + 1][j]
		return f[-1][-1]

# 3.不同路径2
class Solution1:
	def uniquePathsWithObstacles(self, grid):
		m, n = len(grid), len(grid[0])
		@cache
		def dfs(i, j):
			if i < 0 or j < 0:
				return 0
			else:
				c = grid[i][j]
				if c == 1:
					return 0
				else:
					if i == 0 and j == 0:
						return 1
					else:
						return dfs(i - 1, j) + dfs(i, j - 1)
		return dfs(m - 1, n - 1)

# 4.三角形最小路径和
class Solution1:
	def minimumTotal(self, triangle):
		n = len(triangle)
		@cache
		def dfs(i, j):
			if i == n:
				return 0
			return min(dfs(i + 1, j), dfs(i + 1, j + 1)) + triangle[i][j]
		return dfs(0,0)
## 递推写法——错解
class Solution1:
	def minimumTotal(self, triangle):
		n = len(triangle)
		f = []
		for i in range(n):
			f.append([0] * (i + 1))
		f[0][0] = triangle[0][0]
		for i in range(1, n):
			for j in range(i + 1):
				if j == 0:
					f[i][j] = f[i - 1][j] + triangle[i][j]
				else:
					f[i][j] = min(f[i - 1][j], f[i - 1][j - 1]) + triangle[i][j]
		return min(f[-1])
## 递推写法2
class Solution1:
	def minimumTotal(self, triangle):
		n = len(triangle)
		f = []
		for i in range(n):
			f.append([0] * (i + 1))
		for i in range(n - 1, -1, -1):
			for j in range(i + 1):
				if i == n - 1:
					f[i][j] = triangle[i][j]
				else:
					f[i][j] = min(f[i + 1][j], f[i + 1][j + 1]) + triangle[i][j]
		return f[0][0]

# 5.统计异或值为给定值的路径数目
class Solution1:
	def countPathsWithXorValue(self, grid, k):
		n, m = len(grid), len(grid[0])
		mod = 10 ** 9 + 7
		mx = max(map(max, grid))
		@cache
		def dfs(i, j, c):
			if i < 0 or j < 0:
				return 0
			elif i == 0 and j == 0:
				return 1 if c == grid[0][0] ^ k else 0
			c ^= grid[i][j]
			return (dfs(i - 1, j, c) + dfs(i, j - 1, c)) % mod
		return dfs(n - 1, m - 1, 0) % mod

# 6.下降路径最小和2
class Solution1:
	def minFallingPathSum(self, grid):
		n, m = len(grid), len(grid[0])
		@cache
		def dfs(i, j):
			if i == 0:
				return grid[i][j]
			return min(dfs(i - 1, x) for x in range(m) if x != j) + grid[i][j]
		return min(dfs(n - 1, y) for y in range(m))

# 7.机器人可以获得的最大金币数
class Solution1:  # 错解
	def maximumAmount(self, coins):
		c_lis = [0, 0]
		heapq.heapify(c_lis)
		n, m = len(coins), len(coins[0])
		@cache
		def dfs(i, j, c_lis):
			if i < 0 or j < 0:
				return -inf
			elif i == 0 and j == 0:
				if coins[0][0] >= 0:
					return coins[0][0]
				else:
					heapq.heappush(c_lis, -coins[0][0])
					return -heapq.heappop(c_lis)
			if coins[i][j] >= 0:
				return max(dfs(i - 1, j, c_lis), dfs(i, j - 1, c_lis)) + coins[i][j]
			else:
				heapq.push(c_lis, -coins[i][j])
				x = -heapq.heappop(c_lis)
				return max(dfs(i - 1, j, c_lis), dfs(i, j - 1, c_lis)) + x
		return dfs(n - 1, m - 1, c_lis)
## 灵神题解
class Solution2:  
	def maximumAmount(self, coins):
		n, m = len(coins), len(coins[0])
		@cache
		def dfs(i, j, k):
			if i < 0 or j < 0:
				return -inf
			elif i == 0 and j == 0:
				if k > 0:
					return max(coins[0][0], 0)
				else:
					return coins[0][0]
			if k > 0 and coins[i][j] < 0:
				return max(
					max(dfs(i - 1, j, k), dfs(i, j - 1, k)) + coins[i][j],
					max(dfs(i - 1, j, k - 1), dfs(i, j - 1, k - 1))
					)
			else:
				return max(dfs(i - 1, j, k), dfs(i, j - 1, k)) + coins[i][j]
		return dfs(n - 1, m - 1, 2)
## 递推写法
class Solution3:  
	def maximumAmount(self, coins):
		n, m = len(coins), len(coins[0])
		f = [[[-inf] * 3 for _ in range(m + 1)] for _ in range(n + 1)]
		f[0][1] = [0] * 3
		for i in range(n):
			for j, x in enumerate(coins[i]):
				f[i + 1][j + 1][0] = max(f[i][j + 1][0], f[i + 1][j][0]) + coins[i][j]  # 必须选
				f[i + 1][j + 1][1] = max(
					max(f[i][j + 1][1], f[i + 1][j][1]) + coins[i][j],  # 选
					max(f[i][j + 1][0], f[i + 1][j][0])  # 不选
					)
				f[i + 1][j + 1][2] = max(
					max(f[i][j + 1][2], f[i + 1][j][2]) + coins[i][j],  # 选
					max(f[i][j + 1][1], f[i + 1][j][1])  # 不选
					)
		return f[n - 1][m - 1][2]

########### 0-1背包
# 1.和为目标值的最长子序列长度
class Solution:
	def lengthOfLongestSubsequence(self, nums, target):
		n = len(nums)
		@cache
		def dfs(i, c):
			if i < 0:
				return 0 if c == 0 else -inf
			if nums[i] > c:  # 不加这个c可能会为负数，导致计算超出时间限制
				return dfs(i - 1, c)
			return max(dfs(i - 1, c), dfs(i - 1, c - nums[i]) + 1)
		ans = dfs(n - 1, target)
		dfs.cache_clear()
		return ans if ans > -1 else -1
## 
class Solution1:
	def lengthOfLongestSubsequence(self, nums, target):
		n = len(nums)
		f = [[-inf] * (target + 1) for _ in range(n + 1)]
		f[0][0] = 0
		for i, x in enumerate(nums):
			for c in range(target + 1):
				if c < x:
					f[i + 1][c] = f[i][c]
				else:
					f[i + 1][c] = max(f[i][c - x] + 1, f[i][c])
		ans = f[-1][-1]
		return ans if ans > -1 else -1

# 2.分割等和子集
class Solution1:
	def canPartition(self, nums):
		s = sum(nums)
		if s % 2 == 1:
			return False
		@cache
		def dfs(i, c):
			if i < 0:
				return True if c == 0 else False
			if c < nums[i]:
				return dfs(i - 1, c)
			return dfs(i - 1, c) or dfs(i - 1, c - nums[i])
		return dfs(len(nums) - 1, s // 2)


