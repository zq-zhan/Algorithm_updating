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


