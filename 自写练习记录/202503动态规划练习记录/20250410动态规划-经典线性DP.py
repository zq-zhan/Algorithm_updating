############## 最长公共子序列（LCS） ##############
# 1.最长公共子序列
## 灵神题解
class Solution1:
	def longestCommonSubsequence(self, text1, text2):
		n, m = len(text1), len(text2)
		@cache
		def dfs(i, j):
			if i < 0 or j < 0:
				return 0
			if text1[i] == text2[j]:
				return dfs(i - 1, j - 1) + 1
			return max(dfs(i - 1, j), dfs(i, j - 1))
		return dfs(n - 1, m - 1)
## 递推写法
class Solution2:
	def longestCommonSubsequence(self, text1, text2):
		n, m = len(text1), len(text2)
		f = [[0] * (m + 1) for _ in range(n + 1)]
		for i, x in enumerate(text1):
			for j, y in enumerate(text2):
				f[i + 1][j + 1] = f[i][j] + 1 if x == y else max(f[i][j + 1], f[i + 1][j])
		return f[-1][-1]

# 2.两个字符串的删除操作
class Solution1:
	def minDistance(self, word1, word2):
		@cache
		def dfs(i, j):
			if i < 0 or j < 0:
				return i + j + 2
			if word1[i] == word2[j]:
				return dfs(i - 1, j - 1)
			return min(dfs(i - 1, j) + 1, dfs(i, j - 1) + 1)
		return dfs(len(word1) - 1, len(word2) - 1)

# 3.两个字符串的最小ascii删除和
class Solution1:
	def minimumDeleteSum(self, s1, s2):
		@cache
		def dfs(i, j):
			if i < 0:
				res = 0
				for x in s2[:j]:
					res += ord(x)
				return res
			if j < 0:
				res = 0
				for x in s1[:j]:
					res += ord(x)
				return res
			if s1[i] == s2[j]:
				return dfs(i - 1, j - 1)
			return min(dfs(i - 1, j) + ord(s1[i]), dfs(i, j - 1) + ord(s2[j]))
		return dfs(len(s1) - 1, len(s2) - 1)
## 解法二
class Solution2:
	def minimumDeleteSum(self, s1, s2):
		s = list(map(ord, s1))
		t = list(map(ord, s2))
		@cache
		def dfs(i, j):
			if i < 0:
				return sum(t[:j + 1])
			if j < 0:
				return sum(s[:i + 1])
			if s[i] == t[j]:
				return dfs(i - 1, j - 1)
			return min(dfs(i - 1, j) + s[i], dfs(i, j - 1) + t[j])
		return dfs(len(s1) - 1, len(s2) - 1)

# 4.编辑距离
class Solution1:
	def minDistance(self, word1, word2):
		n = len(word1)
		m = len(word2)
		# while n < m:
		# 	word1 += str('0')
		# 	n += 1
		@cache
		def dfs(i, j):
			if i < 0:
				return j + 1
			if j < 0:
				return i + 1
			if word1[i] == word2[j]:
				return dfs(i - 1, j - 1)
			return min(dfs(i - 1, j) + 1, dfs(i - 1, j - 1) + 1, dfs(i, j - 1) + 1)  #分别为删除、替换、插入
		return dfs(n - 1, m - 1)

# 5.不相交的线
class Solution1:
	def maxUncrossedLines(self, nums1, nums2):
		@cache
		def dfs(i, j):
			if i < 0 or j < 0:
				return 0
			if nums1[i] == nums2[j]:
				return dfs(i - 1, j - 1) + 1
			return max(dfs(i - 1, j), dfs(i, j - 1))
		return dfs(len(nums1) - 1, len(nums2) - 1)

############### 最长递增子序列（LIS） ###########
# 1.最长递增子序列
## 灵神题解
class Solution1:
	def lengthOfLIS(self, nums):
		@cache
		def dfs(i):
			ans = 0
			for j in range(i):
				if nums[j] < nums[i]:
					ans = max(ans, dfs(j))
			return ans + 1
		return max(dfs(i) for i in range(len(nums)))
## 枚举选哪个
class Solution2:
	def lengthOfLIS(self, nums):
		@cache
		def dfs(i):
			ans = max(dfs(j) for j in range(i) if nums[j] < nums[i], 0)
			return ans + 1  # 1表示选入的nums[i]
		return max(dfs(i) for i in range(len(nums)))
## 二分+贪心
class Solution3:
	def lengthOfLIS(self, nums):
		ans = []
		for x in nums:
			j = bisect_left(ans, x)
			if j == len(ans):
				ans.append(x)
			else:
				ans[j] = x
		return len(ans)  # 如果必须以nums中最后一个元素为终点，则为j+1
## 用LCS求LIS  —— 超时
class Solution3:
	def lengthOfLIS(self, nums):
		nums2 = Sorted(set(nums))
		@cache
		def dfs(i, j):
			if i < 0 or j < 0:
				return 0
			if nums[i] == nums2[j]:
				return dfs(i - 1, j - 1) + 1
			return max(dfs(i - 1, j), dfs(i, j - 1))
		return dfs(len(nums) - 1, len(nums2) - 1)

# 2.将三个组排序
class Solution1:
	def minimumOperations(self, nums):
		n = len(nums)
		@cache
		def dfs(i):
			ans = 0
			for j in range(i):
				if nums[j] <= nums[i]:  # 条件成立时
					ans = max(ans, dfs(j))
			return ans + 1
		return n - max(dfs(i) for i in range(n)) 

# 3.得到山形数组的最少删除次数
class Solution1:  # 错解
	def minimumMountainRemovals(self, nums):
		n = len(nums)
		def dfs(i):
			left = 0
			for j in range(i):
				if nums[j] < nums[i]:
					left = max(left, dfs(j))
			right = 0
			for k in range(i + 1, n):
				if nums[k] < nums[i]:
					right = max(right, dfs(k))
			return right + left + 1
		return n - max(dfs(i) for i in range(n))
## 灵神题解—— ？
class Solution2:
	def minimumMountainRemovals(self, nums):
		n = len(nums)
		suf = [0] * n
		g = []
		for i in range(n - 1, 0, -1):
			x = nums[i]
			j = bisect_left(g, x)
			if j == len(g):
				g.append(x)
			else:
				g[j] = x
			suf[i] = j + 1  # 从nums[i]开始的最长严格递减子序列的长度

		mx = 0  # 最长山形子序列的长度
		g = []
		for i, x in enumerate(nums):
			j = bisect_left(g, x)
			if j == len(g):
				g.append(x)
			else:
				g[j] = x
			pre = j + 1  # 以nums[i]结尾的最长严格递增子序列的长度
			if pre >= 2 and suf[i] >= 2:  # 不一定要等长
				mx = max(mx, pre + suf[i] - 1)
		return n - mx

# 4.找出到每个位置为止最长的有效障碍赛跑路线
class Solution1:
	def longestObstacleCourseAtEachPosition(self, obstacles):
		n = len(obstacles)
		# @cache
		def dfs(i):
			ans = 0
			for j in range(i):
				if obstacles[j] <= obstacles[i]:
					ans = max(ans, dfs(j))
			return ans + 1
		ans = list(dfs(i) for i in range(n))
		return ans
## 二分 + 贪心
class Solution1:
	def longestObstacleCourseAtEachPosition(self, obstacles):
		n = len(obstacles)
		g = []
		ans = []
		for i, x in enumerate(obstacles):
			j = bisect_right(g, x)
			if j == len(g):
				g.append(x)
			else:
				g[j] = x
			ans.append(j + 1)  # 遍历到此时nums[i]、并以它结尾的元素在g列表中的位置，才为以nums[i]结尾的有效障碍跑长度
		return ans




           















