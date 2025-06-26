############# 常用枚举技巧 #################
# 1.两数之和
class Solution:
	def twoSum(self, nums, target):
		n = len(nums)
		dic_left = defaultdict(int)
		for i, x in enumerate(nums):
			if target - x in dic_left:
				return [dic_left[target - x], i]
			dic_left[x] = i

# 2.与对应负数同时存在的最大正整数
class Solution:
	def findMaxK(self, nums):
		ans = -1
		set_win = set()
		for x in nums:
			if -x in set_win:
				ans = max(ans, abs(x))
			set_win.add(x)
		return ans

# 3.好数对的数目
class Solution:
	def numIdenticalPairs(self, nums):
		ans = 0
		dic_win = defaultdict(int)
		for x in nums:
			if x in dic_win:
				ans += dic_win[x]
			dic_win[x] += 1
		return ans

# 4.可互换矩形的组数
class Solution:
	def interchangeableRectangles(self, rectangles):
		dic_win = defaultdict(int)
		ans = 0
		for width, height in rectangles:
			if width/height in dic_win:
				ans += dic_win[width/height]
			dic_win[width/height] += 1
		return ans

# 5.等价多米诺骨牌对的数量
class Solution:
	def numEquivDominoPairs(self, dominoes):
		ans = 0
		dic_win = defaultdict(int)
		for a, b in dominoes:
			# temp = (a, b) if a <= b else (b, a)
			# if temp in dic_win: 
			# 	ans += dic_win[temp]
			# dic_win[temp] += 1
			## 优化
			temp = tuple(sorted(d))
			ans += dic_win[temp]
			dic_win[temp] += 1
		return ans

# 6.买卖股票的最佳时机
class Solution:
	def maxProfit(self, prices):
		buy = max(prices)
		sold = 0
		ans = 0
		for x in prices:
			if x < buy:
				buy = x
				sold = 0
				continue
			sold = max(sold, x)
			ans = max(sold - buy, 0)
		return ans
##
class Solution:
	def maxProfit(self, prices):
		buy = max(prices)
		ans = 0
		for sold in prices:
			ans = max(ans, sold - buy)
			buy = min(buy, sold)
		return ans

# 7.存在重复元素2
class Solution:
	def containsNearbyDuplicate(self, nums, k):
		dic_win = defaultdict(int)
		for i, x in enumerate(nums):
			if x in dic_win and abs(i - dic_win[x]) <= k:
				return True
			dic_win[x] = i
		return False

# 8.必须拿起的最小连续卡牌数
class Solution:
	def minimumCardPickup(self, cards):
		dic_win = defaultdict(int)
		ans = len(cards) + 1
		for i, x in enumerate(cards):
			if x in dic_win:
				ans = min(ans, i - dic_win[x] + 1)
			dic_win[x] = i
		return ans if ans <= len(cards) else -1

# 9.数组中的最大数对和
class Solution:
	def maxSum(self, nums):
		ans = -1
		dic_win = defaultdict(int)
		for x in nums:
			mx = max(str(x))
			if mx in dic_win:
				ans = max(ans, x + dic_win[mx])
			dic_win[mx] = max(x, dic_win[mx])
		return ans 

# 10.数位和相等数对的最大和
class Solution:
	def maximumSum(self, nums):
		ans = -1
		dic_win = defaultdict(int)
		for x in nums:
			# temp_s = sum(map(int, str(x)))
			## 写法二
			temp_s = 0
			num = x
			while num:
				temp_s += num % 10
				num //= 10
			if temp_s in dic_win:
				ans = max(ans, x + dic_win[temp_s])
			dic_win[temp_s] = max(dic_win[temp_s], x)
		return ans

# 11.K和数对的最大数目
## 双指针解法，O(nlogn)
class Solution:
	def maxOperations(self, nums, k):
		nums.sort()
		p1 = ans = 0
		p2 = len(nums) - 1
		while p1 < p2:
			temp_s = nums[p1] + nums[p2]
			if temp_s < k:
				p1 += 1
			elif temp_s == k:
				ans += 1
				p1 += 1
				p2 -= 1
			else:
				p2 -= 1
		return ans
## 枚举技巧,O(n)
class Solution:
	def maxOperations(self, nums, k):
		dic_win = defaultdict(int)
		ans = 0
		for x in nums:
			if dic_win[k - x]:
				dic_win[k - x] -= 1
				ans += 1
				continue
			dic_win[x] += 1
		return ans

# 12.数对和
class Solution:
	def pairSums(self, nums, target):
		ans = []
		dic_win = defaultdict(int)
		for x in nums:
			if dic_win[target - x]:
				ans.append([target - x, x])
				dic_win[target - x] -= 1
				continue
			dic_win[x] += 1
		return ans

# 13.识别数组中的最大异常值
## 枚举异常值
class Solution:
	def getLargestOutlier(self, nums):
		s = sum(nums)
		ans = -inf
		cnt = Counter(nums)
		for x in nums:
			cnt[x] -= 1
			if (s - x) % 2 == 0 and cnt[(s - x) // 2] > 0:
				ans = max(ans, x)
		return ans
## 枚举元素和
class Solution:
	def getLargestOutlier(self, nums):
		s = sum(nums)
		ans = -inf
		cnt = Counter(nums)
		for y in nums:
			t = s - 2 * y
			if t in cnt and (t != y or cnt[t] > 1):
				ans = max(ans, t)
		return ans
## 排序
class Solution:
	def getLargestOutlier(self, nums):
		s = sum(nums)
		nums.sort()
		ans = -inf
		right = len(nums) - 1
		for i, y in enumerate(nums):
			while right >= 0 and 2 * y > s - nums[right]:
				right -= 1
			if 2 * y == s - nums[right] and right != i:
				return nums[right]

# 14.数组列表中的最大距离
class Solution:
	def maxDistance(self, arrays):
		ans = 0
		mn = inf
		mx = -inf
		for new_arr in arrays:
			ans = max(ans, new_arr[-1] - mn, mx - new_arr[0])
			mn = min(mn, new_arr[0])
			mx = max(mx, new_arr[-1])
		return ans

# 15.统计坏数对的数目
class Solution:
	def countBadPairs(self, nums):
		# nums = [(val, i) for i, val in enumerate(nums)]
		ans = 0
		for i, x in enumerate(nums):
			for j in range(i + 1, len(nums)):
				if j - i != nums[j] - x:
					ans += 1
		return ans
## 解法2
class Solution:
	def countBadPairs(self, nums):
		dic_win = defaultdict(int)
		ans = 0
		n = len(nums)
		for i, x in enumerate(nums):
			if dic_win[x - i]:
				ans += dic_win[x - i]
			dic_win[x - i] += 1
		return n * (n - 1) // 2 - ans

# 16.最佳观光组合
class Solution:
	def maxScoreSightseeingPair(self, values):
		ans = 0
		for i, x in enumerate(values):
			for j in range(i + 1, len(values)):
				ans = max(ans, x + values[j] + i - j)
		return ans
class Solution:
	def maxScoreSightseeingPair(self, values):
		ans = 0
		mx = -inf
		for j, x in enumerate(values):
			ans = max(ans, mx + x - j)
			mx = max(mx, x + j)
		return ans

# 17.统计一个数组中好对子的数目
class Solution:
	def countNicePairs(self, nums):
		mod = 10 ** 9 + 7
		def rev(x):
			x = str(x)[::-1]
			return int(x)
		ans = 0
		dic_win = defaultdict(int)
		for x in nums:
			rev_x = rev(x)
			ans += dic_win[x - rev_x]
			dic_win[x - rev_x] += 1
		return ans % mod

# 18.找出满足差值条件的下标2
class Solution:
	def findIndices(self, nums, indexDifference, valueDifference):
		i = 0
		mn = 0
		mx = 0
		for j, y in enumerate(nums):
			if j - i < indexDifference:
				continue
			if nums[i] < nums[mn]:
				mn = i
			if nums[i] > nums[mx]:
				mx = i
			if abs(nums[mn] - y) >= valueDifference:
				return [mn, j]
			if abs(nums[mx] - y) >= valueDifference:
				return [mx, j]
			i += 1
		return [-1, -1]

# 19.总持续时间可被60整除的歌曲
class Solution:
	def numPairsDivisibleBy60(self, time):
		dic_win = defaultdict(int)
		ans = 0
		for x in time:
			ans += dic_win[60 - x % 60]
			if x % 60 == 0:
				dic_win[60] += 1
			else:
				dic_win[x % 60] += 1
		return ans

# 20.构成整天的下标对数目2
class Solution:
	def countCompleteDayPairs(self, hours):
		dic_win = defaultdict(int)
		ans = 0
		for x in time:
			ans += dic_win[(24 - x % 24) % 24]
			dic_win[x % 24] += 1
		return ans

# 21.美丽下标对的数目
class Solution:
	def countBeautifulPairs(self, nums):
		ans = 0
		dic_win = defaultdict(int)
		for j, x in enumerate(nums):
			for i in range(1, 10):
				if gcd(i, x % 10) == 1:
					ans += dic_win[i]
			while x >= 10:
				x //= 10
			dic_win[x] += 1
		return ans

# 22.统计相似字符串对的数目
class Solution:
	def similarPairs(self, words):
		ans = 0
		dic_win = defaultdict(int)
		for word in words:
			word = str(sorted(set(word)))
			ans += dic_win[word]
			dic_win[word] += 1
		return ans

# 23.有序三元组中的最大值2
class Solution:
	def maximumTripletValue(self, nums):
		n = len(nums)
		if n < 3:
			return 0
		# 后缀最大值
		mx_k = [nums[-1]] * n
		for i in range(n - 2, -1, -1):
			mx_k[i - n] = max(mx_k[i + 1], nums[i])

		mx_i = nums[0]
		ans = 0
		for j in range(1, n - 1):
			ans = max(ans, (mx_i - nums[j]) * mx_k[j + 1])
			mx_i = max(mx_i, nums[j])
		return ans

#################### 枚举中间变量 ############
# 1.元素和最小的山形三元组2
class Solution:
	def minimumSum(self, nums):
		n = len(nums)
		mn_k = [nums[-1]] * n
		for i in range(n - 2, -1, -1):
			# mn_k[i - n] = min(nums[i], mn_k[i + 1])
			mn_k[i] = min(nums[i], mn_k[i + 1])

		ans = sum(nums) + 1
		mn_i = nums[0]
		for j in range(1, n - 1):
			if nums[j] > mn_i and nums[j] > mn_k[j + 1]:
				ans = min(ans, mn_i + nums[j] + mn_k[j + 1])
			mn_i = min(mn_i, nums[j])
		return ans if ans <= sum(nums) else -1

# 2.长度为3的不同回文子序列
class Solution:
	def countPalindromicSubsequence(self, s):
		ans = set()
		dic_k = Counter(s[1:])
		pre = s[0]
		for j in range(1, len(s) - 1):
			if dic_k[s[j]] == 1:
				del dic_k[s[j]]
			else:
				dic_k[s[j]] -= 1
			for pre in s[:j]:
				if pre in dic_k:
					ans.add((pre, s[j], pre))

		return len(ans)

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
			for j, a, b in zip(range(26), pre, suf):  # 枚举前缀和后缀的组合，将O(n)优化到常数级O(26)
				if a*b != 0:
					ans.add(chr(j + 97) + s[i] + chr(j + 97))
			pre[ord(s[i]) - ord('a')] += 1  # 维护前缀和
		return len(ans)

# 3.直角三角形
class Solution:
	def numberOfRightTriangles(self, grid):
		ans = 0
		n, m = len(grid), len(grid[0])
		for i, lis in enumerate(grid):
			suf_lis = [0] * m:
			suf_lis[-1] = lis[-1]
			for j in range(m - 2, -1, -1):
				suf_lis[j] = max(suf_lis[j + 1], lis[j])
			pre_mx = 0
			for key in lis:
				if pre_mx == 1 and key and suf_lis[]
## 灵神题解
class Solution:
	def numberOfRightTriangles(self, grid):
		ans = 0
		col_sum = [sum(col) - 1 for col in zip(*grid)]
		for row in grid:
			row_sum = sum(row) - 1
			ans += row_sum * sum(cs for x, cs in zip(row, col_sum) if x)
		return ans

# 4.有序三元组中的最大值2
class Solution:
	def maximumTripletValue(self, nums):
		ans = 0
		n = len(nums)
		suf_mx = [0] * (n + 1)
		for i in range(n - 1, -1, -1):
			suf_mx[i] = max(nums[i], suf_mx[i + 1])
		pre_mx = 0
		for i, mid in enumerate(nums):
			ans = max(ans, (pre_mx - mid) * suf_mx[i + 1])
			pre_mx = max(pre_mx, mid)
		return ans

# 5.统计特殊三元组
class Solution:
	def specialTriplets(self, nums):
		mod = 10 ** 9 + 7
		ans = 0
		suf_dic = defaultdict(int)
		for x in nums:
			suf_dic[x] += 1
		pre_dic = defaultdict(int)
		for x in nums:
			suf_dic[x] -= 1
			ans += pre_dic[x * 2] * suf_dic[x * 2]
			pre_dic[x] += 1
		return ans % mod

# 6.回旋镖的数量
class Solution:
	def numberOfBoomerangs(self, points):
		ans = 0
		for x1, y1 in points:  # 枚举i
			cnt = defaultdict(int)。# 存储i和j的欧式距离，后续枚举到相同的则计数
			for x2, y2 in points:  # 枚举j
				d2 = (x1 - x2) ** 2 + (y1 - y1) ** 2
				ans += cnt[d2] * 2
				cnt[d2] += 1
		return ans

# 7.132模式
class Solution:
	def find132pattern(self, nums):
		n = len(nums)
		suf_mn = [inf] * (n + 1)
		suf_mx = [-inf] * (n + 1)
		for i in range(n - 1, -1, -1):
			suf_mx[i] = max(suf_mx[i + 1], nums[i])
			suf_mn[i] = min(suf_mn[i + 1], nums[i])

		pre_mn = nums[0]
		for j, x in enumerate(nums):
			# if suf_mn[j + 1] >= x or suf_mx[j + 1] <= pre_mn:
			# 	pre_mn = min(pre_mn, x)
			# else:
			# 	return True

			if (pre_mn <= suf_mn[j + 1] <= x or pre_mn <= suf_mx[j + 1] <= x) and x - pre_mn >= 1:
				return True
			pre_mn = min(pre_mn, x)
		return False
## 正确思路：如何在j + 1至 n - 1找到比nums[j]小但比nums[i]大的元素——栈
class Solution:
	def find132pattern(self, nums):
		n = len(nums)
		pre_mn = [nums[0]]
		for i in range(1, n):
			pre_mn.append(min(pre_mn[i - 1], nums[i]))

		st = []
		# for j in range(n - 1, -1, -1):
		# 	if nums[j] > pre_mn[j]:  # 因为前缀最小和是非递减列表
		# 		while st and pre_mn[j] >= st[-1]:
		# 			st.pop()
		# 		if st and st[-1] < nums[j]:
		# 			return True
		# 		st.append(nums[j])
		## 写法二
		for j in range(n - 1, 0, -1):
			if nums[j] > pre_mn[j - 1]:
				while st and pre_mn[j - 1] >= st[-1]:
					st.pop()
				if st and st[-1] < nums[j]:
					return True
				st.append(nums[j])
		return False

###################### 前缀和 ##################
# 1.区域和检索-数组不可变
class NumArray:
    def __init__(self, nums):
    	self.new_arr = [0] * (len(nums) + 1)
    	for i in range(len(nums)):
    		self.new_arr[i + 1] = self.new_arr[i] + nums[i]
        
    def sumRange(self, left, right):
    	return self.new_arr[right + 1] - self.new_arr[left]

# 2.变长子数组求和
class Solution:
	def subarraySum(self, nums):
		# def diff_sum(left, right):
		# 	return pre_s[right + 1] - pre_s[left]

		# n = len(nums)
		# pre_s = [0] * (n + 1)
		# for i, x in enumerate(nums):
		# 	pre_s[i + 1] = pre_s[i] + x

		# ans = 0
		# for i in range(n):
		# 	ans += diff_sum(max(0, i - nums[i]), i)
		# return ans
		ans = 0
		pre_s = [0] * (n + 1)
		for i in range(len(nums)):
			pre_s[i + 1] = pre_s[i] + x
			ans += pre_s[i + 1] - pre_s[max(0, i - nums[i])]  # 如果nums[i] < 0就不能这样
		return ans
## 简洁写法
class Solution:
	def subarraySum(self, nums):
		s = list(accumulate(nums, initial = 0))
		ans = 0
		for i, num in enumerate(nums):
			ans += s[i + 1] - s[max(0, i - nums[i])]
		return ans

# 3.统计范围内的元音字符串数
class Solution:
	def vowelStrings(self, words, queries):
		n = len(words)
		pre_s = [0] * (n + 1)
		for i, word in enumerate(words):
			pre_s[i + 1] = pre_s[i] + int(word[0] in 'aeiou' and word[-1] in 'aeiou')

		ans = []
		for left, right in queries:
			ans.append(pre_s[right + 1] - pre_s[left])
		return ans

# 4.特殊数组2
class Solution:
	def isArraySpecial(self, nums, queries):
		suf_s = [0] * (len(nums) + 1)
		for i, x in enumerate(nums):
			suf_s[i + 1] = suf_s[i] + nums[i]

		ans = []
		for start, end in queries:
			ans.append((suf_s[end + 1] - suf_s[start]) % 2 == 1)
		return ans
## 灵神思路
class Solution:
	def isArraySpecial(self, nums, queries):
		a = []
		n = len(nums)
		for i in range(n - 1):  # 用于检查一定范围内的数组是不是都奇偶不相同
			if nums[i] % 2 != nums[i + 1] % 2:
				a.append(0)
			else:
				a.append(1)
		suf_s = list(accumulate(a, initial = 0))
		ans = []
		for start, end in queries:
			if suf_s[end] - suf_s[start] == 0:
				ans.append(True)
			else:
				ans.append(False)
		return ans

# 5.任意子数组和的绝对值的最大值
class Solution:
	def maxAbsoluteSum(self, nums):
		n = len(nums)
		suf_s = [0] * (n + 1)
		for i, x in enumerate(nums):
			suf_s[i + 1] = suf_s[i] + x

		diff_s = -inf
		pre_mn = 0
		pre_mx = 0
		for i in range(1, n + 1):
			diff_s = max(diff_s, abs(suf_s[i] - pre_mn), abs(suf_s[i] - pre_mx))
			pre_mn = min(pre_mn, suf_s[i])
			pre_mx = max(pre_mx, suf_s[i])
		return diff_s
## 优化
class Solution:
	def maxAbsoluteSum(self, nums):
		# pre_s = [0]
		# for i in range(len(nums)):
		# 	pre_s.append(pre_s[-1] + nums[i])
		pre_s = list(accumulate(nums, initial = 0))
		return max(pre_s) - min(pre_s)  # 因为有abs，不用考虑枚举的顺序
## 动态规划
class Solution:
	def maxAbsoluteSum(self, nums):
		ans = f_max = f_min = 0
		for x in nums:
			f_max = max(f_max, 0) + x
			f_min = min(f_min, 0) + x
			ans = max(ans, f_max, -f_min)
		return ans

# 6.和有限的最长子序列
class Solution:
	def answerQueries(self, nums, queries):
		nums.sort()
		pre_s = [0] 
		for x in nums:
			pre_s.append(pre_s[-1] + x)

		ans = []
		for querie in queries:
			for i, temp_s in enumerate(pre_s):
				if temp_s > querie:
					ans.append(i - 1)
					break
				elif i == len(nums):
					ans.append(i)
		return ans
## 前缀和+二分查找
class Solution:
	def answerQueries(self, nums, queries):
		# def find(target):  # >=x二分查找标准写法
		# 	left, right = -1, len(nums)
		# 	while left + 1 < right:
		# 		mid = (left + right) // 2
		# 		if pre_s[mid] >= target:
		# 			right = mid
		# 		else:
		# 			left = mid
		# 	return right
		nums.sort()
		for i in range(1, len(nums)):
			nums[i] += nums[i - 1] 

		ans = []
		for querie in queries:
			# ans.append(find(querie + 1))  # >x的元素序号作为<=x的元素个数
			ans.append(bisect_right(nums, querie))
		return ans

# 7.两个字符串的切换距离
class Solution:
	def shiftDistance(self, s, t, nextCost, previousCost):
		ord_a = ord('a')
		nextCost += nextCost
		previousCost += previousCost
		for i in range(1, 52):
			nextCost[i] += nextCost[i - 1]
			previousCost[i] += previousCost[i - 1]

		nextCost = [0] + nextCost
		previousCost = [0] + previousCost

		n = len(s)
		ans = 0
		for i in range(n):
			ord_s = ord(s[i]) - ord_a
			ord_t = ord(t[i]) - ord_a
			if ord_s < ord_t:
				ans += min(nextCost[ord_t] - nextCost[ord_s - 1], previousCost[ord_s + 26] - previousCost[ord_t - 1])
			else:
				ans += min(nextCost[ord_s + 26] - nextCost[ord_t - 1], previousCost[ord_s] - previousCost[ord_t - 1])
		return ans
## 灵神题解
class Solution:
	def shiftDistance(self, s, t, nextCost, previousCost):
		nxt_sum = list(accumulate(nextCost + nextCost, initial = 0))
		pre_sum = list(accumulate(previousCost + previousCost, initial = 0))

		ans = 0
		ord_a = ord('a')
		for x, y in zip(s, t):
			x = ord(x) - ord_a
			y = ord(y) - ord_a
			ans += min(nxt_sum[y + 26 if y < x else y] - nxt_sum[x],
						pre_sum[(x + 26 if x < y else x) + 1] - pre_sum[y + 1])
		return ans

# 8.蜡烛之间的盘子
class Solution:
	def platesBetweenCandles(self, s, queries):
		n = len(s)  # 二分找左右两边第一个符合条件序号，再利用前缀和计算
		caddles = []
		for i, x in enumerate(s):
			if x == '|':
				caddles.append(i)
		s = [1 if x == '*' else 0 for x in s ]
		pre_s = list(accumulate(s, initial = 0))
		ans = []
		for left, right in queries:
			left_new = bisect_left(caddles, left)
			right_new = bisect_right(caddles, right) - 1
			diff = pre_s[right] - pre_s[left]
			if left_new < n and right_new >= 0 and left_new < right_new:
				ans.append(pre_s[caddles[right_new]] - pre_s[caddles[left_new]])
			else:
				ans.append(0)
			# while left < right and pre_s[left] != pre_s[left + 1]:  # 超时
			# 	left += 1
			# while left < right and pre_s[right] != pre_s[right + 1]:
			# 	right -= 1
			# ans.append(pre_s[right] - pre_s[left])
		return ans

############ 前缀和与哈希表 ###################
# 1.和相同的二元子数组
class Solution:
	def numSubarraysWithSum(self, nums, goal):
		pre_s = list(accumulate(nums, initial = 0))
		ans = left = 0
		for right, temp_s in enumerate(pre_s):
			if temp_s - pre_s[left] < goal:
				continue
			elif temp_s - pre_s[left] == goal:
				ans += 1
			else:
				left += 1
		return ans
## 前缀和 + 哈希表思路
class Solution:
	def numSubarraysWithSum(self, nums, goal):
		dic_win = defaultdict(int)
		ans = temp_s = 0
		for x in nums:
			dic_win[temp_s] += 1
			temp_s += x
			ans += dic_win[temp_s - goal]
		return ans
## 恰好型滑动窗口思路
class Solution:
	def numSubarraysWithSum(self, nums, goal):
		temp_s1 = temp_s2 = left1 = left2 = 0
		for right, x in enumerate(nums):
			temp_s1 += x
			temp_s2 += x

			while left1 <= right and temp_s1 >= goal:
				temp_s1 -= nums[left1]
				left1 += 1
			while left2 <= right and temp_s2 >= goal + 1:
				temp_s2 -= nums[left2]
				left2 += 1
			ans += (left1 - left2)
		return ans

# 2.和为k的子数组
## 恰好型滑动窗口：错解，因为nums[i]可能为负数，而滑动窗口的前提是变化的单调性
class Solution:
	def subarraySum(self, nums, k):
		ans = left1 = left2 = temp_s1 = temp_s2 = 0
		for right, x in enumerate(nums):
			temp_s1 += x
			temp_s2 += x
			while left1 <= right and temp_s1 >= k:
				temp_s1 -= nums[left1]
				left1 += 1
			while left2 <= right and temp_s2 >= k + 1:
				temp_s2 -= nums[left2]
				left2 += 1
			ans += left1 - left2
		return ans
## 前缀和思路
class Solution:
	def subarraySum(self, nums, k):
		dic_win = defaultdict(int)
		ans = temp_s = 0
		for x in nums:
			dic_win[temp_s] += 1
			temp_s += x
			ans += dic_win[temp_s - k]
		return ans

# 3.和为奇数的子数组数目
class Solution:
	def numOfSubarrays(self, arr):
		mod = 10 ** 9 + 7
		dic_win = defaultdict(int)
		dic_win[0] = 1
		ans = temp_s = 0
		for x in arr:
			temp_s += x
			ans += dic_win[1 - temp_s % 2]
			dic_win[temp_s % 2] += 1
		return ans % mod

# 4.和可被k整除的子数组
class Solution:
	def subarraysDivByK(self, nums, k):
		dic_win = defaultdict(int)
		ans = temp_s = 0
		dic_win[0] = 1
		for x in nums:
			temp_s += x
			ans += dic_win[temp_s % k]
			dic_win[temp_s % k] += 1
		return ans

# 5.连续的子数组和
class Solution:
	def checkSubarraySum(self, nums, k):
		dic_win = defaultdict(int)
		dic_win[0] = -1
		temp_s = 0
		for i, x in enumerate(nums):
			temp_s += x
			target = dic_win.get(temp_s % k, i)
			if target == i:
				dic_win[temp_s % k] = i
			elif target <= j - 2:
				return True
		return False

class Solution:
	def checkSubarraySum(self, nums, k):
		dic_win = defaultdict(int)
		dic_win[0] = 0
		temp_s = 0
		for i, x in enumerate(nums):
			temp_s += x
			if temp_s % k in dic_win and i - dic_win[temp_s % k] + 1 >= 2:
				return True
			if temp_s % k in dic_win:
				dic_win[temp_s % k] = i
		return False

# 6.路径总和3
class Solution:
	def pathSum(self, root, targetSum):
		ans = 0
		dic_win = defaultdict(int)
		dic_win[0] = 1
		def dfs(root, s):
			if not root:
				return 
			nonlocal ans
			s += root.val
			ans += dic_win[s - targetSum]
			dic_win[s] += 1
			dfs(root.left, s)
			dfs(root.right, s)
			dic_win[s] -= 1  # 恢复原状
		dfs(root, 0)
		return ans

# 7.统计美丽子数组数目
class Solution:  # 子数组位运算的异或和等于0，即子数组位运算的异或和曾出现过
	def beautifulSubarrays(self, nums):
		ans = s = 0
		cnt = defaultdict(int)
		cnt[0] = 1
		for x in nums:
			s ^= x
			ans += cnt[s]
			cnt[s] += 1
		return ans

# 8.连续数组
class Solution:
	def findMaxLength(self, nums):
		dic_win = defaultdict(int)
		dic_win[0] = -1
		ans = pre_s = 0
		for i, nums in enumerate(nums):
			pre_s += 1 if nums == 1 else -1
			pre_index = dic_win.get(pre_s, i)
			if pre_index == i:
				dic_win[pre_s] = i
			else:
				ans = max(ans, i - pre_index)  # 因为pre_index 始终是最早出现的那个index
		return ans

# 9.字母与数字
class Solution:
	def findLongestSubarray(self, array):
		dic_win = defaultdict(int)
		dic_win[0] = -1
		mx_ans = pre_s = 0
		temp_index = len(array)
		ans = []
		for i, x in enumerate(array):
			pre_s += 1 if x.isalpha() else -1
			target = dic_win.get(pre_s, i)
			if target == i:
				dic_win[pre_s] = i
			else:
				# if i - dic_win[pre_s] > mx_ans or \
				# 	(i - dic_win[pre_s] == mx_ans and dic_win[pre_s] < temp_index):
				# 	mx_ans = i - dic_win[pre_s]
				# 	ans = array[dic_win[pre_s] + 1:i + 1]
				# 	temp_index = dic_win[pre_s]
				if i - dic_win[pre_s] > mx_ans:
					mx_ans = i - dic_win[pre_s]
					ans = array[dic_win[pre_s] + 1:i + 1]
					# temp_index = dic_win[pre_s]
		return ans
## 灵神题解
class Solution:
	def findLongestSubarray(self, array):
		s = list(accumulate((-1 if v[0].isdigit() else 1 for v in array), initial = 0))
		begin = end = 0
		first = {}
		for i, v in enumerate(s):
			j = first.get(v, -1)
			if j < 0:  # 首次遇到s[i]
				first[v] = i
			elif i - j > end - begin:
				begin, end = j, i
		return array[begin:end]

# 10.最大好子数组和
class Solution:
	# 这种思路都是错误的，因为nums[i]可能是负数，不是子数组越长和越大
	def maximumSubarraySum(self, nums, k):
		dic_win = defaultdict(lambda : inf)
		ans = -inf
		for i, x in enumerate(nums):
			a = dic_win[x + k]
			b = dic_win[x - k]
			ans = max(ans, sum(nums[a:i + 1]), sum(nums[b:i + 1]))
			dic_win[x] = min(dic_win[x], i)
		return ans if ans > -inf else 0
## 灵神题解
class Solution:
	# 在保证|a[i] - a[j]|=k时维护前缀和最小，从而子数组和最大
	def maximumSubarraySum(self, nums, k):
		ans = -inf
		min_s = defaultdict(lambda:inf)  # 存储至相同a[i]下s[i]的最小值
		pre_s = 0
		for x in nums:
			ans = max(ans, pre_s + x - min(min_s[x - k], min_s[x + k]))
			min_s[x] = min(min_s[x], pre_s)
			pre_s += x
		return ans if ans > -inf else 0

#################### 距离和 ##################
# 1.有序数组中差绝对值之和
class Solution:
	def getSumAbsoluteDifferences(self, nums):
		pre_s = list(accumulate(nums, initial = 0))
		n = len(nums)
		ans = []
		for j, x in enumerate(nums):
			# j = bisect_left(nums, x)
			left = j * x - pre_s[j]
			right = pre_s[n] - pre_s[j] - x * (n - j)
			ans.append(left + right)
		return ans


##################### 差分 #####################
# 1.与车相交的点
class Solution:
	def numberOfPoints(self, nums):
		# mx = max((max(a, b) for a, b in nums))
		mx = max(end for _, end in nums)
		new_arr = [0] * (mx + 1)
		for start, end in nums:
			new_arr[start] += 1
			new_arr[end] -= 1
		pre_s = list(accumulate(new_arr))
		return sum(x > 0 for x in pre_s)

# 2.检查是否区域内所有整数都被覆盖
class Solution:
	def isCovered(self, ranges, left, right):
		mx = max(end for _, end in ranges)
		if left > mx:
			return False
		new_arr = [0] * (mx + 2)
		for start, end in ranges:
			new_arr[start] += 1
			new_arr[end + 1] -= 1
		pre_s = list(accumulate(new_arr))
		return all(x > 0 for x in pre_s[left:right + 1])
## 优化
class Solution:
	def isCovered(self, ranges, left, right):
		new_arr = [0] * (50 + 2)
		for start, end in ranges:
			new_arr[start] += 1
			new_arr[end + 1] -= 1

		pre_s = list(accumulate(new_arr))
		return all(x > 0 for x in pre_s[left:right + 1])

# 3.人口最多的年份
class Solution:
	def maximumPopulation(self, logs):
		 new_arr = [0] * 101
		 for start, end in logs:
		 	new_arr[start - 1950] += 1
		 	new_arr[end - 1950] -= 1
		 pre_s = list(accumulate(new_arr))
		 mx = max(pre_s)
		 for i in range(101):
		 	if pre_s[i] == mx:
		 		return i + 1950
## 写法二：哈希表
class Solution:
	def maximumPopulation(self, logs):
		dic_win = defaultdict(int)
		for birth, death in logs:
			dic_win[birth] += 1
			dic_win[death] -= 1

		temp_s = max_s = 0
		for year, s in sorted(dic_win.items()):
			temp_s += s
			if max_s < temp_s:
				max_s = temp_s
				ans = year
		return ans

# 4.分割正方形1
## 浮点二分
class Solution:
	def separateSquares(self, squares):
		M = 100000
		total_area = sum(l * l for _, _, l in squares)

		def check(y):
			area = 0
			for _, yi, l in squares:
				if yi < y:
					area += l * min(y - yi, l)
			return area >= total_area / 2

		left = 0
		right = max_y = max(y + l for _, y, l in squares)
		for _ in range((max_y * M).bit_length()):  # n.bit_length() == floor(log2(n)) + 1（当 n > 0）
			mid = (left + right) / 2
			if check(mid):
				right = mid
			else:
				left = mid
		return (left + right) / 2
## 差分
class Solution:
    def separateSquares(self, separateSquares):
        tot_area = 0
        diff = defaultdict(int)
        for _, y, l in squares:
            tot_area += l * l
            diff[y] += l
            diff[y + l] -= l

        area = sum_l = 0
        for y, y2 in pairwise(sorted(diff)):
            sum_l += diff[y]  # 矩形底边长度之和
            area += sum_l * (y2 - y)  # 底边长 * 高 = 新增面积
            if area * 2 >= tot_area:
                return y2 - (area * 2 - tot_area) / (sum_l * 2)

# 5.统计已测试设备
class Solution:
	def countTestedDevices(self, batteryPercentages):
		ans = 0
		cnt = 0
		for x in batteryPercentages:
			if x - cnt > 0:
				ans += 1
				cnt += 1
		return ans

# 6.拼车
class Solution:
	def carPooling(self, trips, capacity):
		mx = max(to for _, _, to in trips)
		new_arr = [0] * (mx + 1)
		for num, start, to in trips:
			new_arr[start] += num
			new_arr[to] -= num
		pre_s = list(accumulate(new_arr))
		return max(pre_s) <= capacity
## 排序哈希表解法
class Solution:
	def carPooling(self, trips, capacity):
		dic_win = defaultdict(int)
		for num, start, to in trips:
			dic_win[start] += num
			dic_win[to] -= num

		temp_s = 0
		for _, num in sorted(dic_win.items()):
			temp_s += num
			if temp_s > capacity:
				return False
		return True

# 7.航班预订统计
class Solution:
	def corpFlightBookings(self, bookings, n):
		ans = [0] * (n + 1)
		for first, last, seats in bookings:
			ans[first - 1] += seats
			ans[last] -= seats
		return list(accumulate(ans))[:-1]

# 8.零数组变换1
class Solution:
	def isZeroArray(self, nums, queries):
		new_arr = [0] * (len(nums) + 1)
		for left, right in queries:
			new_arr[left] -= 1
			new_arr[right + 1] += 1
		pre_s = list(accumulate(new_arr))[:-1]
		return all(x + y <= 0 for x, y in zip(nums, pre_s))

# 9.合并区间
class Solution:
	def merge(self, intervals):
		mx = max(end for _, end in intervals)
		new_arr = [0] * (mx + 2)
		for start, end in intervals:
			new_arr[start] += 1
			new_arr[end] -= 1

		pre_s = list(accumulate(new_arr))
		ans = []
		left = right = 0
		while 

## 灵神题解
class Solution:
	def merge(self, intervals):
		intervals.sort(key = lambda x:x[0])
		ans = []
		for x in intervals:
			if ans and x[0] <= ans[-1][1]:
				ans[-1][1] = max(ans[-1][1], x[1])
			else:
				ans.append(x)
		return ans

# 10.插入区间
class Solution:
	def insert(self, intervals, newInterval):
		intervals.append(newInterval)
		intervals.sort(key = lambda x:x[0])
		ans = []
		for x in intervals:
			if ans and ans[-1][1] >= x[0]:
				ans[-1][1] = max(ans[-1][1], x[1])
			else:
				ans.append(x)
		return ans

# 11.我的日程安排表3
class MyCalendarThree:

	def __init__(self):
		dic_win = defaultdict(int)
		self.dic_win = dic_win
	
	def book(self, startTime, endTime):
		self.dic_win[startTime] += 1
		self.dic_win[endTime] -= 1
		ans = temp_s = 0
		for order_time, num in sorted(self.dic_win.items):
			temp_s += num
			ans = max(ans, temp_s)
		return ans
## 有序字典
class MyCalendarThree:

	def __init__(self):
		self.dic_win = SortedDict()

	def book(self, startTime, endTime):
		new_arr = self.dic_win
		new_arr[startTime] = new_arr.get(startTime, 0) + 1
		new_arr[endTime] = new_arr.get(endTime, 0) - 1
		ans = temp_s = 0
		for v in new_arr.values():
			temp_s += v
			ans = max(ans, temp_s)
		return ans

# 12.将区间分为最少组数
class Solution:
	def minGroups(self, intervals):
		dic_win = defaultdict(int)
		for left, right in intervals:
			dic_win[left] += 1
			dic_win[right + 1] -= 1
		ans = temp_s = 0
		for key, val in sorted(dic_win.items()):
			temp_s += val
			ans = max(ans, temp_s)
		return ans

# 13.字母移位2
class Solution:
	def shiftingLetters(self, s, shifts):
		n = len(s)
		new_arr = [0] * (n + 1)
		for start, end, direction in shifts:
			if direction:
				new_arr[start] += 1
				new_arr[end + 1] -= 1
			else:
				new_arr[start] -= 1
				new_arr[end + 1] += 1
		pre_s = list(accumulate(new_arr))
		ord_a = ord('a')
		s = list(s)
		for i in range(n):
			s[i] = ch((ord(s[i]) + pre_s[i] - ord_a) % 26 + ord_a)
		return ''.join(s)

# 14.K连续位的最小翻转次数
class Solution:
	def minKBitFlips(self, nums, k):
		n = len(nums)
		nums = nums + [0]
		new_arr = [0] * (n + 1)
		for i in range(n - k + 1):
			new_arr[i] += (1 - x)
			new_arr[i + k] -= (1 - x)

		pre_s = list(accumulate(new_arr))[:-1]
## 
class Solution:
	def minKBitFlips(self, nums, k):
		n = len(nums)
		diff = [0] * (n + 1)
		ans, revCnt = 0, 0
		for i in range(n):
			revCnt += diff[i]
			if (nums[i] + revCnt) % 2 == 0:
				if i + k > n:
					return -1
				ans += 1
				revCnt += 1
				diff[i + k] -= 1
		return ans

# 15.所有排列中的最大和
class Solution:
	def maxSumRangeQuery(self, nums, requests):
		mod = 10 ** 9 + 7
		n = len(nums)
		new_arr = [0] * (n + 1)
		for start, end in requests:
			new_arr[start] += 1
			new_arr[end + 1] -= 1
		pre_s = list(accumulate(new_arr))[:-1]
		pre_s.sort(reverse = True)
		nums.sort(reverse = True)
		return sum(x * y for x, y in zip(nums, pre_s))

# 16.形成目标数组的子数组最少增加次数
class Solution:
	def minNumberOperations(self, target):
		target = [0] + target
		n = len(target)
		ans = 0
		for i in range(1, n):
			ans += max(0, target[i] - target[i - 1])
		return ans

# 17.零数组变换2
'''
逃脱不了循环中的累积确认，即O(n^2)；但是答案值域明确，使用二分法可以优化内存到o(nlogk)
'''
class Solution:
	def minZeroArray(self, nums, queries):
		cnt = 0
		n = len(nums)
		for left, right, val in queries:
			if all(x <= 0 for x in nums):
				return cnt
			for i in range(n):
				if left<= i <= right and nums[i] > 0:
					nums[i] -= val
			cnt += 1
		if all(x <= 0 for x in nums):
			return cnt
		else:
			return -1
## 差分 + 二分
class Solution:
	def minZeroArray(self, nums, queries):
		def check(target):
			new_arr = [0] * (n + 1)
			for left, right, val in queries[:target]:
				new_arr[left] -= val
				new_arr[right + 1] += val
			pre_s = list(accumulate(new_arr))[:-1]
			return all(x + y <= 0 for x, y in zip(pre_s, nums)) 

		q = len(queries)
		n = len(nums)
		left, right = -1, q + 1
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				right = mid
			else:
				left = mid
		return right if right < q + 1 else -1
## 双指针 + 差分
class Solution:
	def minZeroArray(self, nums, queries):
		diff = [0] * (len(nums) + 1)
		sum_d = k = 0
		for i, (x, d) in enumerate(zip(nums, diff)):
			sum_d += d
			while k < len(queries) and sum_d < x:
				left, right, val = queries[k]
				diff[left] += val
				diff[right + 1] -= val
				if left <= i <= right:
					sum_d += val
				k += 1
			if sum_d < x:
				return -1
		return k








