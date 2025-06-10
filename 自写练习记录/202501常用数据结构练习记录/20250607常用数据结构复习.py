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





