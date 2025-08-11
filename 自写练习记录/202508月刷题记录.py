# 1.20250801杨辉三角
class Solution:
	def generate(self, numRows):
		ans = [[1]]
		for i in range(2, numRows + 1):
			path = [0] * i
			for j in range(0, i):
				if j == 0:
					path[j] = ans[-1][0]
				elif j == i - 1:
					path[j] = ans[-1][-1]
				else:
					path[j] = ans[-1][j - 1] + ans[-1][j]
			ans.append(path)
		return ans
## 灵神题解
class Solution:
	def generate(self, numRows):
		ans = [[1] * (i + 1) for i in range(numRows)]
		for i in range(2, numRows):
			for j in range(1, i):
				ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]
		return ans

# 2.爬楼梯
class Solution:
	def climbStairs(self, n):
		@cache
		def dfs(i):
			if i == 0:
				return 1
			if i < 0:
				return 0
			return dfs(i - 1) + dfs(i - 2)
		return dfs(n)

# 3.使用最小花费爬楼梯
class Solution:
	def minCostClimbingStairs(self, cost):
		n = len(cost)
		@cache
		def dfs(i):
			if i >= n:
				return 0
			return min(dfs(i + 1), dfs(i + 2)) + cost[i]
		return min(dfs(0), dfs(1))

# 4.20250802重排水果
class Solution:
	def minCost(self, basket1, basket2):
		basket1_dic = Counter(basket1)
		basket2_dic = Counter(basket2)
		if len(basket1_dic) != len(basket2_dic):
			return -1

		trans1 = sorted(list(basket1_dic.keys()))
		trans2 = sorted(list(basket2_dic.keys()))

		for key, cnt in basket1_dic.items():
			if cnt == basket2_dic[key]:
				del basket1_dic[key]
				del basket2_dic[key]
			else:
				basket1_dic[key] //= 2
## 灵神题解——贪心
class Solution:
	def minCost(self, basket1, basket2):
		cnt = defaultdict(int)
		for x, y in zip(basket1, basket2):
			cnt[x] += 1
			cnt[y] -= 1  # 交集元素互相抵消

		a, b = [], []
		for x, c in cnt.items():
			if c % 2:  # 奇数无法均分
				return -1
			if c > 0:  # 剩余元素一半放入a或b
				a.extend([x] * (c // 2))
			else:
				b.extend([x] * (-c // 2))
		a.sort()
		b.sort(reverse = True)
		mn = min(cnt)
		return sum(min(x, y, mn*2) for x, y in zip(a, b))

# 5.组合总和4
class Solution:
	def combinationSum4(self, nums, target): 
		@cache
		def dfs(i, path_s):  # 但是i并没有用到，所以可以简化
			if path_s == target:
				return 1
			elif path_s > target:
				return 0
			return sum(dfs(i + 1, path_s + x) for x in nums)
		return dfs(0, 0)
## 灵神题解,复杂度：O(target * n) 状态个数*单个状态的计算时间
class Solution:
	def combinationSum4(self, nums, target):
		@cache
		def dfs(i):
			if i == 0:
				return 1
			elif i < 0:
				return 0
			return sum(dfs(i - x) for x in nums)
		return dfs(target)

# 6.打家劫舍
class Solution:
	def rob(self, nums):
		n = len(nums)
		@cache
		def dfs(i):
			if i < 0:
				return 0
			return max(dfs(i - 1), dfs(i - 2) + nums[i])
		return dfs(n - 1)
## 记忆化搜索的原代码
class Solution:
	def rob(self, nums):
		n = len(nums)
		cache = [-1] * n
		def dfs(i):
			if i < 0:
				return 0
			if cache[i] != -1:
				return cache[i]
			res = max(dfs(i - 1), dfs(i - 2) + nums[i])
			cache[i] = res
			return res
		return dfs(n - 1)
## 递推写法，O(n)空间复杂度
class Solution:
	def rob(self, nums):
		n = len(nums)
		f = [0] * (n + 2)
		for i, x in enumerate(nums):
			f[i + 2] = max(f[i + 1], f[i] + x)
		return f[-1]
## 递推写法，O(1)空间复杂度
class Solution:
	def rob(self, nums):
		n = len(nums)
		f0 = f1 = 0
		for i, x in enumerate(nums):
			newF = max(f1, f0 + x)
			f0 = f1
			f1 = newF
		return newF

# 7.打家劫舍2
class Solution:
	def rob(self, nums):
		def rob_ori(nums):
			n = len(nums)
			@cache
			def dfs(i):
				if i < 0:
					return 0
				return max(dfs(i - 1), dfs(i - 2) + nums[i])
			return dfs(n - 1)
		return max(nums[-1] + rob_ori(nums[1:-2]), rob_ori(nums[:-1]))

# 8.统计放置房子的方式数
class Solution:
	def countHousePlacements(self, n):
		mod = 10 ** 9 + 7
		@cache
		def dfs(i):
			if i < 0:
				return 1
			return dfs(i - 1) + dfs(i - 2)
		ans = dfs(n - 1)
		return ans ** 2 % mod
## 递推写法
class Solution:
	def countHousePlacements(self, n):
		mod = 10 ** 9 + 7
		f = [0] * (n + 2)
		f[0] = f[1] = 1
		for i in range(n):
			f[i + 2] = f[i + 1] + f[i]
		return f[-1] ** 2 % mod
## 递推空间复杂度优化
class Solution:
	def countHousePlacements(self, n):
		mod = 10 ** 9 + 7
		f0 = f1 = 1
		for i in range(n):
			newF = f0 + f1
			f0 = f1
			f1 = newF
		return f1 ** 2 % mod

# 9.删除并获得点数
class Solution:
	def deleteAndEarn(self, nums):
		mn, mx = min(nums), max(nums)
		new_num = list(range(mn, mx + 1))
		n = mx - mn + 1
		nums = Counter(nums)
		@cache
		def dfs(i):
			if i < 0:
				return 0
			x = new_num[i]
			return max(dfs(i - 1), dfs(i - 2) + x * nums[x])
		return dfs(n - 1)
## 灵神题解——值域打家劫舍
class Solution:
	def deleteAndEarn(self, nums):
		new_arr = [0] * (max(nums) + 1)
		for x in nums:
			new_arr[x] += x
		n = len(new_arr)
		@cache
		def dfs(i):
			if i < 0:
				return 0
			return max(dfs(i - 1), dfs(i - 2) + new_arr[i])
		return dfs(n - 1)

# 10.施咒的最大总伤害
class Solution:
	def maximumTotalDamage(self, power):
		mn, mx = min(power), max(power)
		new_arr = [0] * (mx - mn + 1)
		for x in power:
			new_arr[x] += x
		@cache
		def dfs(i):
			if i < 0:
				return 0
			return max(dfs(i - 1), dfs(i - 3) + new_arr[i])
		return dfs(mx - mn)
class Solution:
	def maximumTotalDamage(self, nums):
		mn, mx = min(nums), max(nums)
		new_num = list(range(mn, mx + 1))
		n = mx - mn + 1
		nums = Counter(nums)
		@cache
		def dfs(i):
			if i < 0:
				return 0
			x = new_num[i]
			return max(dfs(i - 1), dfs(i - 3) + x * nums[x])
		return dfs(n - 1)
## 递推写法
class Solution:
	def maximumTotalDamage(self, power):
		new_arr = [0] * (max(power) + 1)
		for x in power:
			new_arr[x] += x
		n = len(new_arr)
		f0 = f1 = f2 = 0
		for i, x in enumerate(new_arr):
			newF = max(f2, f0 + x)
			f0 = f1
			f1 = f2
			f2 = newF
		return f2
## 灵神优化
class Solution:
	def maximumTotalDamage(self, power):
		cnt = Counter(power)
		new_set = sorted(cnt.keys())
		n = len(new_set)
		@cache
		def dfs(i):
			if i < 0:
				return 0
			x = new_set[i]
			# j = i
			# while j and new_set[j - 1] >= x - 2:
			# 	j -= 1
			j = bisect_left(new_set, x - 2)
			return max(dfs(i - 1), dfs(j - 1) + x * cnt[x])
		return dfs(n - 1)
## 递推
class Solution:
	def maximumTotalDamage(self, power):
		cnt = defaultdict(int)
		for x in power:
			cnt[x] += 1
		new_arr = sorted(cnt.keys())
		f = [0] * (len(new_arr) + 1)
		for i, x in enumerate(new_arr):
			j = bisect_left(new_arr, x - 2)
			f[i + 1] = max(f[i], f[j] + x * cnt[x])  # dfs(i) = max(dfs(i - 1), dfs(j - 1) + x * cnt[x])变换而来
		return f[-1]

# 11.施咒的最大总伤害
class Solution:
	def countGoodStrings(self, low, high, zero, one):
		mod = 10 ** 9 + 7
		@cache
		def dfs(i):
			if i == 0:
				return 1
			elif i < 0:
				return 0
			return (dfs(i - zero) + dfs(i - one)) % mod
		ans = 0
		for length in range(low, high + 1):
			ans = (ans + dfs(length)) % mod
		return ans

# 12.20250803摘水果
class Solution:  # O(2 ** k) 超时
	def maxTotalFruits(self, fruits, startPos, k):
		mx = max(x[0] for x in fruits)
		fruits_lis = [0] * (mx + 1)
		for order, cnt in fruits:
			fruits_lis[order] += cnt	
		ans = path = 0
		def dfs(i, k):
			nonlocal ans, path
			if not (0 <= i <= mx) or k < 0:
				return
			x = fruits_lis[i]
			path += x
			fruits_lis[i] = 0
			ans = max(ans, path)

			dfs(i - 1, k - 1)
			dfs(i + 1, k - 1)

			# 回溯
			path -= x
			fruits_lis[i] = x
		dfs(startPos, k)
		return ans
## 灵神题解——滑动窗口
class Solution:  
	def maxTotalFruits(self, fruits, startPos, k):
		left = bisect_left(fruits, [startPos - k])  # 向左最远能走到的id
		right = bisect_left(fruits, [startPos + 1])  # 位置 <= startPos的最大下标+1
		ans = s = sum(f[1] for f in fruits[left:right])
		while right < len(fruits) and fruits[right][0] <= startPos + k:
			s += fruits[right][1]
			while fruits[right][0] * 2 - fruits[left][0] - startPos > k and \
				fruits[right][0] - fruits[left][0] * 2 + startPos > k:
				s -= fruits[left][1]
				left += 1
			ans = max(ans, s)
			right += 1
		return ans
## 二分+前缀和
class Solution:
   def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
       n = len(fruits)
       cnt = [fruits[i][1] for i in range(n)]
       cnt = list(accumulate(cnt, initial=0)) # 前缀和
       pos = [fruits[i][0] for i in range(n)]
       ans = 0
       def cal(l, r):
           nonlocal ans
           lpos, rpos = startPos - l, startPos + r # 此时能走到的左右端点
           idxl = bisect.bisect_left(pos, lpos)
           idxr = bisect.bisect(pos, rpos)
           ans = max(ans, cnt[idxr] - cnt[idxl])
       # 向左走再折回
       for l in range(0, k // 2 + 1):
           r = k - 2 * l
           cal(l, r)
       # 向右走再折回
       for r in range(0, k // 2 + 1):
           l = k - 2 * r
           cal(l, r)
       return ans

# 13.统计打字方案数
## 灵神题解——分组爬楼梯
class Solution:
	def countTexts(self, pressedKeys):
		mod = 10 ** 9 + 7
		ans = 1
		@cache
		def dfs(i, num):
			if i < 0:
				return 0
			elif i == 0:
				return 1
			if num not in {7, 9}:
				return sum(dfs(i - j, num) for j in range(1, 4))
			else:
				return sum(dfs(i - j, num) for j in range(1, 5))
		for x, group in groupby(pressedKeys):
			nums = list(group)
			ans = ans * dfs(len(nums), int(x)) % mod
		return ans

# 14.最大子数组和
class Solution:
	def maxSubArray(self, nums):
		n = len(nums)
		@cache
		def dfs(i):
			if i < 0:
				return 0
			return max(nums[i], dfs(i - 1) + nums[i])
		return max(dfs(i) for i in range(n))

# 15.水果成篮
## 最大子数组和的dp
class Solution:
	def totalFruit(self, fruits):
		n = len(fruits)
		@cache
		def dfs(i, pre1, pre2):
			if i == n:
				return 0
			x = fruits[i]
			if pre1 == -1 or x == pre1:
				return 1 + dfs(i + 1, x, pre2)
			elif pre2 == -1 or x == pre2:
				return 1 + dfs(i + 1, pre1, x)
			else:
				return 0
		return max(dfs(i, -1, -1) for i in range(n))
## 滑动窗口
class Solution:
	def totalFruit(self, fruits):
		dic_win = defaultdict(int)
		left = 0
		ans = 0
		for right, x in enumerate(fruits):
			dic_win[x] += 1
			while len(dic_win) > 2:
				if dic_win[fruits[left]] == 1:
					del dic_win[fruits[left]]
				else:
					dic_win[fruits[left]] -= 1
				left += 1
			ans = max(ans, right - left + 1)
		return ans 

# 16.环形子数组的最大和
class Solution:
	def maxSubarraySumCircular(self, nums):
		n = len(nums)
		nums = nums + nums
		@cache
		def dfs(i, x):
			if i != n and i % n == x:
				return 0
			return max(nums[i % n], dfs(i - 1, x) + nums[i % n])
		return max(dfs(i + n, i) for i in range(n))
## 灵神题解
class Solution:
	def maxSubarraySumCircular(self, nums):
		## 分类讨论
		max_s = -inf  # 最大子数组和
		min_s = 0  # 最小子数组和
		max_f = min_f = 0
		for x in nums:
			max_f = max(max_f, 0) + x
			max_s = max(max_s, max_f)
			min_f = min(min_f, 0) + x
			min_s = min(min_s, min_f)
		if sum(nums) == min_s:
			return max_s
		return max(max_s, sum(nums) - min_s)

# 17.找到最大开销的子字符串
class Solution:
	def maximumCostSubstring(self, s, chars, vals):
		ord_a = ord('a')
		n = len(s)
		chars_dic = defaultdict(int)
		for i, x in enumerate(chars):
			chars_dic[x] = vals[i]
		@cache
		def dfs(i):
			if i < 0:
				return 0
			if s[i] in chars_dic:
				val = chars_dic[s[i]]
			else:
				val = ord(s[i]) - ord_a + 1
			return max(val, dfs(i - 1) + val)  # 以s[i]结尾的字符串的最大开销
		return max(dfs(i) for i in range(-1, n))

# 18.任意子数组和的绝对值的最大值
class Solution: 
	def maxAbsoluteSum(self, nums):
		n = len(nums)
		@cache
		def dfs_mx(i):
			 if i < 0:
			 	return 0
			 return max(nums[i], dfs_mx(i - 1) + nums[i])
		@cache
		def dfs_mn(i):
			if i < 0:
				return 0
			return min(nums[i], dfs_mn(i - 1) + nums[i])
		mx = max(dfs_mx(i) for i in range(n))
		mn = min(dfs_mn(i) for i in range(n))
		return max(0, mx, -mn)
class Solution:
	def maxAbsoluteSum(self, nums):
		pre_s = list(accumulate(nums, initial = 0))
		return max(s) - min(s)
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        ans = f_max = f_min = 0
        for x in nums:
            f_max = max(f_max, 0) + x
            f_min = min(f_min, 0) + x
            ans = max(ans, f_max, -f_min)
        return ans

# 19.20250805水果成篮2
class Solution:
	def numOfUnplacedFruits(self, fruits, baskets):
		n = len(fruits)
		ans = 0
		for x in fruits:
			for i, y in enumerate(baskets):
				if x <= y:
					baskets[i] = 0
					break
			ans += 1 if x <= y else 0
		return ans

# 20.k次串联后最大子数组之和
class Solution:
	def kConcatenationMaxSum(self, arr, k):
		mod = 10 ** 9 + 7
		if all(x > 0 for x in arr):
			return sum(arr) * k % mod
		elif all(x < 0 for x in arr):
			return 0
		s = sum(arr)

		def maxSub(arr):
			n = len(arr)
			@cache
			def dfs(i):
				if i < 0:
					return 0
				return max(dfs(i - 1), 0) + arr[i]
			return max(dfs(i) for i in range(n))
		if k == 1:
			return max(0, maxSub(arr)) % mod
		else:
			return max(maxSub(arr + arr) + max(0, (k - 2) * s), 0) % mod

# 21.拼接数组的最大分数
class Solution:
	def maximumsSplicedArray(self, nums1, nums2):
		def mx_trans(arr1, arr2):
			n = len(arr1)
			diff = []
			for x, y in zip(arr1, arr2):
				diff.append(y - x)
			@cache
			def dfs(i):
				if i < 0:
					return 0
				return max(dfs(i - 1), 0) + diff[i]
			return max(dfs(i) for i in range(n)) + sum(arr1)
		return max(mx_trans(nums1, nums2), mx_trans(nums2, nums1))
## 递推写法
class Solution:
	def maximumsSplicedArray(self, nums1, nums2):
		def mx_trans(arr1, arr2):
			ans = f = 0  # 初始最大子数组和为0的原因是可以不交换
			for x, y in zip(arr1, arr2):
				f = max(f, 0) + y - x
				ans = max(ans, f)
			return sum(arr1) + ans
		return max(mx_trans(nums1, nums2), mx_trans(nums2, nums1))

# 22.删除一次得到子数组最大和
class Solution:  # 超时
	def maximumSum(self, nums):
		def mxSub(arr):
			# n = len(arr)
			# @cache
			# def dfs(i):
			# 	if i < 0:
			# 		return 0
			# 	return max(dfs(i - 1), 0) + arr[i]
			# return max(dfs(i) for i in range(n))
			ans = -inf
			f = 0
			for x in nums:
				f = max(f, 0) + x
				ans = max(ans, f)
			return ans
		if all(x >= 0 for x in nums) or len(nums) == 1:
			return sum(nums)
		else:
			ans = -inf
			for j, x in enumerate(nums):
				if x < 0:
					ans = max(ans, mxSub(nums[:j] + nums[j + 1:]))
		return ans
## 灵神题解
class Solution:  
	def maximumSum(self, nums):
		@cache
		def dfs(i, j):
			if i < 0:
				return -inf
			if j == 0:
				return max(dfs(i - 1, 0), 0) + arr[i]
			return max(dfs(i - 1, 1) + arr[i], dfs(i - 1, 0))
		return max(max(dfs(i, 0), dfs(i, 1)) for i in range(len(arr)))

################## 网格图DP #################
# 23.最小路径和
class Solution:
	def minPathSum(self, grid):
		n, m = len(grid), len(grid[0])
		@cache
		def dfs(i, j):
			if i < 0 or j < 0:
				return inf
			elif i == 0 and j == 0:
				return grid[0][0]
			return min(dfs(i - 1, j), dfs(i, j - 1)) + grid[i][j]
		return dfs(n - 1, m - 1)

# 24.不同路径
class Solution:
	def uniquePaths(self, m, n):
		@cache
		def dfs(i, j):
			if i < 0 or j < 0:
				return 0
			elif i == j == 0:
				return 1
			return dfs(i - 1, j) + dfs(i, j - 1)
		return dfs(m - 1, n - 1)

# 25.不同路径2
class Solution:
	def uniquePathsWithObstacles(self, obstacleGrid):
		n, m = len(obstacleGrid), len(obstacleGrid[0])
		@cache
		def dfs(i, j):
			if i < 0 or j < 0 or obstacleGrid[i][j]:
				return 0
			elif i == 0 and j == 0:
				return 1
			return dfs(i - 1, j) + dfs(i, j - 1)
		return dfs(n - 1, m - 1)

# 26.三角形最小路径和
class Solution:
	def minimumTotal(self, triangle):
		n = len(triangle)
		@cache
		def dfs(i, j):
			if j > i:
				return inf  # 这个情况不可能发生,可以省略
			elif i == n - 1:
				return triangle[i][j]
			return min(dfs(i + 1, j), dfs(i + 1, j + 1)) + triangle[i][j]
		return dfs(0, 0)

# 27.统计异或值为给定值的路径数目
class Solution:
	def countPathsWithXorValue(self, grid, k):
		n, m = len(grid), len(grid[0])
		mod = 10 ** 9 + 7
		@cache
		def dfs(i, j, path):
			if i < 0 or j < 0:
				return 0
			elif i == j == 0:
				return int(path ^ grid[0][0] == k)
			path ^= grid[i][j]
			return (dfs(i - 1, j, path) + dfs(i, j - 1, path)) % mod
		return dfs(n - 1, m - 1, 0)

# 28.下降路径最小和
class Solution:
	def minFallingPathSum(self, matrix):
		n = len(matrix)
		@cache
		def dfs(i, j):
			if j < 0 or j >= n:
				return inf
			elif i == n - 1:
				return matrix[i][j]
			return min(dfs(i + 1, j - 1), dfs(i + 1, j), dfs(i + 1, j + 1)) + matrix[i][j]
		return min(dfs(0, x) for x in range(0, n))

# 29.交替方向的最小路径代价2
class Solution:
	def minCost(self, m, n, waitCost):
		@cache
		def dfs(i, j):
			if i >= m or j >= n:
				return inf
			elif i == m - 1 and j == n - 1:
				return n * m
			if x % 2:
				return min(dfs(i + 1, j), dfs(i, j + 1)) + (i + 1) * (j + 1)
			else:
				return dfs(i, j, x + 1) + waitCost[i][j]
		return dfs(0, 0, 1)
## 灵神题解——过程状态推导出，每个过程为waitCost[i][j] + (i + 1)*(j + 1),而第一个和最后一个状态特殊考虑
class Solution:
	def minCost(self, m, n, waitCost):
		@cache
		def dfs(i, j):
			if i >= m or j >= n:
				return inf
			if i == m - 1 and j == n - 1:
				return n * m  # 最后的进入成本
			return min(dfs(i + 1, j), dfs(i, j + 1)) + waitCost[i][j] + (i + 1)*(j + 1)
		return dfs(0, 0) - waitCost[0][0]
class Solution:
    def minCost(self, m, n, waitCost):
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return inf
            if i == 0 and j == 0:
                return 1  # 起点只有进入成本，不需要等待
            return min(dfs(i, j - 1), dfs(i - 1, j)) + waitCost[i][j] + (i + 1) * (j + 1)
        return dfs(m - 1, n - 1) - waitCost[-1][-1]  # 终点不需要等待

# 30.最多可收集的水果数目
## 灵神题解
class Solution:
	def maxCollectedFruits(self, fruits):
		n = len(fruits)
		@cache
		def dfs(i, j):
			if not (n - 1 - i <= j < n):
				return -inf
			if i == 0:
				return fruits[i][j]
			return max(dfs(i - 1, j - 1), dfs(i - 1, j), dfs(i - 1, j + 1)) + fruits[i][j]

		ans = sum(row[i] for i, row in enumerate(fruits))  # 只能走对角线

		ans += dfs(n - 2, n - 1)
		dfs.cache_clear()

		fruits = list(zip(*fruits))
		return ans + dfs(n - 2, n - 1)

# 31.矩阵中移动的最大次数
class Solution:
	def maxMoves(self, grid):
		n, m = len(grid), len(grid[0])
		@cache
		def dfs(i, j, x):
			if i < 0 or i >= n or j == m or grid[i][j] <= x:
				return -1
			x = grid[i][j]
			return max(dfs(i - 1, j + 1, x), dfs(i, j + 1, x), dfs(i + 1, j + 1, x)) + 1
		return max(dfs(i, 0, 0) for i in range(n))
## 灵神题解
class Solution:
	def maxMoves(self, grid):
		m, n = len(grid), len(grid[0])
		ans = 0
		def dfs(i, j):
			nonlocal ans
			ans = max(ans, j)
			if ans == n - 1:
				return 
			for k in i - 1, i, i + 1:
				if 0 <= k < m and grid[k][j + 1] > grid[i][j]:
					dfs(k, j + 1)
			grid[i][j] = 0
		for i in range(m):
			dfs(i, 0)
		return ans

##################### 背包 ##################
# 32.分割等和子集
class Solution:
	def canPartition(self, nums):
		s = sum(nums)
		if s % 2:
			return False
		n = len(nums)
		@cache
		def dfs(i, temp_s):
			if i < 0 or temp_s > s // 2:
				return temp_s == s // 2
			return dfs(i - 1, temp_s + nums[i]) or dfs(i - 1, temp_s)
		return dfs(n - 1, 0)

# 33.目标和
class Solution:
	def findTargetSumWays(self, nums, target):
		n = len(target)
		new_target = (sum(nums) + target) // 2
		if (sum(nums) + target) % 2:
			return 0
		@cache
		dfs(i, path):
			if i < 0:
				return int(path == new_target)
			return dfs(i - 1, path) + dfs(i - 1, path + nums[i])
		return dfs(n - 1, 0)

# 34.和为目标值的最长子序列的长度
class Solution:
	def lengthOfLongestSubsequence(self, nums, target):
		ans = -1
		path_s = 0
		def dfs(i, path_len):
			nonlocal ans, path_s
			if i < 0:
				if path_s == target:
					ans = max(ans, path_len)
				return
			# 选
			path_s += nums[i]
			dfs(i - 1, path_len + 1)
			path_s -= nums[i]

			## 不选
			dfs(i - 1, path_len)
		dfs(len(nums) - 1, 0)
		return ans
class Solution:
	def lengthOfLongestSubsequence(self, nums, target):
		n = len(nums)
		@cache
		def dfs(i, path_s):
			if path_s == target:
				return 0
			if i < 0 or path_s > target:
				return -inf
			return max(dfs(i - 1, path_s + nums[i]) + 1, dfs(i - 1, path_s))
		ans = dfs(n - 1, 0)
		dfs.cache_clear()
		return ans if ans != -inf else -1
## 灵神题解
class Solution:
	def lengthOfLongestSubsequence(self, nums, target):
		@cache
		def dfs(i, j):
			if i < 0:
				return 0 if j == 0 else -inf
			if nums[i] > j:
				return dfs(i - 1, j)  # 只能不选
			return max(dfs(i - 1, j), dfs(i - 1, j - nums[i]) + 1)
		ans = dfs(len(nums) - 1, target)
		dfs.cache_clear()
		return ans if ans > 0 else -1

# 35.20250808分汤
class Solution:
	def soupServings(self, n):
		if n >= 4451:
			return 1
		@cache
		def dfs(i, j):
			if i <= 0 and j > 0:
				return 1
			elif i <= 0 and j <= 0:
				return 0.5
			elif j <= 0:
				return 0
			return 0.25 * (dfs(i - 100, j) + dfs(i - 75, j - 25) + dfs(i - 50, j - 50) + dfs(i - 25, j - 75))
		return dfs(n, n)

# 36.202508092的幂
class Solution:
	def isPowerOfTwo(self, n):
		if n <= 0:
			return False
		for i in range(0, n):
			if 2 ** i == n:
				return True
			elif 2 ** i < n:
				continue
			else:
				return False
## 灵神思路——2的幂的二进制最高位是1其余是0，n&(n - 1) = 0
class Solution:
	def isPowerOfTwo(self, n):
		return n > 0 and n & (n - 1) == 0

# 36.20250810重新排序得到2的幂
class Solution:
	def reorderedPowerOf2(self, n):
		diff = n - 1
		diff = list(str(diff))
		n = list(str(n))
		diff = int(''.join(diff))
		n = int(''.join(n))
		return True if n & diff == 0 else False

##################### 完全背包 #######################
# 37.零钱兑换
class Solution:
	def coinChange(self, coins, amount):
		n = len(coins)
		@cache
		def dfs(i, path):
			if i < 0 or path > amount:
				return inf
			elif path == amount:
				return 0
			return min(dfs(i, path + coins[i]) + 1, dfs(i - 1, path))
		ans = dfs(n - 1, 0)
		return ans if ans < inf else -1

# 38.零钱兑换2
class Solution:
	def change(self, amount, coins):
		@cache
		def dfs(i, path):
			if i < 0 or path > amount:
				return 0
			elif path == amount:
				return 1
			return dfs(i, path + coins[i]) + dfs(i - 1, path)
		return dfs(len(coins) - 1, 0)

# 39.完全平方数
@cache
def dfs(i, path):
	if path < 0 or i <= 0:
		return inf
	elif path == 0:
		return 0
	return min(dfs(i, path - i ** 2) + 1, dfs(i - 1, path))
class Solution:
	def numSquares(self, n):
		target = isqrt(n) + 1
		return dfs(target, n)

# 40.硬币面值还原
## 灵神题解——反零钱兑换
class Solution:
	def findCoins(self, numWays):
		mx = max(numWays)
		n = len(numWays)
		f = [1] + [0] * n
		ans = []
		for i, ways in enumerate(numWays, 1):
			if ways == f[i]:
				continue
			if ways - 1 != f[i]:
				return []
			ans.append(i)
			for j in range(i, n + 1):
				f[j] += f[j - i]
		return ans

######################### 多重背包 ##########################
# 41.获得分数的方法数
class Solution:  # 错解 无法控制types数组的变化
	def waysToReachTarget(self, target, types):
		MOD = 10 ** 9 + 7
		@cache
		def dfs(i, path):
			if i < 0:
				return 0
			elif path == 0:
				return 1
			if path < types[i][1] or types[i] == 0:
				return dfs(i - 1, path)  # 不选
			return dfs(i, path - types[i][1]) + dfs(i - 1, path)
## 灵神题解
class Solution:  
	def waysToReachTarget(self, target, types):
		MOD = 10 ** 9 + 7
		@cache
		def dfs(i, c):
			if i < 0:
				return 1 if c == 0 else 0
			res = dfs(i - 1, c)  # 不选
			for _ in range(types[i][0]):  # 枚举选k次的情况，加法原理即为方案数
				c -= types[i][1]
				if c < 0:
					break
				res = (res + dfs(i - 1, c)) % MOD
			return res
		return dfs(len(types) - 1, target)

# 42.20250811二的幂数组中查询范围内的乘积
ori_2 = [2 ** i for i in range(31)]
MOD = 10 ** 9 + 7
class Solution:
	def productQueries(self, n, queries):
		power = []
		for x in ori_2[::-1]:
			if sum(power) + x < n:
				power.append(x)

		power.sort()
		plus_pre = [1]
		for x in power:
			plus_pre.append(plus_pre[-1] * x)
		ans = []
		for left, right in queries:
			ans.append(plus_pre[right]//plus_pre[left]%MOD)
		return ans

# 43.掷骰子等于目标和的方法数
class Solution:
	def numRollsToTarget(self, n, k, target):
		MOD = 10 ** 9 + 7
		@cache
		def dfs(i, path):
			# if i > 0 and path <= 0:
			# 	return 0
			if i == 0:
				return int(path == 0)
			res = 0
			for x in range(1, k + 1):
				if path < x:
					break
				res = (res + dfs(i - 1, path - k)) % MOD
			return res
		return dfs(n, target)

# 44.最长公共子序列
class Solution:
	def longestCommonSubsequence(self, text1, text2):
		@cache
		def dfs(i, j):
			if i < 0 or j < 0:
				return 0
			if text1[i] == text2[j]:
				return dfs(i - 1, j - 1) + 1
			return max(dfs(i - 1, j), dfs(i, j - 1))
		return dfs(len(text1) - 1, len(text2) - 1)

# 45.两个字符串的删除操作
class Solution:
	def minDistance(self, word1, word2):
		n, m = len(word1), len(word2)
		@cache
		def dfs(i, j):
			# if i < 0 and j < 0:
			# 	return 0
			# elif i < 0 and j >= 0:
			# 	return j + 1
			# elif i >= 0 and j < 0:
			# 	return i + 1
			if i < 0 or j < 0:
				return i + j + 2
			if word1[i] == word2[j]:
				return dfs(i - 1, j - 1)
			return min(dfs(i - 1, j), dfs(i, j - 1)) + 1
		return dfs(n - 1, m - 1)




