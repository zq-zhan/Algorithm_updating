################### 求最长 #################
# 1.无重复字符的最长子串
class Solution1:
	def lengthOfLongestSubstring(self, s):
		dic_win = defaultdict(int)
		ans = left = 0
		for right, c in enumerate(s):
			dic_win[c] += 1
			while dic_win[c] > 1:
				if dic_win[s[left]] == 1:
					del dic_win[s[left]]
				else:
					dic_win[s[left]] -= 1
				left += 1
			ans = max(ans, right - left + 1)
		return ans

# 2.每个字符最多出现两次的最长子串
class Solution1:
	def maximumLengthSubstring(self, s):
		ans = left = 0
		dic_win = defaultdict(int)
		for right, c in enumerate(s):
			dic_win[c] += 1
			while dic_win[c] > 2:
				if dic_win[s[left]] == 1:
					del dic_win[s[left]]
				else:
					dic_win[s[left]] -= 1
				left += 1
			ans = max(ans, right - left + 1)
		return ans

# 3.删掉一个元素以后全为1的最长子数组
class Solution1:
	def longestSubarray(self, nums):
		cnt_win = 0
		ans = left = 0
		for right, c in enumerate(nums):
			cnt_win += (1 - c)
			while cnt_win > 1:
				cnt_win -= 1 - nums[left]
				left += 1
			ans = max(ans, right - left + 1 - cnt_win)
		return ans

# 4.找到最长的半重复子串
class Solution1:
	def longestSemiRepetitiveSubstring(self, s):
		ans = 1
		left = cnt = 0
		n = len(s)
		for right in range(1, n):
			if s[right] == s[right - 1]:
				cnt += 1
			while cnt > 1:
				if s[left] == s[left + 1]:
					cnt -= 1
				left += 1
			ans = max(ans, right - left + 1)
		return ans

# 5.数组的最大美丽值
class Solution1:
	def maximumBeauty(self, nums, k):
		nums.sort()
		ans = left = 0
		for right, c in enumerate(nums):
			while c - nums[left] > k * 2:
				left += 1
			ans = max(ans, right - left + 1)
		return ans

# 6.最高频元素的频数
"""
思路转化为：求可递增k次的最大连续字符串的长度
"""
class Solution1:
	def maxFrequency(self, nums, k):
		ans = 1
		left = 0
		nums.sort()
		n = len(nums)
		for right in range(1, n):
			# if nums[right] == nums[right - 1] or nums[right] - nums[right - 1] <= cnt:
			# 	k -= nums[right] - nums[right - 1]
			# 	ans = max(ans, right - left + 1)
			# else:
			# 	while k < 0:
			# 		k += nums[left + 1] - nums[left]
			# 		left += 1
			k -= (nums[right] - nums[right - 1]) * (right - left)
			while k < 0:
				k += nums[right] - nums[left]
				left += 1
			ans = max(ans, right - left + 1)
		return ans

# 7.每种字符至少取K个
class Solution1:
	def takeCharacters(self, s, k):
		dic_win = defaultdict(int)
		all_dic = Counter(s)
		# if all_dic['a'] < k or all_dic['b'] < k or all_dic['c'] < k:
		# 	return -1
		if any(all_dic[c] < k for c in 'abc'):
			return -1

		n = len(s)
		ans = left = 0
		for right, c in enumerate(s):
			dic_win[c] += 1
			while dic_win[c] > all_dic[c] - k:
				dic_win[s[left]] -= 1
				left += 1
			ans = max(ans, right - left + 1)
		return n - ans

# 8.找出最长等值子数组
class Solution1:
	def longestEqualSubarray(self, nums, k):
		dic_win = defaultdict(int)
		ans = left = cnt = 0
		for right, c in enumerate(nums):
			dic_win[c] += 1
			cnt += 1 if c != 
			while len(dic_win) > 1 and cnt > k:
				if dic_win[nums[left]] == 1:
					del dic_win[nums[left]]
				else:
					dic_win[nums[left]] -= 1
				left += 1
				cnt -= 1
			ans = max(ans, max(dic_win.values()) - cnt)
		return ans
## 
class Solution2:
	def longestEqualSubarray(self, nums, k):
		dic_win = defaultdict(list)
		for i, x in enumerate(nums):
			dic_win[x].append(i - len(dic_win[x]))

		ans = 0
		for pos in dic_win.values():
			if len(pos) < ans:
				continue
			left = 0
			for right, c in enumerate(pos):
				while c - pos[left] > k:
					left += 1
				ans = max(ans, right - left + 1)
		return ans

################# 求最小 ######################
# 1.长度最小的子数组
class Solution1:
	def minSubArrayLen(self, target, nums):
		ans = len(nums) + 1
		left = 0
		temp_sum = 0
		for right, c in enumerate(nums):
			temp_sum += c
			while temp_sum >= target:
				ans = min(ans, right - left + 1)
				temp_sum -= nums[left]
				left += 1
		return ans if ans < len(nums) + 1 else 0

# 2.最短且字典序最小的美丽子字符串
class Solution1:
	def shortestBeautifulSubstring(self, s, k):
		ans = s + '0'
		left = cnt = 0
		temp_s = ''
		for right, c in enumerate(s):
			temp_s += c
			cnt += int(c == '1')
			while cnt == k:
				if len(ans) > len(temp_s) or (len(ans) == len(temp_s) and ans > temp_s):
					ans = temp_s
				temp_s = temp_s[1:]
				cnt -= int(s[left] == '1')
				left += 1
		return ans if ans != s + '0' else ''

# 3.替换子串得到平衡字符串
class Solution1:
	def balancedString(self, s):
		n = len(s)
		target = n // 4
		s_dic = Counter(s)
		if len(s_dic) == 4 and min(s_dic.values()) == target:
			return 0
		ans = len(s)
		left = 0
		for right, c in enumerate(s):
			s_dic[c] -= 1
			while max(s_dic.values()) <= target:
				ans = min(ans, right - left + 1)
				s_dic[s[left]] += 1
				left += 1
		return ans

# 4.无限数组的最短子数组
class Solution1:
	def minSizeSubarray(self, nums, target):
		n = len(nums)
		s = sum(nums)
		cnt = target // s
		target = target % s
		if target == 0:
			return cnt * n
		ans = inf
		left = temp_sum = 0
		nums = nums + nums
		for right, c in enumerate(nums):
			temp_sum += c
			while temp_sum >= target:
				if temp_sum == target:
					ans = min(ans, right - left + 1)
				temp_sum -= nums[left]
				left += 1
		return ans + cnt * n if ans < inf else -1

# 5.最小覆盖子串
class Solution1:
	def minWindow(self, s, t):
		if s == t:
			return s
		t_dic = Counter(t)
		ans = s + '0'
		left = 0
		for right, c in enumerate(s):
			t_dic[c] -= 1
			while max(t_dic.values()) <= 0:
				if max(t_dic.values()) == 0:
					temp_str = s[left:right + 1]
					if len(temp_str) < len(ans) or (len(temp_str) == len(ans) and temp_str < ans):
						ans = s[left:right + 1]
				t_dic[s[left]] += 1
				left += 1
		return ans if len(ans) <= len(s) else ''

###################### 求子数组个数 ##############
########## 越长越合法 ##########
# 1.包含所有三种字符的子字符串数目
class Solution1:
	def numberOfSubstrings(self, s):
		dic_win = {'a':0, 'b':0, 'c':0}
		ans = left = 0
		for right, c in enumerate(s):
			dic_win[c] += 1
			while min(dic_win.values()) > 0:
				dic_win[s[left]] -= 1
				left += 1
			ans += left
		return ans




# 1.字符串至少出现k次的子字符串1
class Solution1:
	def numberOfSubstrings(self, s, k):
		dic_win = defaultdict(int)
		ans = left = 0
		for right, c in enumerate(s):
			dic_win[c] += 1
			while max(dic_win.values()) >= k:
				dic_win[s[left]] -= 1
				left += 1
			ans += left
		return ans

########## 越短越合法 #########
# 1.乘积小于k的子数组
class Solution1:
	def numSubarrayProductLessThanK(self, nums, k):
		if min(nums) >= k:
			return 0
		temp_plus = 1
		ans = left = 0
		for right, c in enumerate(nums):
			temp_plus *= c
			while temp_plus >= k:
				temp_plus /= nums[left]
				left += 1
			ans += right - left + 1
		return ans

# 2.统计满足k约束的子字符串数量1
class Solution1:
	def countKConstraintSubstrings(self, s, k):
		cnt_0 = cnt_1 = ans = left = 0
		for right, c in enumerate(s):
			if c == '0':
				cnt_0 += 1
			else:
				cnt_1 += 1
			while cnt_0 > k and cnt_1 > k:
				if s[left] == '0':
					cnt_0 -= 1
				else:
					cnt_1 -= 1
				left += 1
			ans += right - left + 1
		return ans

# 3.统计得分小于k的子数组数目
class Solution1:
	def countSubarrays(self, nums, k):
		temp_s = ans = left = 0
		for right, c in enumerate(nums):
			temp_s += c
			while temp_s * (right - left + 1) >= k:
				temp_s -= nums[left]
				left += 1
			ans += right - left + 1
		return ans

# 4.不间断子数组
class Solution1:
	def continuousSubarrays(self, nums):
		dic_win = defaultdict(int)
		ans = left = 0
		for right, c in enumerate(nums):
			dic_win[c] += 1
			while max(dic_win.keys()) - min(dic_win.keys()) > 2:
				if dic_win[s[left]] == 1:
					del dic_win[s[left]]
				else:
					dic_win[s[left]] -= 1
				left += 1
			ans += right - left + 1
		return ans

# 5.美观的花束
class Solution1:
	def beautifulBouquet(self, flowers, cnt):
		dic_win = defaultdict(int)
		ans = left = 0
		mod = 10 ** 9 + 7
		for right, c in enumerate(flowers):
			dic_win[c] += 1
			# while max(dic_win.values()) > cnt:
			while dic_win[c] > cnt:
				dic_win[flowers[left]] -= 1
				left += 1
			ans += right - left + 1
		return ans % mod



############ 恰好型滑动窗口 ############
# 1.和相同的二元子数组
## 分解为两个越长越合法问题
class Solution1:
	def numSubarraysWithSum(self, nums, goal):
		def over(target):
			temp_s = ans = left = 0
			for right, c in enumerate(nums):
				temp_s += c
				while left <= right and temp_s >= target:
					temp_s -= nums[left]
					left += 1
				ans += left
			return ans
		return over(goal) - over(goal + 1)
## 三指针做法
class Solution2:
	def numSubarraysWithSum(self, nums, goal):
		temp_s1 = temp_s2 = ans = left1 = left2 = 0
		for right, c in enumerate(nums):
			temp_s1 += c
			temp_s2 += c
			while left1 <= right and temp_s1 >= goal:
				temp_s1 -= nums[left1]
				left1 += 1
			while left2 <= right and temp_s2 >= goal + 1:
				temp_s2 -= nums[left2]
				left2 += 1
			ans += left1 - left2
		return ans

# 2.统计优美子数组
class Solution1:
	def numberOfSubarrays(self, nums, k):
		temp_cnt1 = temp_cnt2 = ans = left1 = left2 = 0
		for c in nums:
			if c % 2 == 1:
				temp_cnt1 += 1
				temp_cnt2 += 1
			while temp_cnt1 >= k:
				temp_cnt1 -= nums[left1] % 2
				left1 += 1
			while temp_cnt2 >= k + 1:
				temp_cnt2 -= nums[left2] % 2
				left2 += 1
			ans += left1 - left2
		return ans

# 3.元音辅音字符串计数2
class Solution1:
	def countOfSubstrings(self, word, k):
		dic_yuan1 = defaultdict(int)
		dic_yuan2 = defaultdict(int)
		cnt_fu1 = cnt_fu2 = ans = left1 = left2 = 0
		for right, c in enumerate(word):
			if c in "aeiou":
				dic_yuan1[c] += 1
				dic_yuan2[c] += 1
			else:
				cnt_fu1 += 1
				cnt_fu2 += 1
			while len(dic_yuan1) == 5 and cnt_fu1 >= k:
				if word[left1] in "aeiou":
					if dic_yuan1[word[left1]] == 1:
						del dic_yuan1[word[left1]]
					else:
						dic_yuan1[word[left1]] -= 1
				else:
					cnt_fu1 -= 1
				left1 += 1
			while len(dic_yuan2) == 5 and cnt_fu2 >= k + 1:
				if word[left2] in "aeiou":
					if dic_yuan2[word[left2]] == 1:
						del dic_yuan2[word[left2]]
					else:
						dic_yuan2[word[left2]] -= 1
				else:
					cnt_fu2 -= 1
				left2 += 1
			ans += left1 - left2
		return ans

# 4.k个不同整数的子数组
class Solution1:
	def subarraysWithKDistinct(self, nums, k):
		def upper_target(target):
			dic_win = defaultdict(int)
			ans = left = 0
			for c in nums:
				dic_win[c] += 1
				while len(dic_win) >= target:
					if dic_win[nums[left]] == 1:
						del dic_win[nums[left]]
					else:
						dic_win[nums[left]] -= 1
					left += 1
				ans += left
			return ans
		return upper_target(k) - upper_target(k + 1)

#################### 随机 ###############
# 1.绝对差不超过限制的最长连续子数组
class Solution1:  # 求最长
	def longestSubarray(self, nums, limit):
		ans = left = 0
		dic_win = defaultdict(int)
		for right, c in enumerate(nums):
			dic_win[c] += 1
			while max(dic_win.keys()) - min(dic_win.keys()) > limit:
				if dic_win[nums[left]] == 1:
					del dic_win[nums[left]]
				else:
					dic_win[nums[left]] -= 1
				left += 1
			ans = max(ans, right - left + 1)
		return ans
## 优化
class Solution2:  # 求最长，复杂度：O(nlogn)
	def longestSubarray(self, nums, limit):
		ans = left = 0
		temp_lis = SortedList()
		for right, c in enumerate(nums):
			temp_lis.add(c)
			while temp_lis[-1] - temp_lis[0] > limit:
				temp_lis.remove(nums[left])
				left += 1
			ans = max(ans, right - left + 1)
		return ans

# 2.适龄的朋友
class Slution1:
	def numFriendRequests(self, ages):
		ages.sort()
		ans = left = 0
		ori_mn = ages[0]
		for right, c in enumerate(nums):
			while c <= 0.5 * ori_mn + 7 or c >= ori_mn or 
## 注意数据范围
class Solution2:
	def numFriendRequests(self, ages):
		cnt = [0] * 121
		for x in ages:
			cnt[x] += 1
		ans = 0
		for ax, x in enumerate(cnt):
			for ay, y in enumerate(cnt):
				if not (ay <= 0.5  ax + 7 or ay > ax or (ay > 100 and ax < 100)):
					ans += x * (y - int(ax == ay))
		return ans

