# 越长越合法
# 1.包含所有三种字符的子字符串数目
class Solution1:
	def numberOfSubstrings(self, s):
		ans = left = 0
		dic_win = {'a':0, 'b':0, 'c':0}
		for right, c in enumerate(s):
			dic_win[c] += 1
			if min(dic_win.values()) < 1:
				continue
			ans += left + 1
			dic_win[s[left]] -= 1
		return ans
## 灵神题解
class Solution2:
	def numberOfSubstrings(self, s):
		ans = left = 0
		dic_win = {'a':0, 'b':0, 'c':0}
		for x in s:
			dic_win[x] += 1
			while min(dic_win.values()) >= 1:
				dic_win[s[left]] -= 1
				left += 1
				# left += 1
			ans += left
		return ans

# 2.统计最大元素出现至少K次的子数组
class Solution1:
	def countSubarrays(self, nums, k):
		mx = max(nums)
		ans = left = 0
		dic_win = defaultdict(int)
		for right, c in enumerate(nums):
			dic_win[c] += 1
			while dic_win[mx] >= k:
				dic_win[nums[left]] -= 1
				left += 1
			ans += left
		return ans

# 3.字符至少出现k次的子字符串1
class Solution1:
	def numberOfSubstrings(self, s, k):
		ans = left = 0
		dic_win = defaultdict(int)
		for right, c in enumerate(s):
			dic_win[c] += 1
			while max(dic_win.values()) >= k:
				dic_win[s[left]] -= 1
				left += 1
			ans += left
		return ans

# 4.统计完全子数组的数目
class Solution1:  # 复杂度O(n^2)
	def countCompleteSubarrays(self, nums):
		target_num = len(set(nums))
		set_win = []
		ans = left = 0
		for right, c in enumerate(nums):
			set_win.append(c)
			while len(set(set_win)) == target_num:
				set_win = set_win[1:]
				left += 1
			ans += left
		return ans
## 题解二
class Solution2:
	def countCompleteSubarrays(self, nums):
		target_num = len(set(nums))
		dic_win = defaultdict(int)
		ans = left = 0
		for right, c in enumerate(nums):
			dic_win[c] += 1
			while len(dic_win) == target_num:
				if dic_win[nums[left]] == 1:
					del dic_win[nums[left]]
				else:
					dic_win[nums[left]] -= 1
				left += 1
			ans += left
		return ans

# 越短越合法
# 1.乘积小于k的子数组
class Solution1:
	def numSubarrayProductLessThanK(self, nums, k):
		ans = left = 0
		if k <= 1:
			return 0
		temp_plus = 1
		for right, c in enumerate(nums):
			temp_plus *= c
			while temp_plus >= k:
				temp_plus /= nums[left]
				left += 1
			ans += right - left + 1
		return ans
# 2.统计满足K约束的子字符串数量1
class Solution1:
	def countKConstraintSubstrings(self, s, k):
		ans = left = 0
		dic_win = {'0':0, '1':0}
		for right, c in enumerate(s):
			dic_win[c] += 1
			while min(dic_win.values()) > k:
				dic_win[s[left]] -= 1
				left += 1
			ans += right - left + 1
		return ans


# 恰好型滑动窗口
# 1.和相同的二元子数组
class Solution1:
	def numSubarraysWithSum(self, nums, goal):

		def mx_target(x):
			ans = left = 0
			temp_sum = 0
			for right, c in enumerate(nums):
				temp_sum += c
				while left <= right and temp_sum >= x:
					temp_sum -= nums[left]
					left += 1
				ans += left
			return ans
		return mx_target(goal) - mx_target(goal + 1)

