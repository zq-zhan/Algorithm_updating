# 1.检查数组是否存在有效划分
class Solution1:
	def validPartition(self, nums):
		n = len(nums)
		f = [True] + [False] * n
		for i in range(n):
			if (i > 0 and f[i - 1] and nums[i] == nums[i - 1]) or \
				(i > 1 and f[i - 2] and (nums[i] == nums[i - 1] == nums[i - 2] or \
					nums[i] == nums[i - 1] + 1 == nums[i - 2] + 2)):
				f[i + 1] = True
		return f[-1]
## 递归
class Solution2:
	def validPartition(self, nums):
		@cache
		def dfs(i):
			if i == -1:
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

# 2.单词拆分
class Solution1:
	def wordBreak(self, s, wordDict):
		wordlen = set(map(len, wordDict))
		@cache
		def dfs(i):
			if i < 0:
				return True
			if i < min(wordlen) - 1:
				return False
			res = False
			for length in wordlen:
				if i >= length - 1 and s[i - length + 1:i + 1] in wordDict:
					res |= dfs(i - length)
			return res
		return dfs(len(s) - 1)

#################### 最优划分 ###############
# 1.分割回文串2
class Solution1:
	def minCut(self, s):
		n = len(s)
		def dfs(i):
			if i <= 0:
				return 0
			res = 0
			for j in range(i + 1, n):
				if s[j:n] != s[j:n][::-1]:
					res += dfs()
			return 
## 灵神题解
class Solution2:
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

# 2.字符串中的额外字符
class Solution1:
	def minExtraChar(self, s, dictionary):
		wordlen = set(map(len, dictionary))
		n = len(s)
		@cache
		def dfs(i):
			if i < 0:
				return 0
			# if i < min(wordlen) - 1:
			# 	return i + 1
			ans = dfs(i - 1) + 1
			# for length in wordlen:
			# 	if i > length - 1 and s[i - length + 1:i + 1] in dictionary:
			# 		ans = min(ans, dfs(i - length))
			for j in range(i + 1):  # 枚举左端点
				if s[j:i + 1] in dictionary:
					ans = min(ans, dfs(j - 1))
			return ans
		return dfs(n - 1)

class Solution2:
	def minExtraChar(self, s, dictionary):
		wordlen = set(map(len, dictionary))
		n = len(s)
		@cache
		def dfs(i):
			if i < 0:
				return 0
			if i < min(wordlen) - 1:
				return i + 1
			ans = dfs(i - 1) + 1  # 不选的时候，ans最大
			for length in wordlen:
				if i >= length - 1 and s[i - length + 1:i + 1] in dictionary:
					ans = min(ans, dfs(i - length))
			# for j in range(i + 1):  # 枚举左端点
			# 	if s[j:i + 1] in dictionary:
			# 		ans = min(ans, dfs(j - 1))
			return ans
		return dfs(n - 1)

class Solution3:
	def minExtraChar(self, s, dictionary):
		wordlen = set(map(len, dictionary))
		n = len(s)
		@cache
		def dfs(i):
			if i < 0:
				return 0
			if i < min(wordlen) - 1:
				return i + 1
			ans = inf
			for length in wordlen:
				if i >= length - 1 and s[i - length + 1:i + 1] in dictionary:
					ans = min(ans, dfs(i - length))
			ans = min(ans, dfs(i - 1) + 1)
			return ans
		return dfs(n - 1)
