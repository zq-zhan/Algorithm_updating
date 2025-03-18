# 1.打家劫舍
class Solution1:  # 贪心做法是错误的
	def rob(self, nums):
		choose_1 = 0
		choose_2 = 0
		for i, c in enumerate(nums):
			if i % 2 == 0:
				choose_1 += c
			else:
				choose_2 += c
		return max(choose_1, choose_2)
## 动态规划写法
class Solution2:
	def rob(self, nums):
		@cache
		def dfs(i):
			if i >= 2:
				return max(dfs(i - 1), dfs(i - 2) + nums[i])
			elif i == 1:
				return max(dfs(0), nums[1])
			else:
				return nums[0]

		n = len(nums)
		return dfs(n - 1)
## 灵神题解——动态规划
class Solution1:
	def rob(self, nums):
		n = len(nums)
		@cache
		def dfs(i):
			if i < 0:
				return 0
			return max(dfs(i - 1), dfs(i - 2) + nums[i])
		return dfs(n - 1)
## 递推写法
class Solution3:
	def rob(self, nums):
		n = len(nums)
		f = [0] * n
		f[0] = nums[0]
		for i in range(1, n):
			if i >= 2:
				f[i] = max(f[i - 1], f[i - 2] + nums[i])
			elif i == 1:
				f[i] = max(nums[0], nums[1])
		return f[n - 1]
## 灵神题解——递推写法优化
class Solution3:
	def rob(self, nums):
		n = len(nums)
		f = [0] * (n + 2)
		for i, c in enumerate(nums):
			f[i + 2] = max(f[i + 1], f[i] + c)
		return f[n + 1]
## 灵神题解——递推空间复杂度优化
class Solution4:
	def rob(self, nums):
		n = len(nums)
		f0 = f1 = 0
		for i, c in enumerate(nums):
			new_f = max(f1, f0 + c)
			f0 = f1
			f1 = new_f
		return f1

# 2.爬楼梯
class Solution1:
	def climbStairs(self, n):
		@cache
		def dfs(i):
			if i <= 1:
				return 1
			return dfs(i - 1) + dfs(i - 2)
		return dfs(n)
## 递推写法
class Solution2:
	def climbStairs(self, n):
		f = [0] * (n + 1)
		f[0] = 1
		f[1] = 1
		for i in range(2, n + 1):
			f[i] = f[i - 1] + f[i - 2]
		return f[n]
## 空间优化
class Solution3:
	def climbStairs(self, n):
		f0 = f1 = 1
		for _ in range(n + 1):
			new_f = f0 + f1
			f0 = f1
			f1 = new_f
		return new_f

# 3.使用最小花费爬楼梯
class Solution1:
	def minCostClimbingStairs(self, cost):
		cost.append(0)
		n = len(cost)
		@cache
		def dfs(i):
			if i < 0:
				return 0
			return min(dfs(i - 1) + cost[i - 1], dfs(i - 2) + cost[i - 2])
		return dfs(n - 1)
## 递推写法
class Solution2:
	def minCostClimbingStairs(self, cost):
		cost.append(0)
		f0 = f1 = 0
		for i in range(len(cost) - 1):
			new_f = min(f0 + cost[i], f1 + cost[i + 1])
			f0 = f1
			f1 = new_f
		return f1
## 优化
class Solution3:
	def minCostClimbingStairs(self, cost):
		n = len(cost)
		f0 = f1 = 0
		for i in range(1, n):
			new_f = min(f0 + cost[i - 1], f1 + cost[i])  # 这样就可以选到cost[i - 1]
			f0 = f1
			f1 = new_f
		return f1

# 4.组合总和4
class Solution1:
	def combinationSum4(self, nums, target):
		@cache
		def dfs(i):
			if i == 0:
				return 1
			# else:
			# 	ori = 0
			# 	for x in nums:
			# 		ori += dfs(i - x) if i >= x else 0
			# 	return ori
			return sum(dfs(i - x) for x in nums if i >= x)
		return dfs(target)
## 递推
class Solution2:
	def combinationSum4(self, nums, target):
		f = [0] * (target + 1)
		f[0] = 1
		for i in range(1, target + 1):
			for x in nums:
				f[i] += f[i - x] if i >= x else 0
		return f[-1]
## 递推空间优化(错解)
class Solution3:
	def combinationSum4(self, nums, target):
		f0 = 0
		f1 = 1
		for i in range(1, target + 1):
			new_f = 0
			for x in nums:
				new_f += f1 if i >= x else 0
			f0 = f1
			f1 = new_f
		return f1

# 5.统计构造好字符串的方案数
class Solution1:
	def countGoodStrings(self, low, high, zero, one):
		mod = (10 ** 9 + 7)
		@cache
		def dfs(i):
			if i == 0:
				return 1
			elif i < 0:
				return 0
			return (dfs(i - zero) + dfs(i - one)) % mod
		ans = 0
		for num in range(low, high + 1):
			ans += dfs(num)
		return ans % mod
## 递推写法
class Solution2:
	def countGoodStrings(self, low, high, zero, one):
		ans = 0
		for num in range(low, high + 1):
			f = [0] * (num + 1)
			f[0] = 1
			for i in range(1, num + 1):
				f[i] += f[i - zero] if i >= zero else 0
				f[i] += f[i - one] if i >= one else 0
			ans += f[-1]
		return ans % (10 ** 9 + 7)
## 优化
class Solution3:
	def countGoodStrings(self, low, high, zero, one):
		mod = (10 ** 9 + 7)
		f = [0] * (high + 1)
		f[0] = 1
		for i in range(1, high + 1):
			if i >= zero:
				f[i] += f[i - zero]
			if i >= one:
				f[i] = (f[i] + f[i - one]) % mod
		return sum(f[low:]) % mod

# 6.统计打字方案数
class Solution1:
	def countTexts(self, pressedKeys):
		mod = (10 ** 9 + 7)
		n = len(pressedKeys)
		same_lis = []
		left = 0
		for right in range(n - 1):
			if pressedKeys[right] == pressedKeys[right + 1]:
				continue
			same_lis.append([pressedKeys[left], right - left + 1])
			left = right + 1
		same_lis.append([pressedKeys[left], n - left])
		@cache
		def dfs(i, x):
			if i == 0:
				return 1
			elif i < 0:
				return 0
			return sum(dfs(i - j, x) for j in range(1, x)) % mod

		ans = 1
		for char, num in same_lis:
			if char in ('7', '9'):
				ans = (ans * dfs(num, 5)) % mod
			else:
				ans = (ans * dfs(num, 4)) % mod
		return ans % mod
## 递推
class Solution2:
	def countTexts(self, pressedKeys):
		mod = (10 ** 9 + 7)
		n = len(pressedKeys)
		same_lis = []
		left = 0
		for right in range(n - 1):
			if pressedKeys[right] == pressedKeys[right + 1]:
				continue
			same_lis.append([pressedKeys[left], right - left + 1])
			left = right + 1
		same_lis.append([pressedKeys[left], n - left])

		ans = 1
		for char, num in same_lis:
			f = [1] + [0] * num
			for i in range(1, num + 1):
				if char in ('7', '9'):
					f[i] = sum(f[i - j] for j in range(1, 5) if i >= j) % mod
				else:
					f[i] = sum(f[i - j] for j in range(1, 4) if i >= j) % mod
			ans = (ans * f[-1]) % mod
		return ans % mod

# 7.打家劫舍2
class Solution1:  # （错解）
	def rob(self, nums):
		n = len(nums)
		tag = True
		@cache
		def dfs(i):
			if i <= 0:
				return 0
			if tag:
				return max(dfs(i - 1) + nums[0], dfs(i - 2) + nums[i])
			else:
				return max(dfs(i - 1), dfs(i - 2) + nums[i])
			tag = False
		return dfs(n - 1)
## 递推写法(错解)
class Solution2:
	def rob(self, nums):
		n = len(nums)
		f = [0] * n
		f[0] = nums[0]
		f[1] = max(nums[1], f[0])
		for i in range(2, n):
			f[i] = max(f[i - 1], f[i - 2] + nums[i])
## 灵神题解
class Solution3:
	def rob(self, nums):
		def rob_normal(nums):
			f0 = f1 = 0
			for x in nums:
				new_f = max(f1, f0 + x)
				f0 = f1
				f1 = new_f
			return f1
		ans = max(nums[0] + rob_normal(nums[2:-1]), rob_normal(nums[1:]))
		return ans
## 递归写法
class Solution4:
	def rob(self, nums):
		def rob_normal(nums):
			n = len(nums)
			@cache
			def dfs(i):
				if i < 0:
					return 0
				return max(dfs(i - 1), dfs(i - 2) + nums[i])
			return dfs(n - 1)
		ans = max(nums[0] + rob_normal(nums[2:-1]), rob_normal(nums[1:]))
		return ans

# 8.删除并获得点数
## 值域数组
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
## 递推写法
class Solution2:
	def deleteAndEarn(self, nums):
		n = max(nums) + 1
		a = [0] * n
		for x in nums:
			a[x] += x
		f = [0] * n
		f[0] = 0
		f[1] = max(f[0], a[1])
		for i in range(2, n):
			f[i] = max(f[i - 1], f[i - 2] + a[i])
		return f[-1]
## 递推空间优化
class Solution3:
	def deleteAndEarn(self, nums):
		n = max(nums) + 1
		a = [0] * n
		for x in nums:
			a[x] += x
		f0 = f1 = 0
		for x in a:
			new_f = max(f1, f0 + x)
			f0 = f1
			f1 = new_f
		return f1

# 9.统计放置房子的方式数
class Solution1:
	def countHousePlacements(self, n):
		mod = (10 ** 9 + 7)
		@cache
		def dfs(i):
			if i < 0:
				return 0
			elif i == 0:
				return 1
			elif i == 1:
				return 2
			return dfs(i - 1) + dfs(i - 2)
		ans = dfs(n) % mod
		return (ans * ans) % mod
## 递推
class Solution2:
	def countHousePlacements(self, n):
		mod = (10 ** 9 + 7)
		f = [0] * (n + 1)
		f[0] = 1
		f[1] = 2
		for i in range(2, n + 1):
			f[i] = (f[i - 1] + f[i - 2]) % mod
		return f[-1] ** 2 % mod

# 10.施咒的最大总伤害
class Solution1:
	def maximumTotalDamage(self, power):
		n = max(power) + 1
		a = [0] * n
		for x in power:
			a[x] += x
		@cache
		def dfs(i):
			if i < 0:
				return 0
			return max(dfs(i - 1), dfs(i - 2), dfs(i - 3) + a[i])
		return dfs(n - 1)
## 递推写法
class Solution2:
	def maximumTotalDamage(self, power):
		n = max(power) + 1
		a = [0] * n
		for x in power:
			a[x] += x
		if n < 3:
			return max(a[:n])

		f = [0] * n
		f[0] = a[0]
		f[1] = max(a[0], a[1])
		f[2] = max(a[0], a[1], a[2])
		for i in range(3, n):
			f[i] = max(f[i - 1], f[i - 2], f[i - 3] + a[i])
		return f[-1] 		
## 灵神题解
class Solution3:
	def maximumTotalDamage(self, power):
		cnt = defaultdict(int)
		for x in power:
			cnt[x] += 1
		a = sorted(cnt.keys())
		@cache
		def dfs(i):
			if i < 0:
				return 0
			x = a[i]
			j = bisect_left(a, x - 2)
			# while j and a[j - 1] >= x - 2:
			# 	j -= 1
			return max(dfs(i - 1), dfs(j - 1) + x * cnt[x])
		return dfs(len(a) - 1)
## 递推解法
class Solution4:
	def maximumTotalDamage(self, power):
		cnt = defaultdict(int)
		for x in power:
			cnt[x] += 1
		a = sorted(cnt.keys())
		f = [0] * (len(a) + 1)

		# j = 0
		for i, c in enumerate(a):
			# while a[j] < c - 2:
			# 	j += 1
			j = bisect_left(a, c - 2)
			f[i + 1] = max(f[i], f[j] + c * cnt[c])
		return f[-1]

################## 最大子数组和
# 1.最大子数组和
## 递归写法
class Solution1:
	def maxSubArray(self, nums):
		n = len(nums)
		@cache
		def dfs(i):
			if i < 0:
				return 0
			return max(dfs(i - 1), 0) + nums[i]
		return max(dfs(j) for j in range(n))
## 递推
class Solution2:
	def maxSubArray(self, nums):
		n = len(nums)
		f = [0] * n
		f[0] = nums[0]
		for i in range(1, n):
			f[i] = max(f[i - 1], 0) + nums[i]
		return max(f)
## 递推空间优化
class Solution3:
	def maxSubArray(self, nums):
		ans = -inf
		f0 = 0
		for x in nums:
			f0 = max(f0, 0) + x
			ans = max(ans, f0)
		return ans
		# ans = f0 = nums[0]
		# for i in range(1, len(nums)):
		# 	f1 = max(f0, 0) + nums[i]
		# 	ans = max(ans, f1)
		# 	f0 = f1
		# return f0
## 前缀和
class Solution4:
	def maxSubArray(self, nums):  # 复杂度O(n^2)
		sub_pre = [0] * (len(nums) + 1)
		temp_sum = 0
		ans = -inf
		for i, x in enumerate(nums):
			temp_sum += x
			ans = max(ans, temp_sum - min(sub_pre))
			sub_pre[i + 1] = temp_sum
		return ans
## 前缀和优化
class Solution5:
	def maxSubArray(self, nums):
		ans = -inf
		min_pre_sum = 0
		temp_sum = 0
		for i, x in enumerate(nums):
			temp_sum += x
			ans = max(ans, temp_sum - min_pre_sum)
			min_pre_sum = min(min_pre_sum, temp_sum)
		return ans

# 2.找到最大开销的子字符串
class Solution1:
	def maximumCostSubstring(self, s, chars, vals):
		ori = ord('a') - 1
		n = len(s)
		chars_value = defaultdict(int)
		for i, c in enumerate(chars):
			chars_value[c] = vals[i]
		@cache
		def dfs(i):
			if i < 0:
				return 0
			# if s[i] in chars:
			# 	temp_sum = chars_value[s[i]]
			temps_num = ord(s[i]) - ori if s[i] not in chars else chars_value[s[i]]
			return max(dfs(i - 1), 0) + temps_num
		return max(dfs(j) for j in range(n))
## 递推
class Solution2:
	def maximumCostSubstring(self, s, chars, vals):
		ori = ord('a') - 1
		n = len(s)
		chars_value = defaultdict(int)
		for i, c in enumerate(chars):
			chars_value[c] = vals[i]
		f = [0] * (n + 1)
		for i in range(n):
			temps_num = ord(s[i]) - ori if s[i] not in chars else chars_value[s[i]]
			f[i + 1] = max(f[i], 0) + temps_num
		return max(f)
## 递推空间优化
class Solution3:
	def maximumCostSubstring(self, s, chars, vals):
		ori = ord('a') - 1
		n = len(s)
		chars_value = defaultdict(int)
		for i, c in enumerate(chars):
			chars_value[c] = vals[i]
		ans = -inf
		f0 = 0
		for i in range(n):
			temps_num = ord(s[i]) - ori if s[i] not in chars else chars_value[s[i]]
			f0 = max(f0, 0) + temps_num
			ans = max(f0, ans)
		return max(ans, 0)
## 前缀和做法
class Solution4:
	def maximumCostSubstring(self, s, chars, vals):
		ori = ord('a') - 1
		n = len(s)
		chars_value = defaultdict(int)
		for i, c in enumerate(chars):
			chars_value[c] = vals[i]
		min_pre_sum = 0
		temp_sum = 0
		ans = -inf
		for i, c in enumerate(s):
			temp_sum += ord(s[i]) - ori if s[i] not in chars else chars_value[s[i]]
			ans = max(ans, temp_sum - min_pre_sum)
			min_pre_sum = min(min_pre_sum, temp_sum)
		return max(ans, 0)

#################### 网格图DP ###################
# 1.最小路径和
class Solution1:
	def minPathSum(self, grid):
		m, n = len(grid), len(grid[0])
		@cache
		def dfs(i, j):
			if i == 0 and j == 0:
				return grid[0][0]
			elif i < 0 or j < 0:
				return inf
			return min(dfs(i - 1, j), dfs(i, j - 1)) + grid[i][j]
		return dfs(m - 1, n - 1)
## 递推写法
class Solution2:
	def minPathSum(self, grid):
		m, n = len(grid), len(grid[0])
		f = [[inf] * (n + 1) for _ in range(m + 1)]
		for i, row in enumerate(grid):
			for j, x in enumerate(row):
				if i == j == 0:
					f[1][1] == x
				else:
					f[i + 1][j + 1] = min(f[i + 1][j], f[i][j + 1]) + x
		return f[m][n]

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
		return f[m][n]

# 3.不同路径2
class Solution1:
	def uniquePathsWithObstacles(self, obstacleGrid):
		m, n = len(obstacleGrid), len(obstacleGrid[0])
		@cache
		def dfs(i, j):
			if i < 0 or j < 0 or obstacleGrid[i][j] == 1:
				return 0
			elif i == 0 and j == 0:
				return 1
			return dfs(i - 1, j) + dfs(i, j - 1)
		return dfs(m - 1, n - 1)

# 4.三角形最小路径和
class Solution1:
	def minimumTotal(self, triangle):
		m = len(triangle)
		@cache
		def dfs(i, j):
			if i > m:
				return 0
			return min(dfs(i + 1, j), dfs(i + 1, j + 1)) + triangle[i][j]
		return dfs(0, 0)
## 递推
class Solution2:
    def minimumTotal(self, triangle):
        n = len(triangle)
        f = [[0] * (i + 1) for i in range(n)]
        f[-1] = triangle[-1]
        for i in range(n - 2, -1, -1):
            for j, x in enumerate(triangle[i]):
                f[i][j] = min(f[i + 1][j], f[i + 1][j + 1]) + x
        return f[0][0]

# 5.统计异或值为给定值的路径数目
class Solution1:
	def countPathsWithXorValue(self, grid, k):
		@cache
		def dfs(i, j, ans):
			if i == 0 and j == 0:
				if ans ^ grid[i][j] == k:
					return 1
				else:
					return 0
			elif i < 0 and j < 0:
				return 0
			return dfs(i - 1, j, ans ^ grid[i][j]) + dfs(i , j - 1, ans ^ grid[i][j])
		m, n = len(grid), len(grid[0])
		return dfs(m - 1, n - 1, 0)
## 灵神递归：定义dfs(i, j, x)为递归到i，j时路径异或值为x的方案数
class Solution2:
	def countPathsWithXorValue(self, grid, k):
		mod = (10 ** 9 + 7)
		@cache
		def dfs(i, j, x):
			if i == j == 0:
				return 1 if x == grid[0][0] else 0
			elif i < 0 or j < 0:
				return 0
			val = grid[i][j]
			return (dfs(i - 1, j, x ^ val) + dfs(i, j - 1, x ^ val)) % mod
		m, n = len(grid), len(grid[0])
		return dfs(m - 1, n - 1, k) % mod
## 递推
class Solution3:
    def countPathsWithXorValue(self, grid, k):
        MOD = 1_000_000_007
        u = 1 << max(map(max, grid)).bit_length()
        # if k >= u:
        #     return 0

        m, n = len(grid), len(grid[0])
        f = [[[0] * u for _ in range(n + 1)] for _ in range(m + 1)]
        f[0][1][0] = 1
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                for x in range(u):
                    f[i + 1][j + 1][x] = (f[i + 1][j][x ^ val] + f[i][j + 1][x ^ val]) % MOD
        return f[m][n][k]

# 6.下降路径最小和
class Solution1:
	def minFallingPathSum(self, matrix):
		n = len(matrix)
		@cache
		def dfs(i, j):
			if i < 0 or j >= n or j < 0:
				return inf
			elif i == 0 and j < n:
				return matrix[i][j]
			return min(dfs(i - 1, j - 1), dfs(i - 1, j), dfs(i - 1, j + 1)) + matrix[i][j]
		return min(dfs(n - 1, x) for x in range(n))
## 递推
class Solution2:
	def minFallingPathSum(self, matrix):
		n = len(matrix)
		f = [[0] * n for _ in range(n)]
		f[0] = matrix[0]
		for i in range(1, n):
			for j in range(n):
				if j == 0:
					f[i][j] = min(f[i - 1][j], f[i - 1][j + 1]) + matrix[i][j]
				elif j == n - 1:
					f[i][j] = min(f[i - 1][j - 1], f[i - 1][j]) + matrix[i][j]
				else:
					f[i][j] = min(f[i - 1][j - 1], f[i - 1][j], f[i - 1][j + 1]) + matrix[i][j]
		return min(f[-1])

# 7.矩阵中移动的最大次数
class Solution1:
	def maxMoves(self, grid):  # 错解
		m, n = len(grid), len(grid[0])
		@cache
		def dfs(i, j, val):
			if 0 <= i < m and val >= grid[i][j]:
				return 0
			else:
				if i < 0 or i > m - 1 or j >= n - 1:
					return 0
				# elif j == n - 1:
				# 	return 1
				new_val = grid[i][j]
				return max(dfs(i - 1, j + 1, new_val), dfs(i, j + 1, new_val), dfs(i + 1, j + 1, new_val)) + 1
		return max(dfs(x, 0, 0) for x in range(n))
## 灵神题解
class Solution2:
	def maxMoves(self, grid):
		m, n = len(grid), len(grid[0])
		ans = 0
		def dfs(i, j):
			nonlocal ans
			ans = max(ans, j)
			if ans == n - 1:
				return
			for k in (i - 1, i, i + 1):
				if 0 <= k < m and grid[k][j + 1] > grid[i][j]:
					dfs(k, j + 1)
			grid[i][j] = 0
		for i in range(m):
			dfs(i, 0)
		return ans
## 灵神题解——递推（BFS——广度优先搜索）
class Solution3:
	def maxMoves(self, grid):
		m, n = len(grid), len(grid[0])
		vis = [-1] * m
		q = range(m)
		for j in range(n - 1):
			tmp = q
			q = []
			for i in tmp:
				for k in (i - 1, i, i + 1):
					if 0 <= k < m and vis[k] != j and grid[k][j + 1] > grid[i][j]:
						vis[k] = j
						q.append(k)
			if not q:
				return j
		return n - 1

# 8.网格中的最小路径代价
class Solution1:
	def minPathCost(self, grid, moveCost):
		m, n = len(grid), len(grid[0])
		@cache
		def dfs(i, j):
			if i == m - 1:
				return grid[i][j]
			val = grid[i][j]
			return min(dfs(i + 1, x) + grid[i][j] + moveCost[val][x] for x in range(n))
		return min(dfs(0, c) for c in range(n))
## 递推写法
class Solution2:
	def minPathCost(self, grid, moveCost):
		m, n = len(grid), len(grid[0])
		f = [[inf] * n for _ in range(m)]
		f[-1] = grid[-1]
		for i in range(m - 2, -1, -1):
			for j, c in enumerate(grid[i]):
				for k, cost in enumerate(moveCost[c]):
					f[i][j] = min(f[i][j], f[i + 1][k] + cost)
				f[i][j] += c
		return min(f[0])
## 原地修改（空间复杂度O(1)）
class Solution3:
	def minPathCost(self, grid, moveCost):
		m, n = len(grid), len(grid[0])
		for i in range(m - 2, -1, -1):
			for j in range(n):
				grid[i][j] += min(g + c for g, c in zip(grid[i + 1], moveCost[grid[i][j]]))
		return min(grid[0])

# 9.下降路径最小和2
class Solution1:
	def minFallingPathSum(self, grid):
		m, n = len(grid), len(grid[0])
		@cache
		def dfs(i, j):
			if i == 0:
				return grid[i][j]
			return min(dfs(i - 1, x) for x in range(n) if x != j) + grid[i][j]
		return min(dfs(m - 1, c) for c in range(n))

################# 背包 ################
# 1.和为目标值的最长子序列长度
class Solution1:
	def lengthOfLongestSubsequence(self, nums, target):
		








