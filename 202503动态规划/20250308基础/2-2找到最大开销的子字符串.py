from collections import defaultdict
from functools import cache
from math import inf

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
		return max(dfs(j) for j in range(-1, n))


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

if __name__ == '__main__':
	s = "adaa"
	chars = "d"
	vals = [-1000]
	print(Solution5().maximumCostSubstring(s, chars, vals))