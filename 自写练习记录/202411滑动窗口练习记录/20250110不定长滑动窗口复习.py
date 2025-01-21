# 1、无重复字符的最长子串
class Solution1:
	def lengthOfLongestSubstring(self, s):
		ans = left = 0
		dic_win = defaultdict(int)
		for right, c in enumerate(s):
			dic_win[c] += 1
			while max(dic_win.values()) > 1:
				dic_win[s[left]] -= 1
				left += 1
			ans = max(ans, right - left + 1)
		return ans

# 2、每个字符最多出现两次的最长子字符串
class Solution1:
	def maximumLengthSubstring(self, s):
		ans = left = 0
		dic_win = defaultdict(int)
		for right, c in enumerate(s):
			dic_win[c] += 1
			while max(dic_win.values()) > 2:
				dic_win[s[left]] -= 1
				left += 1
			ans = max(ans, right - left + 1)
		return ans


# 3.删除一个元素以后全为1的最长子数组
class Solution1:
	def longestSubarray(self, nums):
		ans = left = 0
		zero_num = 0
		for right, c in enumerate(nums):
			if nums[right] == 0:
				zero_num += 1
			# ans = max(ans, right - left)
			while zero_num > 1:
				zero_num -= 1 if nums[left] == 0 else 0
				left += 1
			ans = max(ans, right - left)
		return ans

# 4、尽可能使字符串相等
class Solution1:
	def equalSubstring(self, s, t, maxCost):
		ans = left = 0
		for right, c in enumerate(s):
			maxCost -= abs(ord(s[right]) - ord(t[right]))
			while maxCost < 0:
				maxCost += abs(ord(s[left]) - ord(t[left]))
				left += 1
			ans = max(ans, right - left + 1)
		return ans

# 5、找到最长的半重复子字符串
class Solution1:
	def longestSemiRepetitiveSubstring(self, s):
		ans = 1
		left = 0
		temp_cnt = 0
		for right in range(1, len(s)):
			if s[right] == s[right - 1]:
				temp_cnt += 1
			while temp_cnt > 1:
				if s[left] == s[left + 1]:
					temp_cnt -= 1
				left += 1
			ans = max(ans, right - left + 1)
		return ans


######################################## 不定长滑动窗口——求最小#######################
# 1.长度最小的子数组
class Solution5:
	def minSubArrayLen(self, target, nums):
		ans = len(nums) + 1
		left = 0
		sum_win = 0
		for right, c in enumerate(nums):
			sum_win += c
			while sum_win >= target:
				ans = min(ans, right - left + 1)
				sum_win -= nums[left]
				left += 1
		return ans if ans <= len(nums) else 0
# 2.最短且字典序最小的美丽子字符传
class Solution1:
	def shortestBeautifulSubstring(self, s, k):
		ans = s + '0'
		left = 0
		substr_cnt = 0
		for right, c in enumerate(s):
			substr_cnt += 1 if c == '1' else 0
			while substr_cnt == k:
				if len(ans) > right - left + 1 or (len(ans) == right - left + 1 and ans > s[left:right+1]):
					ans = s[left:right + 1]
				substr_cnt -= 1 if s[left] == '1' else 0
				left += 1
		return ans if len(ans) <= len(s) else ''
# 3.替换子串得到平衡子串
class Solution1:  # 错误，注意待替换子串必须是连续的
	def balancedString(self, s):
		ans = 0
		left = 0
		n = len(s)
		dic_all = {'Q':0, 'E':0, 'W':0, 'R':0}
		for x in s:
			dic_all[x] += 1
		for x in 'QWER':
			while dic_all[x] > n // 4:
				ans += 1
				dic_all[x] -= 1
				if dic_all['Q'] < n // 4:
					dic_all['Q'] += 1
				elif dic_all['E'] < n // 4:
					dic_all['E'] += 1
				elif dic_all['W'] < n // 4:
					dic_all['W'] += 1
				elif dic_all['R'] < n // 4:
					dic_all['R'] += 1
		return ans
## 灵神题解
class Solution2:
	def balancedString(self, s):
		m = len(s) // 4
		cnt = Counter(s)
		if len(cnt) == 4 and min(cnt.values()) == m:
			return 0

		ans = len(s) + 1
		left = 0
		for right, c in enumerate(s):
			cnt[c] -= 1
			while max(cnt.values()) <= m:
				ans = min(ans, right - left + 1)
				cnt[s[left]] -= 1
				left += 1
		return ans
# 4.无限子数组的最短子数组
class Solution1:
	def minSizeSubarray(self, nums, target):
		ans = inf
		left = 0
		temp_sum = 0
		n = len(nums)
		for right in range(0, 10 ** 5 + 1):
			temp_sum += nums[right % n]
			while temp_sum >= target:
				if temp_sum == target:
					ans = min(ans, right - left + 1)
				temp_sum -= nums[left % n]
				left += 1
		return ans
## 关键：解析题意
## 灵神题解——
class Solution2:
	def minSizeSubarray(self, nums, target):
		total = sum(nums)
		n = len(nums)
		ans = inf
		left = s = 0
		for right in range(n * 2):
			s += nums[right % n]
			while s >= target % total:
				if s == target % total:
					ans = min(ans, right - left + 1)
				s -= nums[left % n]
				left += 1
		return ans + target // total * n if ans < inf else -1

# 5.删除最短的子数组使剩余数组有序
class Solution1:
	def findLengthOfShortestSubarray(self, arr):
		n = len(arr)
		ans = n
		left = 0
		ans_lis = [arr[0]]
		for right, c in enumerate(arr):
			if c >= ans_lis[-1]:
				ans_lis.append(c)
				left += 1
				continue
## 灵神题解
### 方法一：枚举左端点left，移动右端点right，直到arr[left]<=arr[right]
class Solution2:
	def findLengthOfShortestSubarray(self, arr):
		n = len(arr)
		right = n - 1
		while right and arr[right - 1] <= arr[right]:
			right -= 1
		if right == 0:
			return 0

		ans = right  # 删除arr[:right]
		left = 0
		while left == 0 or arr[left - 1] <= arr[left]:
			while right < n and arr[right] < arr[left]:
				right += 1
			ans = min(ans, right - left - 1)  # arr[left] <= arr[right],删除arr[left+1:right]
			left += 1
		return ans
### 方法二：枚举右端点right，移动左端点，直到arr[left]>arr[right]
class Solution3:
	def findLengthOfShortestSubarray(self, arr):
		n = len(arr)
		right = n - 1
		while right and arr[right - 1] <= arr[right]:
			right -= 1
		if right == 0:
			return 0
		ans = right
		left = 0
		while True:
			while right == n or arr[left] <= arr[right]:
				ans = min(ans, right - left - 1)
				if arr[left] > arr[left + 1]:
					return ans
				left += 1
			right += 1






