# 1.找出最大的几近缺失整数
class Solution1:
	def largestInteger(self, nums, k):
		n = len(nums)	
		if k == n:
			return max(nums)
		temp_win = defaultdict(int)
		for i in range(n - k + 1):
			for j in range(i, i + k):
				temp_win[nums[j]] += 1
		ans = -1
		for x in temp_win:
			if temp_win[x] == 1:
				ans = max(ans, x)
		return ans
## 优化
class Solution2:
	def largestInteger(self, nums, k):
		n = len(nums)
		nums_dic = Counter(nums)
		if k == n:
			return max(nums)
		elif k == 1:
			ans = -1
			for x in nums_dic:
				if nums_dic[x] == 1:
					ans = max(ans, x)
			return ans
		else:
			a = nums[0]
			b = nums[-1]
			if nums_dic[a] == 1 and nums_dic[b] == 1:
				return max(a, b)
			elif nums_dic[a] == 1 and nums_dic[b] != 1:
				return a
			elif nums_dic[a] != 1 and nums_dic[b] == 1:
				return b
			else:
				return -1

# 2.最长回文子序列
class Solution1:  # 记忆化搜索
	def longestPalindromeSubseq(self, s):
		@cache
		def dfs(i, j):  # s[i]到s[j]的最长回文子序列长度
			if i > j:  # 空串
				return 0
			elif i == j:  # 只有一个字符
				return 1
			elif s[i] == s[j]:
				return dfs(i + 1, j - 1) + 2
			else:
				return max(dfs(i + 1, j), dfs(i, j - 1))
		return dfs(0, len(s) - 1)
class Solution2:  # 递归写法
	def longestPalindromeSubseq(self, s):
		n = len(s)
		f = [[0] * n for _ in range(n)]
		for i in range(n - 1, -1, -1):
			f[i][i] = 1
			for j in range(i + 1, n):
				if s[i] == s[j]:
					f[i][j] = f[i + 1][j - 1] + 2
				else:
					f[i][j] = max(f[i + 1][j], f[i][j - 1])
		return f[0][n - 1]

# 3.至多K次操作后的最长回文子序列
class Solution1:
	def longestPalindromicSubsequence(self, s, k):


# 4.长度至少为M的K个子数组之和
class Solution1:
	def maxSum(self, nums, k, m):
		ans, win_sum = 0, 0
		temp_sum = []
		p1, p2 = 0, 0
		while p2 < len(nums):
			win_sum += nums[p2]
			if p2 - p1 + 1 < m:
				p2 += 1
				continue
			else:
				temp_sum.append([p1,p2])
				temp_sum.append(win_sum)
				win_sum -= nums[p1]
				p1 += 1
				p2 += 1








