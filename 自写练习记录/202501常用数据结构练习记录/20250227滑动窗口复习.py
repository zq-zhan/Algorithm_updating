# 1.定长子串中元音的最大数目
class Solution1:
	def maxVowels(self, s, k):
		ans = 0
		temp_ans = 0
		s = list(s)
		for left, x in enumerate(s):
			temp_ans += 1 if x in 'aeiou' else 0
			if left >= k - 1:
				ans = max(ans, temp_ans)
				temp_ans -= 1 if s[left - k + 1] in 'aeiou' else 0
		return ans

# 2.子数组最大平均数1
class Solution1:
	def findMaxAverage(self, nums, k):
		ans = -inf
		temp_ans = 0
		for left, x in enumerate(nums):
			temp_ans += x
			if left >= k - 1:
				ans = max(ans, temp_ans / k)
				temp_ans -= nums[left - k + 1]
		return ans

# 3.长度为K子数组中的最大和
class Solution2:
	def maximumSubarraySum(self, nums, k):
		ans = 0
		temp_ans = 0
		dic_win = defaultdict(int)
		for left, x in enumerate(nums):
			temp_ans += x
			dic_win[x] += 1
			if left >= k - 1:
				if len(dic_win) == k:
					ans = max(ans, temp_ans)
				temp_num = nums[left - k + 1]
				temp_ans -= temp_num
				if dic_win[temp_num] == 1:
					del dic_win[temp_num]
				else:
					dic_win[temp_num] -= 1
		return ans

# 4.拆炸弹
class Solution1:  # 暴力解法
	def decrypt(self, code, k):
		n = len(code)
		if k == 0:
			return [0] * n
		ans = []
		code = code + code + code
		for i in range(n, 2 * n):
			if k > 0:
				ans.append(sum(code[i + 1:i + k + 1]))
			else:
				ans.append(sum(code[i + k:i]))
		return ans
## 分类讨论
class Solution2:
	def decrypt(self, code, k):
		res_lis = []
		temp_ans = 0
		n = len(code)
		if k > 0:
			new_arr = code[1:] + code
		elif k < 0:
			new_arr = code[k:] + code
		else:
			return [0] * n

		# cnt = 0
		abs_k = abs(k)
		for left, x in enumerate(new_arr):
			temp_ans += x
			# cnt += 1
			if left >= abs_k - 1:
				res_lis.append(temp_ans)
				temp_ans -= new_arr[left - abs_k + 1]
			if len(res_lis) == n:
				break
		return res_lis

# 5.检查一个字符串是否包含所有长度为K的二进制子串
class Solution1:
	def hasAllCodes(sefl, s, k):
		set_win = set()
		temp_win = ''
		for left, x in enumerate(s):
			temp_win += x
			if left >= k - 1:
				set_win.add(temp_win)
				temp_win = temp_win[1:]
		return len(set_win) == 2 ** k


############### 不定长滑动窗口
# 1.无重复字符的最长子串
class Solution1:
	def lengthOfLongestSubstring(self, s):
		temp_win = set()
		left, right = 0, 0
		n = len(s)
		ans = 0
		while right < n:
			while left <= right and s[right] in temp_win:
				temp_win.remove(s[left])
				left += 1
			temp_win.add(s[right])
			ans = max(ans, right - left + 1)
			right += 1
		return ans

# 2.每个字符最多出现两次的最长子字符串
class Solution1:
	def maximumLengthSubstring(self, s):
		dic_win = defaultdict(int)
		ans = 0
		left = 0
		for right, c in enumerate(s):
			dic_win[c] += 1
			while max(dic_win.values()) > 2:
				dic_win[s[left]] -= 1
				left += 1
			ans = max(ans, right - left + 1)
		return ans
## 优化
class Solution2:
	def maximumLengthSubstring(self, s):
		dic_win = defaultdict(int)
		ans = 0
		left = 0
		for right, c in enumerate(s):
			dic_win[c] += 1
			while dic_win[c] > 2:
				dic_win[s[left]] -= 1
				left += 1
			ans = max(ans, right - left + 1)
		return ans

# 3.删掉一个元素以后全为1的最长子数组
class Solution1:
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

# 4.尽可能使字符串相等
class Solution1:
	def equalSubstring(self, s, t, maxCost):
		ans, left = 0, 0
		temp_win = 0
		for right, (x, y) in enumerate(zip(s, t)):
			temp_win += abs(ord(x) - ord(y))
			while temp_win > maxCost:
				temp_win -= abs(ord(s[left]) - ord(t[left]))
				left += 1
			ans = max(ans, right - left + 1)
		return ans

# 5.水果成篮
class Solution1:
	def totalFruit(self, fruits):
		dic_win = defaultdict(int)
		ans, left = 0, 0
		for right, c in enumerate(fruits):
			dic_win[c] += 1
			while len(dic_win) > 2:
				if dic_win[fruits[left]] == 1:
					del dic_win[fruits[left]]
				else:
					dic_win[fruits[left]] -= 1
				left += 1
			ans = max(ans, right - left + 1)
		return ans

# 6.删除子数组的最大得分
class Solution1:
	def maximumUniqueSubarray(self, nums):
		ans, left = 0, 0
		lis_win = []
		temp_sum = 0
		for right, c in enumerate(nums):
			lis_win.append(c)
			temp_sum += c
			while len(set(lis_win)) < right - left + 1:
				temp_sum -= nums[left]
				lis_win = lis_win[1:]
				left += 1
			ans = max(ans, temp_sum)
		return ans
##
class Solution2:
	def maximumUniqueSubarray(self, nums):
		ans, left = 0, 0
		temp_sum = 0
		set_win = set()
		for right, c in enumerate(nums):
			while c in set_win:
				temp_sum -= nums[left]
				set_win.remove(nums[left])
				left += 1
			set_win.add(c)
			temp_sum += c
			ans = max(ans, temp_sum)
		return ans

# 7.最多K个重复元素的最长子数组
class Solution1:
	def maxSubarrayLength(self, nums, k):
		ans = left = 0
		dic_win = defaultdict(int)
		for right, c in enumerate(nums):
			dic_win[c] += 1
			while dic_win[c] > k:
				dic_win[nums[left]] -= 1
				left += 1
			ans = max(ans, right - left + 1)
		return ans


####################### 不定长滑动窗口-求最小
# 1.长度最小的子数组
class Solution1:
	def minSubArrayLen(self, target, nums):
		if sum(nums) < target:
			return 0

		ans = len(nums)
		left = 0
		temp_sum = 0
		for right, c in enumerate(nums):
			temp_sum += c
			while temp_sum >= target:
				ans = min(ans, right - left + 1)
				temp_sum -= nums[left]
				left += 1
		return ans

# 2.最短且字典序最小的美丽子字符串
class Solution1:
	def shortestBeautifulSubstring(self, s, k):
		ans = s + '0'
		left = 0
		temp_sum = 0
		# temp_substr = ''
		for right, c in enumerate(s):
			temp_sum += 1 if c == '1' else 0
			# temp_substr += c
			while temp_sum == k:
				temp_len = right - left + 1
				temp_substr = s[left : right + 1]
				if temp_len < len(ans) or (temp_len == len(ans) and temp_substr < ans):
					ans = s[left : right + 1]
				temp_sum -= 1 if s[left] == '1' else 0
				left += 1
		return ans if len(ans) <= len(s) else ''
## 优化
class Solution5:
	def shortestBeautifulSubstring(self, s, k):
		if s.count('1') < k:
			return ''

		ans = s
		left = 0
		temp_cnt = 0
		for right, c in enumerate(s):
			temp_cnt += int(c)
			while temp_cnt > k or s[left] == '0':
				temp_cnt -= int(s[left])
				left += 1
			if temp_cnt == k:
				temp_str = s[left : right + 1]
				if len(temp_str) < len(ans) or (len(temp_str) == len(ans) and temp_str < ans):
					ans = temp_str
		return ans

# 3.替换子串得到平衡字符串
class Solution4:  
	def balancedString(self, s):
		s_dic = Counter(s)
		m = len(s) // 4
		if len(s_dic) == 4 and min(s_dic.values()) == m:
			return 0

		ans = len(s)
		left = 0
		for right, c in enumerate(s):
			s_dic[c] -= 1
			while max(s_dic.values()) <= m:
				ans = min(ans, right - left + 1)
				s_dic[s[left]] += 1
				left += 1
		return ans 

# 4.无限数组的最短子数组
class Solution1:
	def minSizeSubarray(self, nums, target):
		n = len(nums)
		times = target // sum(nums)
		target = target - times * sum(nums)
		if target == 0:
			return times * n
		nums = nums + nums
		ans = n
		left = 0

		for right, c in enumerate(nums):
			target -= c
			while target <= 0:
				if target == 0:
					ans = min(ans, right - left + 1)
				target += nums[left]
				left += 1
		return ans + times * n if ans < n else -1

# 5.最小覆盖子串
class Solution3:
	def minWindow(self, s, t):
		if s == t:
			return s
		t_dic = Counter(t)
		ans = s + '#'
		left = 0
		for right, c in enumerate(s):
			t_dic[c] -= 1
			while max(t_dic.values()) <= 0:
				t_dic[s[left]] += 1
				if len(ans) > right - left + 1:
					ans = s[left : right + 1]
				left += 1
		return ans if ans != s + '#' else ''

# 6.包含所有三种字符的子字符串数目
## 当满足条件时不断右移left、直到条件不成立，此时满足条件的子字符串个数为left个(0, ..., left - 1)
class Solution1:
	def numberOfSubstrings(self, s):
		dic_win = defaultdict(int)
		ans, left = 0, 0
		for right, c in enumerate(s):
			dic_win[c] += 1
			while len(dic_win) == 3:
				# ans += left + 1
				if dic_win[s[left]] == 1:
					del dic_win[s[left]]
				else:
					dic_win[s[left]] -= 1
				left += 1
			ans += left
		return ans

# 7.统计最大元素出现至少K次的子数组
class Solution1:
	def countSubarrays(self, nums, k):
		max_num = max(nums)
		cnt_win = 0
		ans, left = 0, 0
		for right, c in enumerate(nums):
			cnt_win += 1 if c == max_num else 0
			while cnt_win >= k:
				cnt_win -= 1 if nums[left] == max_num else 0
				left += 1
			ans += left
		return ans

# 8.字符至少出现k次的子字符串1
class Solution1:
	def numberOfSubstrings(self, s, k):
		dic_win = defaultdict(int)
		ans, left = 0, 0
		for right, c in enumerate(s):
			dic_win[c] += 1
			while dic_win[c] >= k:
				dic_win[s[left]] -= 1
				left += 1
			ans += left
		return ans

# 9.统计完全子数组的数目
class Solution1:
	def countCompleteSubarrays(self, nums):
		target = len(set(nums))
		dic_win = defaultdict(int)
		ans, left = 0, 0
		for right, c in enumerate(nums):
			dic_win[c] += 1
			while len(dic_win) == target:
				if dic_win[nums[left]] == 1:
					del dic_win[nums[left]]
				else:
					dic_win[nums[left]] -= 1
				left += 1
			ans += left
		return ans

# 10.统计好子数组的数目
class Solution1:
	def countGood(self, nums, k):
		dic_win = defaultdict(int)
		ans, left = 0, 0
		cnt = 0
		for right, c in enumerate(nums):
			dic_win[c] += 1
			cnt += dic_win[c] - 1

			while cnt >= k:
				cnt -= dic_win[nums[left]] - 1
				dic_win[nums[left]] -= 1
				left += 1
			ans += left
		return ans

# 11.统计重新排列后包含另一个字符串的子字符串数目2
class Solution1:
	def validSubstringCount(self, word1, word2):
		word2_dic = Counter(word2)
		ans = left = 0
		for right, c in enumerate(word1):
			if c in word2:
				word2_dic[c] -= 1
			while max(word2_dic.values()) <= 0:  # 窗口中的元素可以多、但是不可以少，所以word2_dic为负值时也可以满足
				if word1[left] in word2:
					word2_dic[word1[left]] += 1
				left += 1
			ans += left
		return ans
## 优化：Counter较慢
class Solution2:
	def validSubstringCount(self, word1, word2):
		word2_dic = defaultdict(int)
		for x in word2:
			word2_dic[x] += 1
		ans = left = 0
		for right, c in enumerate(word1):
			if c in word2:
				word2_dic[c] -= 1
			while max(word2_dic.values()) <= 0:  # 窗口中的元素可以多、但是不可以少，所以word2_dic为负值时也可以满足
				if word1[left] in word2:
					word2_dic[word1[left]] += 1
				left += 1
			ans += left
		return ans

# 12.乘积小于k的子数组
class Solution1:
	def numSubarrayProductLessThanK(self, nums, k):
		if k <= 1:
			return 0
		ans = left = 0
		plus_win = 1
		for right, c in enumerate(nums):
			plus_win *= c
			while plus_win >= k:
				plus_win /= nums[left]
				left += 1
			ans += right - left + 1
		return ans

# 13.乘积满足k约束的子字符串数量
class Solution1:
	def countKConstraintSubstrings(self, s, k):
		dic_win = defaultdict(int)
		ans = left = 0
		for right, c in enumerate(s):
			dic_win[c] += 1
			while dic_win['1'] > k and dic_win['0'] > k:
				dic_win[s[left]] -= 1
				left += 1
			ans += right - left + 1
		return ans
##
class Solution4:
	def countKConstraintSubstrings(self, s, k):
		dic_win = {'1':0,'0':0}
		ans = left = 0
		for right, c in enumerate(s):
			dic_win[c] += 1
			while min(dic_win.values()) > k:
				dic_win[s[left]] -= 1
				left += 1
			ans += right - left + 1
		return ans

# 14.统计得分小于k的子数组数目
class Solution1:
	def countSubarrays(self, nums, k):
		ans = left = 0
		temp_score = 0
		for right, c in enumerate(nums):
			temp_score += c
			while temp_score * (right - left + 1) >= k:
				temp_score -= nums[left]
				left += 1
			ans += right - left + 1
		return ans

# 15.不间断子数组
class Solution1:
	def continuousSubarrays(self, nums):
		ans = left = 0
		temp_win = defaultdict(int)
		for right, c in enumerate(nums):
			temp_win[c] += 1
			while max(temp_win) - min(temp_win) > 2:
				if temp_win[nums[left]] == 1:
					del temp_win[nums[left]]
				else:
					temp_win[nums[left]] -= 1
				left += 1
			ans += right - left + 1
		return ans

# 16.找出唯一性数组的中位数
class Solution1:  # 错解
	def medianOfUniquenessArray(self, nums):
		ans_lis = []
		left = 0
		temp_win = defaultdict(int)
		for right, c in enumerate(nums):
			temp_win[c] += 1
			while max(temp_win.values()) > 1:
				if temp_win[nums[left]] == 1:
					del temp_win[nums[left]]
				else:
					temp_win[nums[left]] -= 1
				left += 1
			ans_lis.extend(i for i in range(1, right - left + 1))
		ans_lis.sort()
		n = len(ans_lis)
		if n % 2 == 1:
			return ans_lis[n // 2 + 1]
		else:
			return min(ans_lis[n // 2], ans_lis[n // 2 + 1])
class Solution2:
	def medianOfUniquenessArray(self, nums):
		left = 0
		ans_lis = []
		n = len(nums)
		temp_win = defaultdict(int)
		for right, c in enumerate(nums):
			temp_win[c] += 1
			while max

# 17.和相同的二元子数组
class Solution1:
	def numSubarraysWithSum(self, nums, goal):
		def upper_target(nums, target):
			ans = left = 0
			temp_sum = 0
			for right, c in enumerate(nums):
				temp_sum += c
				while left <= right and temp_sum >= target:
					temp_sum -= nums[left]
					left += 1
				ans += left
			return ans
		return upper_target(nums, goal) - upper_target(nums, goal + 1)
## 优化：三指针——同时维护两个left
class Solution2:
	def numSubarraysWithSum(self, nums, goal):
		left1 = left2 = ans = 0
		temp_sum1 = temp_sum2 = 0
		for right, c in enumerate(nums):
			temp_sum1 += c
			temp_sum2 += c
			while left1 <= right and temp_sum1 >= goal:
				temp_sum1 -= nums[left1]
				left1 += 1
			while left2 <= right and temp_sum2 >= goal + 1:
				temp_sum2 -= nums[left2]
				left2 += 1
			ans += left1 - left2
		return ans

# 18.统计优美子数组
class Solution1:
	def numberOfSubarrays(self, nums, k):
		left1 = left2 = ans = 0
		cnt1 = cnt2 = 0
		for right, c in enumerate(nums):
			if c % 2 == 1:
				cnt1 += 1
				cnt2 += 1
			while left1 <= right and cnt1 >= k:
				cnt1 -= 1 if nums[left1] % 2 == 1 else 0
				left1 += 1
			while left2 <= right and cnt2 >= k + 1:
				cnt2 -= 1 if nums[left2] % 2 == 1 else 0
				left2 += 1
			ans += left1 - left2
		return ans


# 19.绝对差不超过限制的最长连续子数组
class Solution1:
	def longestSubarray(self, nums, limit):
		temp_win = defaultdict(int)
		ans = left = 0
		for right, c in enumerate(nums):
			temp_win[c] += 1
			if max(temp_win) - min(temp_win) <= limit:
				ans = max(ans, right - left + 1)
				continue
			if temp_win[nums[left]] == 1:
				del temp_win[nums[left]]
			else:
				temp_win[nums[left]] -= 1
			left += 1
		return ans
##
class Solution1:  # 因为循环内取max所以复杂度为O(n^2)
	def longestSubarray(self, nums, limit):
		temp_win = defaultdict(int)
		ans = left = 0
		for right, c in enumerate(nums):
			temp_win[c] += 1
			while max(temp_win) - min(temp_win) > limit:
				if temp_win[nums[left]] == 1:
					del temp_win[nums[left]]
				else:
					temp_win[nums[left]] -= 1
				left += 1
			ans = max(ans, right - left + 1)
		return ans
### 优化1：有序列表
class Solution2:
	def longestSubarray(self, nums, limit):
		temp_win = SortedList()
		ans = left = 0
		for right, c in enumerate(nums):
			temp_win.add(c)
			while temp_win[-1] - temp_win[0] > limit:
				temp_win.remove(nums[left])
				left += 1
			ans = max(ans, right - left + 1)
		return ans
### 优化2：维护两个队列
class Solution3:
	def longestSubarray(self, nums, limit):
		temp_win = SortedList()
		ans = left = 0
		min_deque = max_deque = deque()
		for right, c in enumerate(nums):
			while max_deque and c > max_deque[-1]:
				max_deque.pop()
			max_deque.append(c)
			while min_deque and c < min_deque[-1]:
				min_deque.pop()
			min_deque.append(c)

			while max_deque[0] - min_deque[0] > limit:
				nums_left = nums[left]
				if nums_left == max_deque[0]:
					max_deque.popleft()
				if nums_left == min_deque[0]:
					min_deque.popleft()
				left += 1
			ans = max(ans, right - left + 1)
		return ans

# 20.适龄的朋友
class Solution1:
	def numFriendRequests(self, ages):
		ages.sort()
		ans = left = 0
		temp_win = defaultdict(int)
		for right, c in enumerate(ages):
			temp_win[c] += 1
			while 

# 21.反转字符串
class Solution1:
	def reverseString(self, s):
		n = len(s)
		left, right = 0, n - 1
		while left < right:
			temp_s = s[left]
			s[left] = s[right]
			s[right] = temp_s
			left += 1
			right -= 1
		return s

# 22.验证回文串
class Solution1:
	def isPalindrome(self, s):
		ori_s = []
		for x in s:
			if x.isalpha():
				ori_s.append(x.lower())
			elif x.isdigit():
				ori_s.append(x)
		n = len(ori_s)
		temp_s = ori_s.copy()
		left, right = 0, n - 1
		while left < right:
			temp_char = ori_s[left]
			ori_s[left] = ori_s[right]
			ori_s[right] = temp_char
			left += 1
			right -= 1
		return temp_s == ori_s
## 优化
class Solution2:
	def isPalindrome(self, s):
		left, right = 0, len(s) - 1
		while left < right:
			while left < right and not s[left].isalnum():
				left += 1
			while left < right and not s[right].isalnum():
				right -= 1
			if s[left].lower() != s[right].lower():
				return False
			left += 1
			right -= 1
		return True

# 23.删除字符串两端相同字符后的最短长度
class Solution1:
	def minimumLength(self, s):
		left, right = 0, len(s) - 1
		while left < right:
			while left <= right and s[left] == s[left + 1]:
				left += 1
			while left <= right and s[right] == s[right - 1]:
				right -= 1
			if left < right and s[left] == s[right]:
				left += 1
				right -= 1
			else:
				break
		return right - left + 1
##
class Solution1:
	def minimumLength(self, s):
		left, right = 0, len(s) - 1
		while left < right:
			while left < right and s[left] == s[left + 1]:
				left += 1
			while left < right and s[right] == s[right - 1]:
				right -= 1
			if s[left] == s[right]:
				left += 1
				right -= 1
			else:
				break
		return max(0,right - left + 1)

# 24.最长乘积等价子数组
class Solution1:
	def maxLength(self, nums):
		def max_gcd(nums):
			return reduce(math.gcd, numbers)
		def min_lcm(nums):
			def lcm(a, b):
				return abs(a * b) // math.gcd(a, b)
			return reduce(lcm, nums)
		def prod(nums):
			ori = 1
			for x in nums:
				ori *= x
			return ori
		left = 0
		ans = 0
		temp_lis = []
		for right, c in enumerate(nums):
			temp_lis.append(c)
			while prod(temp_lis) != max_gcd(temp_lis) * min_lcm(temp_lis):
				temp_lis = temp_lis[1:]
				left += 1
			ans = max(ans, right - left + 1)
		return ans
## 枚举——暴力解法
class Solution2:
	def maxLength(self, nums):
		max_m = lcm(*nums) * max(nums)  # 最大公因数 * 最小公倍数最大的情况
		ans = 0
		n = len(nums)
		for left in range(n):
			m, l, g = 1, 1, 0
			for right in range(left, n):
				x = nums[right]
				m *= x
				l = lcm(l, x)  # 最小公倍数
				g = gcd(g, x)  # 最大公因数
				if m == l * g:
					ans = max(ans, right - left + 1)
				if m > max_m:
					break
		return ans














