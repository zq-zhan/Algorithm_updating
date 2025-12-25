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
				res = (res + dfs(i - 1, path - x)) % MOD
			return res
		return dfs(n, target)

####################### 经典线性DP #####################
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

# 46.20250812将一个数字表示成幂的和的方案数
class Solution:
	def numberOfWays(self, n, x):
		MOD = 10 ** 9 + 7
		@cache
		def dfs(i, path):
			if i < 0 or path > n:
				return 0
			if path == n:
				return 1
			return (dfs(i - 1, path + i ** x) + dfs(i - 1, path)) % MOD
		return dfs(n, 0)

# 47.两个字符串的最小ASCII删除和
class Solution:
	def minimumDeleteSum(self, s1, s2):
		n, m = len(s1), len(s2)
		@cache
		def dfs(i, j):
			if i < 0 and j < 0:
				return 0
			elif i < 0:
				return sum(ord(s2[k]) for k in range(j + 1))
			elif j < 0:
				return sum(ord(s1[k]) for k in range(i + 1))
			if s1[i] == s2[j]:
				return dfs(i - 1, j - 1)
			return min(dfs(i - 1, j) + ord(s1[i]), dfs(i, j - 1) + ord(s2[j]))
		return dfs(n - 1, m - 1)

# 48.编辑距离
class Solution:
	def minDistance(self, word1, word2):
		n, m = len(word1), len(word2)
		@cache
		def dfs(i, j):
			if i < 0 or j < 0:
				return i + j + 2
			if word1[i] == word2[j]:
				return dfs(i - 1, j - 1)
			return min(dfs(i, j - 1) + 1, dfs(i - 1, j) + 1,dfs(i - 1, j - 1) + 1)
		return dfs(n - 1, m - 1)

# 49.不相交的线
class Solution:
	def maxUncrossedLines(self, nums1, nums2):
		n, m = len(nums1), len(nums2)
		@cache
		def dfs(i, j):
			if i < 0 or j < 0:
				return 0
			if nums1[i] == nums2[j]:
				return dfs(i - 1, j - 1) + 1
			return max(dfs(i - 1, j), dfs(i, j - 1))
		return dfs(n - 1, m - 1)

# 50.两个子序列的最大点积
class Solution:
	def maxDotProduct(self, nums1, nums2):
		if all(x < 0 for x in nums1) and all(x > 0 for x in nums2):
			return max(nums1) * min(nums2)
		elif all(x > 0 for x in nums1) and all(x < 0 for x in nums2):
			return min(nums1) * max(nums2)

		n, m = len(nums1), len(nums2)
		@cache
		def dfs(i, j):
			if i < 0 or j < 0:
				return 0
			return max(dfs(i - 1, j), dfs(i, j - 1), dfs(i - 1, j - 1) + nums1[i] * nums2[j])
		return dfs(n - 1, m - 1)
class Solution:
	def maxDotProduct(self, nums1, nums2):
		n, m = len(nums1), len(nums2)
		@cache
		def dfs(i, j, flag):
			if i < 0 or j < 0:
				return 0 if flag else -inf
			return max(
				dfs(i - 1, j, flag),
				dfs(i, j - 1, flag),
				dfs(i - 1, j - 1, True) + nums1[i] * nums2[j]
				)
		return dfs(n - 1, m - 1, False)

# 51.202508133的幂
class Solution:
	def isPowerOfThree(self, n):
		if n <= 0:
			return False
		target = int(math.log(n, 3)) + 1
		for i in range(target + 1):
			if 3 ** i == n:
				return True
		return False
## 灵神题解——3的幂质因子只有3
class Solution:
	def isPowerOfThree(self, n):
		return n > 0 and 3 ** 19 % n == 0

# 52.最高乘法得分
class Solution:
	def maxScore(self, a, b):
		n = len(b)
		@cache
		def dfs(i, j):
			if i < 0:
				return 0
			elif j < 0:
				return -inf
			return max(
				dfs(i, j - 1),
				dfs(i - 1, j - 1) + a[i] * b[j]
				)
		return dfs(3, n - 1)

# 53.不同子序列
class Solution:
	def numDistinct(self, s, t):
		n, m = len(s), len(t)
		@cache
		def dfs(i, j):
			if j < 0:
				return 1
			elif i < 0:
				return 0
			res = 0
			if s[i] == t[j]:
				res += dfs(i - 1, j - 1)
			res += dfs(i - 1, j)
			return res
		return dfs(n - 1, m - 1)

# 54.插入一个字母的最大子序列数
class Solution:  # 错解！！！
	def numOfSubsequences(self, s):
		t = "LCT"
		@cache
		def dfs(i, j, tag):
			if j < 0:
				return 1
			if i < 0:
				return 0
			res = 0
			if s[i] == t[j]:
				res += dfs(i - 1, j - 1, tag)
			if tag:
				res = max(res, dfs(i, j - 1, False))
			res = max(res, dfs(i - 1, j, tag))
			return res  
		return dfs(len(s) - 1, 2, True)

# 55.最长递增子序列
class Solution:  # 用LCS求LIS
	def lengthOfLIS(self, nums):
		new_nums = sorted(set(nums))
		n, m = len(nums), len(new_nums)
		@cache
		def dfs(i, j):
			if i < 0 or j < 0:
				return 0
			if nums[i] == new_nums[j]:
				return dfs(i - 1, j - 1) + 1
			return max(dfs(i - 1, j), dfs(i, j - 1))
		return dfs(n - 1, m - 1)
## 灵神思路——枚举选哪个
class Solution:  
	def lengthOfLIS(self, nums):
		n = len(nums)
		@cache
		def dfs(i):
			res = 0
			for j in range(i):
				if nums[j] < nums[i]:
					res = max(res, dfs(j))
			return res + 1
		return max(dfs(i) for i in range(n))


# 56.20250814判断一个数字是否可以表示成三的幂的和
class Solution:  # 超过内存限制
	def checkPowersOfThree(self, n):
		@cache
		def dfs(i, path):
			if path < 0 or i > n:
				return False
			elif path == 0:
				return True
			return dfs(i + 1, path - 3 ** i) or dfs(i + 1, path)
		return dfs(0, n)
## 灵神题解——遍历n的三进制的每一位如果有2就返回false
class Solution:  
	def checkPowersOfThree(self, n):
		while n:
			if n % 3 == 2:
				return False
			n //= 3
		return True

# 57.字母异位词分组
class Solution:
	def groupAnagrams(self, strs):
		ans_dic = defaultdict(list)
		for substr in strs:
			res = ''.join(sorted(substr))
			ans_dic[res].append(substr)
		return list(ans_dic.values())

# 58.最长连续序列
class Solution:
	def longestConsecutive(self, nums):
		nums = list(set(nums))
		heapq.heapify(nums)
		ans = temp_length = 0
		pre = 'a'
		while nums:
			if pre == 'a' or nums[0] - pre == 1:
				temp_length += 1
			else:
				temp_length = 1
			pre = heapq.heappop(nums)
			ans = max(ans, temp_length)
		return ans
## 灵神题解
class Solution:
	def longestConsecutive(self, nums):
		st = set(nums)
		ans = 0
		for x in st:
			if x - 1 in st:
				continue
			y = x + 1
			while y in st:
				y += 1
			ans = max(ans, y - x)
		return ans

# 59.202508154的幂
class Solution:
	def isPowerOfFour(self, n):
		if n <= 0:
			return False
		for i in range(n):
			if 4 ** i == n:
				return True
			elif 4 ** i > n:
				return False

# 60.202508166和9组成的最大数字
class Solution:
	def maximum69Number(self, num):
		num = list(str(num))
		for i, x in enumerate(num):
			if x == '9':
				continue
			else:
				nums[i] = '9'
				break
		return int(''.join(num))

# 61.20250817新21点
class Solution:
	def new21Game(self, n, k, maxPts):
		res = []
		@cache
		def dfs(path_s, prob):
			if path_s >= k:
				res.append((path_s, prob))
				return 
			for x in range(1, maxPts + 1):
				dfs(path_s + x, prob * (1 / maxPts))
		dfs(0, 1.0)
		ans = 0
		for score, prob in res:
			if score <= n:
				ans += prob
		return ans
class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        dp=[None]*(K+W)
        s=0
        for i in range(K,K+W):          # 填蓝色的格子
            dp[i] = 1 if i<=N else 0
            s+=dp[i]
        for i in range(K-1,-1,-1):      # 填橘黄色格子
            dp[i]=s/W
            s += dp[i]-dp[i+W]
        return dp[0]

# 62.找到字符串中所有字母异位词
class Solution:
	def findAnagrams(self, s, p):
		dic_p = Counter(p)
		temp_win = dic_p.copy()
		ans = []
		left = 0
		for right, x in enumerate(s):
			if x not in dic_p:
				temp_win = dic_p.copy()
				left = right + 1
				continue
			elif not temp_win[x]:
				temp_win = dic_p.copy()
				left = right
			temp_win[x] -= 1
			if max(temp_win.values()) == 0:
				ans.append(left)
				temp_win[s[left]] += 1
				left += 1
		return ans
class Solution:
	def findAnagrams(self, s, p):
		dic_p = Counter(p)
		ans = []
		k = len(p)
		# n = len(s)
		temp_win = defaultdict(int)
		for i, x in enumerate(s):
			temp_win[x] += 1
			if sum(temp_win.values()) == k:
				if temp_win == dic_p:
					ans.append(i - k + 1)
				if temp_win[s[i - k + 1]] == 1:
					del temp_win[s[i - k + 1]]
				else:
					temp_win[s[i - k + 1]] -= 1
		return ans

# 63.滑动窗口最大值
class Solution:  # 超时
	def maxSlidingWindow(self, nums, k):
		ans = []
		n = len(nums)
		temp_win = defaultdict(int)
		left = 0
		for right, x in enumerate(nums):
			temp_win[x] += 1
			if right - left + 1 == k:
				ans.append(max(temp_win.keys()))
				if temp_win[nums[left]] == 1:
					del temp_win[nums[left]]
				else:
					temp_win[nums[left]] -= 1
				left += 1
		return ans
## 灵神题解——队列
class Solution:
    def maxSlidingWindow(self, nums, k):
        ans = [0] * (len(nums) - k + 1)  # 窗口个数
        q = deque()  # 双端队列

        for i, x in enumerate(nums):
            # 1. 右边入
            while q and nums[q[-1]] <= x:
                q.pop()  # 维护 q 的单调性
            q.append(i)

            # 2. 左边出
            left = i - k + 1  # 窗口左端点
            if q[0] < left:  # 队首已经离开窗口了
                q.popleft()

            # 3. 在窗口左端点处记录答案
            if left >= 0:
                # 由于队首到队尾单调递减，所以窗口最大值就在队首
                ans[left] = nums[q[0]]

        return ans

# 64.轮转数组
## 灵神题解
class Solution:
	def rotate(self, nums, k):
		def reverse(i, j):
			while i < j:
				nums[i], nums[j] = nums[j], nums[i]
				i += 1
				j -= 1

		n = len(nums)
		k %= n
		reverse(0, n - 1)
		reverse(0, k - 1)
		reverse(k, n - 1)
class Solution:
	def rotate(self, nums, k):
		n = len(nums)
		k = k % n
		nums[:] = nums[-k:] + nums[:-k]

# 65.2025081824点游戏
EPS = 1e-9
class Solution:
	def judgePoint24(self, cards):
		n = len(cards)
		if n == 1:
			return abs(cards[0] - 24) < EPS

		for i, x in enumerate(cards):
			for j in range(i + 1, n):
				y = cards[j]
				candidates = [x + y, x - y, y - x, x * y]
				if abs(y) > EPS:  # 分母不为0
					candidates.append(x / y)
				if abs(x) > EPS:
					candidates.append(y / x)

				new_cards = cards[:j] + cards[j + 1:]
				for res in candidates:
					new_arr[i] = res
					if self.judgePoint24(new_cards):
						return True
		return False

# 66.除自身以外数组的乘积
class Solution:
	def productExceptSelf(self, nums):
		n = len(nums)
		new_arr1 = [1]
		for x in nums:
			new_arr1.append(new_arr1[-1] * x)
		new_arr2 = [1] * (n + 1)
		for i in range(n - 1, -1, -1):
			new_arr2[i] = new_arr2[i + 1] * nums[i]

		ans = [0] * n
		for i in range(n):
			ans[i] = new_arr1[i] * new_arr2[i + 1]
		return ans

# 67.将三个组排序
class Solution:  # 转换为求最长递增子序列的长度
	def minimumOperations(self, nums):
		n = len(nums)
		@cache
		def dfs(i):
			res = 0
			for j in range(i):
				if nums[j] <= nums[i]:
					res = max(res, dfs(j))
			return res + 1
		return n - max(dfs(i) for i in range(n))

# 68.得到山形数组的最少删除次数
class Solution:
	def minimumMountainRemovals(self, nums):
		n = len(nums)
		@cache
		def dfs_add(i):
			res = 0
			for j in range(i):
				if nums[j] < nums[i]:
					res = max(res, dfs_add(j))
			return res + 1
		@cache
		def dfs_diff(i):
			res = 0
			for j in range(i + 1, n):
				if nums[j] < nums[i]:
					res = max(res, dfs_diff(j))
			return res + 1
		ans = 3
		for i in range(n):
			left = dfs_add(i)
			right = dfs_diff(i)
			if left >= 2 and right >= 2:
				ans = max(ans, left + right - 1)
		return n - ans

# 69.接雨水
## 灵神题解——前后缀分解
class Solution:
	def trap(self, height):
		n = len(height)
		pre_max = [0] * n  # pre_max[i]表示从height[0]到height[i]的最大值
		pre_max[0] = height[0]
		for i in range(1, n):
			pre_max[i] = max(pre_max[i - 1], height[i])

		suf_max = [0] * n
		suf_max[-1] = height[-1]
		for i in range(n - 2, -1, -1):
			suf_max[i] = max(suf_max[i + 1], height[i])

		ans = 0
		for h, pre, suf in zip(height, pre_max, suf_max):
			ans += min(pre, suf) - h
		return ans
		
# 70.20250819全0子数组的数目
class Solution:
	def zeroFilledSubarray(self, nums):
		nums = nums + [1]
		ans = left = 0
		for right, x in enumerate(nums):
			if x == 0:
				continue
			ans += (right - left) * (right - left + 1) // 2
			left = right + 1
		return ans
## 灵神思路扩展——增量法
class Solution:
	def zeroFilledSubarray(self, nums):
		ans = cnt0 = 0
		for x in nums:
			if x:
				cnt0 = 0
			else:
				cnt0 += 1
				ans += cnt0
		return ans

# 71.找出到每个位置为止最长的有效障碍赛跑路线
class Solution:  # 超时
	def longestObstacleCourseAtEachPosition(self, obstacles):
		ans = []
		n = len(obstacles)
		@cache
		def dfs(i):
			res = 0
			for j in range(i):
				if obstacles[j] <= obstacles[i]:
					res = max(res, dfs(j))
			return res + 1
		for i in range(n):
			ans.append(dfs(i))
		return ans

# 72.使数组k递增的最少操作次数
def find_mx(nums):
	g = []
	for x in nums:
		j = bisect_right(g, x)
		if j == len(g):
			g.append(x)
		else:
			g[j] = x
	return len(g) 

class Solution:
	def kIncreasing(self, arr, k):
		n = len(arr)
		ans = 0
		# @cache
		# def dfs(i, nums):
		# 	res = 0
		# 	for j in range(i):
		# 		if nums[j] <= nums[i]:
		# 			res = max(res, dfs(j))
		# 	return res + 1
				
		for i in range(k):
			new_arr = [arr[j] for j in range(i, n, k)]
			m = len(new_arr)
			# temp_mx = max(dfs(i, new_arr) for i in range(m))
			temp_mx = find_mx(new_arr)
			ans += m - temp_mx
		return ans
## 写法二
class Solution:
	def kIncreasing(self, arr, k):
		def f(x):
			g = []
			for i in range(x, n, k):
				j = bisect_right(g, arr[i])
				if j == len(g):
					g.append(arr[i])
				else:
					g[j] = arr[i]
			return len(g)
		n = len(arr)
		return n - sum(f(x) for x in range(k))
## 记忆化搜索解法
class Solution:
	def kIncreasing(self, arr, k):
		n = len(arr)
		@cache
		def dfs(i):
			res = 0
			for j in range(i - k, -1, -k):
				if arr[j] <= arr[i]:
					res = max(res, dfs(j))
			return res + 1
		# return n - sum(dfs(i) for i in range(n))  这里有问题，还是要拆
        if k == 1:
            return n - max(dfs(i) for i in range(n))
        else:
            total = 0
            # 分成k个独立的子序列，分别计算每个子序列的LNDS
            for start in range(k):
                max_len = 0
                for i in range(start, n, k):
                    max_len = max(max_len, dfs(i))
                total += max_len
            return n - total

# 73.20250820统计全为1的正方形子矩阵
class Solution:
    def countSquares(self, matrix):
        ans = 0
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:  # 只有以 1 开头的才可能形成正方形
                    cnt = 0
                    while i + cnt < m and j + cnt < n:
                        # 计算子矩阵 (i,j) 到 (i+cnt, j+cnt) 的和
                        total = 0
                        for r in range(i, i + cnt + 1):
                            total += sum(matrix[r][j:j + cnt + 1])
                        # 判断是否全是 1
                        if total == (cnt + 1) * (cnt + 1):
                            ans += 1
                            cnt += 1
                        else:
                            break
        return ans
## 灵神题解——动态规划
class Solution:
	def countSquares(self, matrix):
		m, n = len(matrix), len(matrix[0])
		f = [[0] * (n + 1) for _ in range(m + 1)]
		for i, row in enumerate(matrix):
			for j, x in enumerate(row):
				if x:
					f[i + 1][j + 1] = min(f[i][j], f[i][j + 1], f[i + 1][j]) + 1
		return sum(map(sum, f))

# 74.检查数组是否存在有效划分
## 灵神题解——递推写法
class Solution:
	def validPartition(self, nums):
		n = len(nums)
		f = [True] + [False] * n
		for i, x in enumerate(nums):
			if i > 0 and f[i - 1] and x == nums[i - 1] or \
				i > 1 and f[i - 2] and (x == nums[i - 1] == nums[i - 2] or \
										x == nums[i - 1] + 1 == nums[i - 2] + 2):
				f[i + 1] = True
		return f[n]
## 递归		
class Solution:
	def validPartition(self, nums):
		@cache
		def dfs(i):
			if i < 0:
				return True
			elif i == 0:
				return False
			res = False
			if nums[i] == nums[i - 1]:
				res |= dfs(i - 2)
			if i > 1 and (nums[i] == nums[i - 1] == nums[i - 2] or nums[i] == nums[i - 1] + 1 == nums[i - 2] + 2):
				res |= dfs(i - 3)
			return res
		return dfs(len(nums) - 1)

# 75.单词拆分
class Solution:
	def wordBreak(self, s, wordDict):
		wordDict = set(wordDict)
		wordLen = list(map(len, wordDict))
		@cache
		def dfs(i):
			if i < 0:
				return True
			# elif i == 0:
			# 	return s[0] in wordDict
			elif i < min(wordLen) - 1:
				return False
			res = False
			for length in wordLen:
				if i - length + 1 >= 0 and s[i - length + 1:i + 1] in wordDict:
					res |= dfs(i - length)
				# res |= dfs(i - length) and s[i - length + 1:i + 1] in wordDict:
			return res
		return dfs(len(s) - 1)

# 76.20250821统计全1子矩形
## 灵神题解
class Solution:
    def numSubmat(self, mat):
        m, n = len(mat), len(mat[0])
        ans = 0
        for top in range(m):  # 枚举上边界
            a = [0] * n
            for bottom in range(top, m):  # 枚举下边界
                h = bottom - top + 1  # 高
                # 2348. 全 h 子数组的数目
                last = -1
                for j in range(n):
                    a[j] += mat[bottom][j]  # 把 bottom 这一行的值加到 a 中
                    if a[j] != h:
                        last = j  # 记录上一个非 h 元素的位置
                    else:
                        ans += j - last
        return ans

# 77.分割回文串2
## 灵神题解
class Solution:
	def minCut(self, s):
		@cache
		def is_palindrome(l, r):
			if l >= r:
				return True
			return s[l] == s[r] and is_palindrome(l + 1, r - 1)
		@cache
		def dfs(r):
			if is_palindrome(0, r):
				return 0
			res = inf
			for l in range(1, r + 1):  # 枚举分割位置
				if is_palindrome(l, r):
					res = min(res, dfs(l - 1) + 1)
			return res
		return dfs(len(s) - 1)
		
# 78.字符串中的额外字符
class Solution:
	def minExtraChar(self, s, dictionary):
		dictionary = set(dictionary)
		wordLen = set(map(len, dictionary))
		@cache
		def dfs(i):
			if i < min(wordLen) - 1:
				return max(0, i + 1)
			ans = dfs(i - 1) + 1  # 不选的时候ans最大
			for length in wordLen:
				if i >= length - 1 and s[i - length + 1:i + 1] in dictionary:
					ans = min(ans, dfs(i - length))
			return ans
		return dfs(len(s) - 1)
class Solution:
	def minExtraChar(self, s, dictionary):
		dictionary = set(dictionary)
		mn_len = min(list(map(len, dictionary)))
		@cache
		def dfs(i):
			if i < mn_len - 1:
				return max(0, i + 1)
			res = inf
			for j in range(i + 1):
				if s[j:i + 1] in dictionary:
					res = min(res, dfs(j - 1))
					break
			res = min(res, dfs(i - 1) + 1)
			return res
		return dfs(len(s) - 1)

# 79.20250822包含所有1的最小矩形面积1
class Solution:
	def minimumArea(self, grid):
		n, m = len(grid), len(grid[0])
		left = m - 1
		right = 0
		high = 0
		low = n - 1
		for i in range(n):
			for j in range(m):
				if grid[i][j]:
					left = min(left, j)
					right = max(right, j)
					# high = max(high, i)
					high = i
					low = min(low, i)
		return (right - left + 1) * (high - low + 1)

# 80.最大化子数组的总成本
class Solution:
	def maximumTotalCost(self, nums):
		@cache
		def cost(i, j):
			res = 0
			for k, x in enumerate(nums[i:j + 1]):
				res += x * (-1) ** k
			return res
		@cache
		def dfs(i):
			if i < 0:
				return 0
			res = -inf
			for j in range(i + 1):
				res = max(res, dfs(j - 1) + cost(j, i))
			return res
		return dfs(len(nums) - 1)
## 灵神题解——优化
class Solution:
	def maximumTotalCost(self, nums):
		@cache
		def dfs(i):
			if i < 0:
				return 0
			if i == 0:
				return nums[0]
			return max(dfs(i - 1) + nums[i], dfs(i - 2) + nums[i - 1] - nums[i])
		return dfs(len(nums) - 1)

# 81.20250823包含所有1的最小矩形面积2
class Solution:
	def minimumSum(self, grid):

# 82.将字符串分割为最少的美丽子字符串
class Solution:
	def minimumBeautifulSubstrings(self, s):
		# @cache
		# def check(x):
		# 	for i in range(x + 1):
		# 		if 5 ** i == x:
		# 			return True
		# 		elif 5 ** i > x:
		# 			break
		# 	return False
		target = {1, 5, 25, 125, 625, 3125, 15625}
		@cache
		def dfs(i):
			if i < 0:
				return 0
			res = inf
			for j in range(i + 1):
				x = int(s[j:i + 1], 2)
				if s[j] == '1' and x in target:
					res = min(res, dfs(j - 1) + 1)
			return res
		ans = dfs(len(s) - 1)
		return ans if ans < inf else -1

# 83.20250824删掉一个元素以后全为1的最长子数组
class Solution:
	def longestSubarray(self, nums):
		if sum(nums) == len(nums):
			return len(nums) - 1
		ans = cnt = left = 0
		for right, x in enumerate(nums):
			while x == 0 and cnt == 1:
				cnt -= int(nums[left] == 0)
				left += 1
			cnt += int(x == 0)
			ans = max(ans, right - left + 1 - cnt)
		return ans
## 不定长滑动窗口解法
class Solution:
	def longestSubarray(self, nums):
		cnt_win = 0
		ans = 0 
		left = 0
		for right, c in enumerate(nums):
			cnt_win += 1 if c == 0 else 0
			while cnt_win > 1:
				cnt_win -= 1 if nums[left] == 0 else 0
				left += 1
			ans = max(ans, right - left)
		return ans
class Solution:
	def longestSubarray(self, nums):
		cnt_win = 0
		ans = left = 0
		for right, c in enumerate(nums):
			cnt_win += (1 - c)
			while cnt_win > 1:
				cnt_win -= 1 - nums[left]
				left += 1
			ans = max(ans, right - left + 1 - cnt_win)
		return min(ans, len(nums) - 1)

# 84.解码方法
class Solution:  # 错解
	def numDecodings(self, s):
		if s.startswith('0'):
			return 0
		@cache
		def dfs(i):
			if i < 0:
				return 0
			res = 0
			for j in range(i + 1):
				if s[j] != '0' and int(s[j:i + 1]) < 27:
					res = max(res, dfs(j - 1) + 1)
			return res
		return dfs(len(s) - 1)
class Solution:  
	def numDecodings(self, s):
		@cache
		def dfs(i):
			if i < 0:
				return 1
			ans = 0
			num = int(s[i:i + 1])
			if 1 <= num <= 9:
				ans += dfs(i - 1)
			num = int(s[max(i - 1, 0):i + 1])
			if 10 <= num <= 26:
				ans += dfs(i - 2)
			return ans
		return dfs(len(s) - 1)

##################### 状态机DP #################
# 85.买卖股票的最佳时机
class Solution:
	def maxProfit(self, prices):
		n = len(prices)
		suf_mx = [0] * (n + 1)
		for i in range(n - 1, -1, -1):
			suf_mx[i] = max(prices[i], suf_mx[i + 1])
		pre_min = inf
		ans  = 0
		for i, x in enumerate(prices):
			ans = max(ans, suf_mx[i] - pre_min)
			pre_min = min(pre_min, x)
		return ans
## 简洁写法——枚举卖出价格，维护最小的买入价格即可
class Solution:
	def maxProfit(self, prices):
		ans = 0
		pre_buy = prices[0]
		for sold in prices:
			ans = max(ans, sold - pre_buy)
			pre_buy = min(pre_buy, sold)
		return ans

# 86.买卖股票的最佳时机2
class Solution:  # 超出内存限制
	def maxProfit(self, prices):
		n = len(prices)
		@cache
		def dfs(i, x):
			if i > n - 1:
				return 0
			if x != -1:
				return max(dfs(i, -1) + prices[i] - x, dfs(i + 1, x))
			return max(dfs(i + 1, prices[i]), dfs(i + 1, -1))
		return dfs(0, -1)
## 灵神题解
class Solution:
	def maxProfit(self, prices):
		n = len(prices)
		@cache
		def dfs(i, hold):
			if i < 0:
				return -inf if hold else 0
			if hold:
				return max(dfs(i - 1, True), dfs(i - 1, False) - prices[i])
			return max(dfs(i - 1, False), dfs(i - 1, True) + prices[i])
		return dfs(n - 1, False)

# 87.买卖股票的最佳时机含冷冻期
## 核心思想类似打家劫舍
class Solution:
	def maxProfit(self, prices):
		n = len(prices)
		@cache
		def dfs(i, hold):
			if i < 0:
				return -inf if hold else 0
			if hold:
				return max(dfs(i - 1, True), dfs(i - 2, False) - prices[i]) # 上一个未持有状态买入股票后这阶段变为持有
			return max(dfs(i - 1, False), dfs(i - 1, True) + prices[i]) # 上一个持有状态卖出股票后这阶段变为未持有
		return dfs(n - 1, False)		

# 88.买卖股票的最佳时机3
# 交易两次
class Solution:
	def maxProfit(self, prices):
		n = len(prices)
		@cache
		def dfs(i, j, hold):
			if j < 0:
				return -inf
			if i < 0:
				return -inf if hold else 0
			if hold:
				return max(dfs(i - 1, j, True), dfs(i - 1, j, False) - prices[i])
			return max(dfs(i - 1, j, False), dfs(i - 1, j - 1, True) + prices[i])
		return dfs(n - 1, 2, False)	

# 89.买卖股票的最佳时机5
# 普通交易+做空交易
## +p的时候也就是卖出的时候视为交易完成一次，可以用j - 1;-p也就是买入的时候视为交易完成一次可以用j - 1;二者选一种即可
class Solution:
	def maximumProfit(self, prices, k):
		n = len(prices)
		@cache
		def dfs(i, j, state):
			if j < 0:
				return -inf
			if i < 0:
				return -inf if state else 0
			p = prices[i]
			if state == 0:
				return max(dfs(i - 1, j, 0), dfs(i - 1, j, 1) + p, dfs(i - 1, j, 2) - p)
			elif state == 1:
				return max(dfs(i - 1, j, 1), dfs(i - 1, j - 1, 0) - p)
			return max(dfs(i - 1, j, 2), dfs(i - 1, j - 1, 0) + p)	
		ans = dfs(n - 1, k, 0)
		dfs.cache_clear()
		return ans

# 90.买卖股票的最佳时机含手续费
class Solution:
	def maxProfit(self, prices, fee):
		n = len(prices)
		@cache
		def dfs(i, state):
			if i < 0:
				return -inf if state else 0
			if state:
				return max(dfs(i - 1, state), dfs(i - 1, 0) - prices[i])
			return max(dfs(i - 1, state), dfs(i - 1, 1) + prices[i] - fee)
		return dfs(n - 1, 0)

# 91.20250825对角线遍历
## 灵神题解——枚举k,i + j = k,
class Solution:
	def findDiagonalOrder(self, mat):
		m, n = len(mat), len(mat[0])
		ans = []
		for k in range(m + n - 1):
			min_j = max(k - m + 1, 0)
			max_j = min(k, n - 1)
			if k % 2 == 0:  #偶数从小到大
				for j in range(min_j, max_j + 1):
					ans.append(mat[k - j][j])
			else:
				for j in range(max_j, min_j - 1, -1):
					ans.append(mat[k - j][j])
		return ans

# 92.N皇后
class Solution:
    def solveNQueens(self, n):
        ans = []
        queens = [0] * n  # 皇后放在 (r,queens[r])
        col = [False] * n
        diag1 = [False] * (n * 2 - 1)
        diag2 = [False] * (n * 2 - 1)
        def dfs(r: int) -> None:
            if r == n:
                ans.append(['.' * c + 'Q' + '.' * (n - 1 - c) for c in queens])
                return
            # 在 (r,c) 放皇后
            for c, ok in enumerate(col):
                if not ok and not diag1[r + c] and not diag2[r - c]:  # 判断能否放皇后
                    queens[r] = c  # 直接覆盖，无需恢复现场
                    col[c] = diag1[r + c] = diag2[r - c] = True  # 皇后占用了 c 列和两条斜线
                    dfs(r + 1)
                    col[c] = diag1[r + c] = diag2[r - c] = False  # 恢复现场
        dfs(0)
        return ans

# 93.超级饮料的最大强化能量
class Solution:
	def maxEnergyBoost(self, energyDrinkA, energyDrinkB):
		n = len(energyDrinkA)
		@cache
		def dfs(i, state):
			if i < 0:
				return 0
			if state == 0:
				return max(dfs(i - 1, 0), dfs(i - 2, 1)) + energyDrinkA[i]
			return max(dfs(i - 1, 1), dfs(i - 2, 0)) + energyDrinkB[i]
		return max(dfs(n - 1, 0), dfs(n - 1, 1))

# 94.选择建筑的方案数
class Solution:  # 超出内存，恰好为k的买卖股票
	def numberOfWays(self, s):
		n = len(s)
		@cache
		def dfs(i, j, x):
			if j < 0:
				return 0
			if i < 0:
				return int(j == 0)
			if s[i] == x:
				return dfs(i - 1, j, x)
			return dfs(i - 1, j, x) + dfs(i - 1, j - 1, s[i])
		return dfs(n - 1, 3, -1)
## 灵神题解——前后缀分解
class Solution:
	def numberOfWays(self, s):
		n = len(s)
		pre_0 = [0] * (n + 1)
		suf_0 = [0] * (n + 1)
		pre_1 = [0] * (n + 1)
		suf_1 = [0] * (n + 1)
		for i in range(n):
			pre_0[i + 1] = pre_0[i] + int(s[i] == '0')
			pre_1[i + 1] = pre_1[i] + int(s[i] == '1')
		for i in range(n - 1, -1, -1):
			suf_0[i] = suf_0[i + 1] + int(s[i] == '0')
			suf_1[i] = suf_1[i + 1] + int(s[i] == '1')
		ans = 0
		for i, x in enumerate(s):
			if x == '1':
				ans += pre_0[i] * suf_0[i + 1]
			else:
				ans += pre_1[i] * suf_1[i + 1]
		return ans
		# tot_0 = s.count('0')
		# ans = c0 = 0
		# for i, x in enumerate(s):
		# 	if x == '1':
		# 		ans += c0 * (total - c0)
		# 	else:
		# 		c1 = i - c0
		# 		ans += c1 * (len(s) - tot_0 - c1)
		# 		c0 += 1
		# return ans

# 95.20250826对角线最长的矩形的面积
class Solution:
	def areaOfMaxDiagonal(self, dimensions):
		ans = length = 0
		for x, y in dimensions:
			dig = x ** 2 + y ** 2
			if dig > length:
				length = dig
				ans = x * y
			elif dig == length:
				ans = max(ans, x * y)
		return ans
## 灵神思路——多关键词比较
class Solution:
	def areaOfMaxDiagonal(self, dimensions):
		return max((x * x + y * y, x * y) for x, y in dimensions)[1]

# 96.一个小组的最大实力值
## 回溯写法
class Solution:
	def maxStrength(self, nums):
		res = -inf
		path = []
		def dfs(i):
			nonlocal res
			if i < 0:
				if path:
					temp = 1
					for x in path:
						temp *= x
					res = max(res, temp)
				return
			# 选
			path.append(nums[i])
			dfs(i - 1)
			path.pop()

			# 不选
			dfs(i - 1)
		dfs(len(nums) - 1)
		return res
## 回溯写法二
class Solution:
	def maxStrength(self, nums):
		n = len(nums)
		ans = -inf
		def dfs(i, temp, k):
			nonlocal ans
			if i < 0:
				if k:
					ans = max(ans, temp)
				return
			## 选
			dfs(i - 1, temp * nums[i], k + 1)
			## 不选
			dfs(i - 1, temp, k)
		dfs(n - 1, 1, 0)
		return ans

# 97.乘积为正数的最长子数组长度
class Solution:  # 暴力解法，超时
	def getMaxLen(self, nums):
		ans = 0
		n = len(nums)
		for i in range(n):
			temp = 1
			for j in range(i, -1, -1):
				temp *= nums[j]
				if temp > 0:
					ans = max(ans, j - i + 1)
		return ans
## 贪心思路
class Solution:  
	def getMaxLen(self, nums):
		cntp = cntn = ans = st = 0
		firstn = lastn = -1
		for i, x in enumerate(nums):
			if x == 0:
				cntp = cntn = 0
				firstn = lastn = -1
				st = i + 1  # 起始下标
			elif x > 0:
				cntp += 1
			else:
				if firstn == -1:
					firstn = i
				lastn = i
				cntn += 1
			if cntn % 2 == 0:
				ans = max(ans, cntp + cntn)
			else:
				ans = max(ans, i - firstn, lastn - st)
		return ans

# 98.访问数组中的位置使分数最大
class Solution:
	def maxScore(self, nums, x):
		n = len(nums)
		@cache
		def dfs(i, t):
			if i == n:
				return 0
			if nums[i] % 2 == t:  # 相同必选，
				return dfs(i + 1, t) + nums[i]
			return max(dfs(i + 1, t), dfs(i + 1, t ^ 1) - x + nums[i])  # 不同的时候比较
		return dfs(0, nums[0] % 2)

# 99.最大交替子序列和
class Solution:
	def maxAlternatingSum(self, nums):
		@cache
		def dfs(i, t):
			if i < 0:
				return 0
			if t % 2 == 0:
				return max(dfs(i - 1, t ^ 1) - nums[i], dfs(i - 1, t))
			return max(dfs(i - 1, t ^ 1) + nums[i], dfs(i - 1, t))
		return dfs(len(nums) - 1, 1)

# 100.摆动序列
class Solution:
	def wiggleMaxLength(self, nums):
		if all(nums) == 0:
			return 1

		n = len(nums)
		@cache
		def dfs(i, pre1, pre2):
			if i == n:
				return 0
			if pre1 == -1 or pre2 == -1 or (pre1 - pre2) * (nums[i] - pre1) < 0:
				return max(dfs(i + 1, nums[i], pre1) + 1, dfs(i + 1, pre1, pre2))
			return dfs(i + 1, pre1, pre2)
		return dfs(0, -1, -1)
## 回溯解法
class Solution:
	def wiggleMaxLength(self, nums):
		n = len(nums)
		ans = 1
		def dfs(i, path):
			nonlocal ans
			ans = max(ans, len(path))
			if i == n:
				return
			
			## 不选
			if (len(path) > 1 and (path[-1] - path[-2]) * (nums[i] - path[-1]) >= 0) or (len(path) >= 1 and path[-1] == nums[i]):
				dfs(i + 1, path)	
			else:		
				## 选
				path.append(nums[i])
				dfs(i + 1, path)
				path.pop()  # 回溯
		dfs(0, [])
		return ans
## 贪心
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # special condition
        if len(nums) == 1: return 1      
        start_by_True, st_need_flag = 1, False
        start_by_False, sf_need_flag = 1, True
        for i in range(1, len(nums)):
            value = nums[i] - nums[i-1]
            cur_flag = True if value > 0 else False
            if value == 0:
                continue
            if cur_flag == st_need_flag:
                start_by_True += 1
                st_need_flag = not st_need_flag
            if cur_flag == sf_need_flag:
                start_by_False += 1
                sf_need_flag = not sf_need_flag
        return max(start_by_True, start_by_False)

        

# 101.20250828按对角线进行矩阵排序
class Solution:
	def sortMatrix(self, grid):
		m, n = len(grid), len(grid[0])
		for k in range(1, m + n):
			min_j = max(n - k, 0)
			max_j = min(m + n - 1 - k, n - 1)
			a = [grid[k + j - n][j] for j in range(min_j, max_j + 1)]
			a.sort(reverse = k >= n)
			for j, val in zip(range(min_j, max_j + 1), a):
				grid[k + j - n][j] = val
		return grid

# 102.20250829鲜花游戏
class Solution:
	def flowerGame(self, n, m):
		n_ou = n // 2
		m_ou = m // 2
		n_ji = n - n_ou
		m_ji = m - m_ou
		return n_ou * m_ji + n_ji * m_ou

# 103.20250830有效数独
class Solution:
	def isValidSudoku(self, board):
		for row in board:
			a = [x for x in row if x != '.']
			if len(a) != len(set(a)):
				return False
		for j in range(n):
			b = [row[j] for row in board if row[j] != '.']
			if len(b) != len(set(b)):
				return False
		target = [(1,1), (1,4), (1,7), (4,1), (4,4), (4,7), (7,1), (7,4), (7,7)]
		for x, y in target:
			a = set()
			for diff1 in (-1, 0, 1):
				for diff2 in (-1, 0, 1):
					num = board[x + diff1][y + diff2]
					if num != '.':
						if num not in a:
							a.add(num)
						else:
							return False
		return True

# 104.矩阵置零
class Solution:
	def setZeroes(self, matrix):
		m, n = len(matrix), len(matrix[0])
		row_zero = set()
		col_zero = set()
		for i in range(m):
			for j in range(n):
				if matrix[i][j] == 0:
					row_zero.add(i)
					col_zero.add(j)
		for i in range(m):
			for j in range(n):
				if i in row_zero or j in col_zero:
					matrix[i][j] = 0
				






