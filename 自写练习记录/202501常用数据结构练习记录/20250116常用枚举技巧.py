# 枚举右、维护左
# 1.两数之和
class Solution1:
	def twoSum(self, nums, target):
		left = 0
		while left < len(nums) - 1:
			right = left + 1
			while right < len(nums):
				if nums[right] == target - nums[left]:
					return [left, right]
				right += 1
			left += 1
## 灵神题解——哈希表解法
class Solution2:
	def twoSum(Self, nums, target):
		idx = {}
		for j, x in enumerate(nums):  # 枚举右
			if target - x in idx:
				return [idx[target - x], j]
			idx[x] = j # 维护左

# 2.好数对的数目
class Solution1:
	def numIdenticalPairs(self, nums):
		idx = defaultdict(list)
		ans = 0
		for j, x in enumerate(nums):
			if x in idx:
				ans += len(idx[x])
			idx[x].append(j)
		return ans
## 灵神题解
class Solution2:
	def numIdenticalPairs(self, nums):
		ans = 0
		cnt = defaultdict(int)
		for x in nums:
			ans += cnt[x]
			cnt[x] += 1
		return ans 

# 3.可互换矩形的组数
class Solution1:
	def interchangeableRectangles(self, rectangles):
		ans = 0
		idx = defaultdict(int)
		for j, rectangle in enumerate(rectangles):
			bili = rectangle[0] / rectangle[1]
			if bili in idx:
				ans += len(idx[bili])
			idx[bili] += 1
		return ans

# 4.存在重复元素2
class Solution1:
	def containsNearbyDuplicate(self, nums, k):
		idx = defaultdict(list)
		for j, x in enumerate(nums):
			if x in idx:
				if abs(c - idx[x][-1]) <= k:
					return True
				# for c in idx[x]:
				# 	if abs(c - j) <= k:
				# 		return True
			idx[x].append(j)
		return False
## 灵神题解
class Solution2:
	def containsNearbyDuplicate(self, nums, k):
		last = {}
		for j, x in enumerate(nums):
			if x in last and j - last[x] <= k:
				return True
			last[x] = i  # 记录每个数x上一次出现的位置的下标
		return False

###########################################################
# 枚举中间变量
# 1.元素和最小的山形三元组
class Solution1:
	def minimumSum(self, nums):
		n = len(nums)
		ans = inf
		for j in range(1, n - 1):
			mid = nums[j]
			i = j - 1
			k = j + 1

			while i >= 0 and k < n:
				if nums[i] >= mid:
					i -= 1
					continue
				if nums[k] >= mid:
					k += 1
					continue
				# left = nums[i]
				# right = nums[k]
				
				i -= 1
				k += 1
				if nums[i] < mid and nums[j] < mid:
					ans = min(ans, nums[i] + mid + nums[k])
				i -= 1
				k += 1

		return ans if ans < inf else -1
## 灵神题解
class Solution2:
	def minimumSum(self, nums):
		n = len(nums)
		suf = [0] * n
		suf[-1] = nums[-1]
		for i in range(n - 2, 1, -1):
			suf[i] = min(suf[i + 1], nums[i])

		ans = inf
		pre = nums[0]
		for j in range(1, n - 1):
			if pre < nums[j] > suf[j + 1]:
				ans = min(ans, pre + nums[i] + suf[j + 1])
			pre = min(pre, nums[j])
		return ans if ans < inf else -1

# 2.长度为3的不同回文子序列
class Solution1:
	def countPalindromicSubsequence(self, s):
		ans = 0
		n = len(s)
		left_lis = [s[0]]
		right_lis = [s[-1]]
		for m in range(1, n - 1):
			left_lis.append([left_lis[m-1] + [s[m]]])
		for n in range(n - 2, 1, -1):
			right_lis.append([right_lis[n+1] + [s[n]]])

		for j in range(1, n - 1):
## 
class Solution2:
	def countPalindromicSubsequence(self, s):
		n = len(s)
		suf = [0] * 26
		for i in range(n - 1, -1, -1):
			suf[ord(s[i]) - ord('a')] += 1
		ans = set()
		pre = [0] * 26
		for i in range(n):
			suf[ord(s[i]) - ord('a')] -= 1  # 维护后缀和
			for j, a, b in zip(range(26), pre, suf):
				if a*b != 0:
					ans.add(chr(j + 97) + s[i] + chr(j + 97))
			pre[ord(s[i]) - ord('a')] += 1  # 维护前缀和
		return len(ans)

# 3.直角三角形
class Solution1:
	def numberOfRightTriangles(self, grid):
		n = len(s)
		rowSum_lis = []
		colSum_lis = [0] * n
		for i in range(n):
			rowSum_lis.append(sum(grid[i]))
			colSum_lis += list(grid[i][j] for j in range(n))
## 灵神题解
class Solution1:
	def numberOfRightTriangles(self, grid):
		col_sum = [sum(col) - 1 for col in zip(*grid)]  # zip(*grid) 转置矩阵，zip(*grid)[i] 第i列
		ans = 0
		for row in grid:
			row_sum = sum(row) - 1
			if row_sum > 0:
				for col in col_sum:
					if col >= 0:
						ans += row_sum * col
				# ans += sum(row_sum * col for col in col_sum if clo >= 0)
		return ans

# 4.有序三元组中的最大值2
class Solution1:
	def maximumTripletValue(self, nums):
		ans = 0
		n = len(nums)
		suf = [nums[-1]] * n
		for p1 in range(n - 2, -1, -1):
			suf[p1] = max(nums[p1], suf[p1 + 1])
		pre = [nums[0]] * n
		for p2 in range(1, n):
			pre[p2] = max(nums[p2], pre[p2 - 1])

		for j in range(1, n - 1):
			ans = max(ans, (pre[j - 1] - nums[j]) * suf[j + 1])
		return ans
## 灵神题解——优化思路：前缀最大值可以在计算答案的同时算出来
class Solution2:
	def maximumTripletValue(self, nums):
		ans = 0
		n = len(nums)
		suf_max = [0] * (n + 1)
		for p1 in range(n - 1, 1, -1):
			suf_max[p1] = max(suf_max[p1 + 1], nums[p1])
		pre_max = 0
		for j, x in enumerate(nums):
			ans = max(ans, (pre_max - x) * suf_max[j + 1])
			pre_max = max(pre_max, x)
		return ans

# 5.回旋镖的数量
class Solution1:
	def numberOfBoomerangs(self, points):
		ans = 0
		for i, point1 in enumerate(points):
			cnt = defaultdict(int)
			for j, point2 in enumerate(points):
				dis = (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2
				ans += cnt[dis] * 2
				cnt[dis] += 1
		return ans

# 6.132模式
class Solution1:
	def find132pattern(self, nums):
		n = len(nums)
		pre_min = [nums[0]] * n
		for l in range(1, n):
			pre_min[l] = min(pre_min[l - 1], nums[l])
		for j in range(n - 2, 0, -1):
			k = j + 1
			while k < n:
				if pre_min[j - 1] < nums[k] < nums[j]:
					return True
				k += 1
		return False
## 枚举k（会错乱）
class Solution1:
	def find132pattern(self, nums):
		n = len(nums)
		pre_min = [nums[0]] * n
		for l in range(1, n):
			pre_min[l] = min(pre_min[l - 1], nums[l])
		mid_max = [nums[0]] * n
		for h in range(1, n):
			mid_max[h] = max(mid_max[h - 1], nums[h])
		for k in range(2, n - 1):
			if pre_min[k - 2] < nums[k] < mid_max[k - 1]:
				return True
		return False
## 灵神题解
class Solution1:
	def find132pattern(self, nums):
		n = len(nums)
		st = []
		k = -inf
		for i in range(n - 1, -1, -1):
			if nums[i] < k:
				return True
			while st and nums[i] > nums[st[-1]]:
				k = nums[st.pop()]
			st.append(i)
		return False
## 栈解法
class Solution4:
	def find132pattern(self, nums):
		le = len(nums)
		if le < 2:
			return False

		mi = [nums[0]]  # 前缀和最小值
		for i in range(1, le):
			mi.append(min(nums[i], mi[-1]))

		stack = []
		for i in range(le - 1, -1, -1):
			print(stack)
			if nums[i] > mi[i]:
				while stack and mi[i] >= stack[-1]:
					stack.pop()  # 移除栈顶元素

				if stack and stack[-1] < nums[i]:
					return True
				stack.append(nums[i])
		return False








