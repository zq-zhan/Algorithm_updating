# 1.在排序数组中查找元素的第一个和最后一个未知
## 开区间二分
class Solution1:
	def searchRange(self, nums, target):
		def lower_bound(nums, target):
			left, right = -1, len(nums)  # 开区间(left, right)
			while left + 1 < right:  # 区间不为空
				mid = (left + right) // 2
				if nums[mid] >= target:
					right = mid  # （left, mid)
				else:
					left = mid  # (mid, right)
	        # 循环结束后 left+1 = right
		    # 此时 nums[left] < target 而 nums[right] >= target
		    # 所以 right 就是第一个 >= target 的元素下标
			return right

		start = lower_bound(nums, target)  # >=x
		end = lower_bound(nums, target + 1) - 1  # <=x
		if start == len(nums) or nums[start] != target:
			return [-1, -1]
		return [start, end]
## 库函数写法
class Solution2:
	def searchRange(self, nums, target):
		start = bisect_left(nums, target)
		end = bisect_right(nums, target) - 1
		if start == len(nums) or nums[start] != target:
			return [-1, -1]
		return [start, end]

# 2.搜索插入位置
class Solution1:
	def searchInsert(self, nums, target):
		def lower_bound(nums, target):
			left, right = -1, len(nums)
			while left + 1 < right:
				mid = (left + right) // 2
				if nums[mid] >= target:
					right = mid
				else:
					left = mid
			return right
		return lower_bound(nums, target)
## 库函数写法
class Solution2:
	def searchInsert(self, nums, target):
		return bisect_left(nums, target)

# 3.二分查找
class Solution1:
	def search(self, nums, target):
		ans = bisect_left(nums, target)
		if ans == len(nums) or nums[ans] != target:
			return -1
		return ans
## 开区间手写二分函数
class Solution2:
	def search(self, nums, target):
		def lower_bound(nums, target):
			left, right = -1, len(nums)
			while left + 1 < right:
				mid = (left + right) // 2
				if nums[mid] >= target:
					right = mid
				else:
					left = mid
			return right
		ans = lower_bound(nums, target)
		if ans == len(nums) or nums[ans] != target:
			return -1
		return ans

# 4.咒语和药水的成功对数
class Solution1:
	def successfulPairs(self, spells, potions, success):
		ans = [0] * len(spells)
		def lower_bound(nums, target):
			left, right = -1, len(nums)
			while left + 1 < right:
				mid = (left + right) // 2
				if nums[mid] >= target:
					right = mid
				else:
					left = mid
			return right

		potions.sort()
		for i, c in enumerate(spells):  # 复杂度：O(mn)
			# nums = [x * c for x in potions]
			ans[i] = len(potions) - lower_bound(potions, (success - 1) // c + 1)
		return ans
##
class Solution2:
	def successfulPairs(self, spells, potions, success):
		ans = []
		potions.sort()
		for x in spells:
			ans.append(len(potions) - bisect_right(potions, (success - 1) // x))
		return ans

# 5.两个数组间的距离值
class Solution1:
	def findTheDistanceValue(self, arr1, arr2, d):
		ans = 0
		for x in arr1:  #O(nm)
			nums = [abs(x - c) for c in arr2]
			if sum(t > d for t in nums) == len(arr2):
				ans += 1
		return ans
## 二分法
class Solution2:
	def findTheDistanceValue(self, arr1, arr2, d):
		arr2.sort()  # O(mlogm + nlogm)
		ans = 0
		for x in arr1:
			start = bisect_left(arr2, x - d)
			# end = bisect_right(arr2, x + d) - 1
			if start == len(arr2) or arr2[start] > x + d:
				ans += 1
		return ans
## 灵神双指针写法
class Solution3:
	def findTheDistanceValue(self, arr1, arr2, d):
		arr1.sort()
		arr2.sort()
		ans = j = 0
		for x in arr1:
			while j < len(arr2) and arr2[j] < x - d:
				j += 1
			if j == len(arr2) or arr2[j] > x + d:
				ans += 1
		return ans

# 6.和有限的最长子序列
class Solution1:
	def answerQueries(self, nums, queries):
		nums.sort()
		new_nums = [nums[0]]
		for i in range(1, len(nums)):
			new_nums.append(new_nums[-1] + nums[i])

		ans = []
		for x in queries:
			ans.append(bisect_right(new_nums, x))
		return ans

# 7.比较字符串最小字母出现的频次
class Solution1:
	def numSmallerByFrequency(self, queries, words):
		def f(s):
			s.sort()
			i = 1
			while i < len(s) and s[i] == s[i - 1]:
				i += 1
			return i
		words = [f(x) for x in words]
		queries = [f(x) for x in queries]
		words.sort()

		ans = []
		for target in queries:
			ans.append(bisect_left(words, target))
		return ans
## 解法二
class Solution2:
	def numSmallerByFrequency(self, queries, words):
		def f(s):
			s_l = list(s)
			s_l.sort()
			return bisect_right(s_l, s_l[0])

		words = [f(x) for x in words]
		queries = [f(x) for x in queries]
		words.sort()
		ans = []
		for target in queries:
			ans.append(len(words) - bisect_right(words, target))
		return ans

# 8.使结果不超过阈值的最小除数
class Solution1:
	def smallestDivisor(self, nums, threshold):
		left, right = 0, max(nums) + 1
		while left + 1 < right:
			mid = (left + right) // 2
			if sum((x - 1 // mid + 1) for x in nums) <= threshold:
				right = mid
			else:
				left = mid
		return left

# 9.完成旅途的最少时间
class Solution1:
	def minimumTime(self, time, totalTrips):
		left = 0
		right = totalTrips * min(time) + 1
		while left + 1 < right:
			mid = (left + right) // 2
			if sum(mid // x for x in time) >= totalTrips:
				right = mid
			else:
				left = mid
		return right

# 10.准时到达的列车最小时速
class Solution1:
	def minSpeedOnTime(self, dist, hours):
		left, right = 0, sum(dist)
		while left + 1 < right:
			mid = (left + right) // 2
			if sum((x - 1) // mid + 1 for x in dist) <= hour:
				right = mid
			else:
				left = mid

		if sum((x - 1) // right + 1 for x in dist) > hour:
			return -1
		return right

# 11.在D天内送达包裹的能力
class Solution3:
	def shipWithinDays(self, weights, days):
		def check(nums, target, days):
			ans = temp_sum = 0
			for x in nums:
				if temp_sum + x <= target:
					temp_sum += x
				else:
					ans += 1
					temp_sum = x
			# if temp_sum <= target:
			ans += 1
			return ans <= days


		left, right = max(weights) - 1, sum(weights)
		while left + 1 < right:
			mid = (left + right) // 2
			if check(weights, mid, days):
				right = mid
			else:
				left = mid
		return right

# 12.爱吃香蕉的珂珂
class Solution1:
	def minEatingSpeed(self, piles, h):
		left, right = 0, max(piles)
		while left + 1 < right:
			mid = (left + right) // 2
			if sum((x - 1) // mid + 1 for x in piles) <= h:
				right = mid
			else:
				left = mid
		return right

# 13.移山所需的最少秒数
class Solution3:
	def minNumberOfSeconds(self, mountainHeight, workerTimes):
		def check(mid, workerTimes, mountainHeight):
			ans = 0
			for x in workerTimes:
				ans += (sqrt(1 + 8 * mid // x) - 1) // 2
			return ans >= mountainHeight


		left, right = 0, max(workerTimes) * (mountainHeight + 1) * mountainHeight // 2 + 1
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid, workerTimes, mountainHeight):
				right = mid
			else:
				left = mid
		return right
## 灵神方法二：最小堆模拟
class Solution1:
	def minNumberOfSeconds(self, mountainHeight, workerTimes):
		h = [(t, t, t) for t in workerTimes]
		heapq.heapify(h)
		for _ in range(mountainHeight):
			nxt, delta, base = h[0]
			heapq.heapreplace(h, (nxt + delta + base, delta + base, base))
		return nxt

# 14.H指数2
class Solution3:
	def hIndex(self, citations):
		left, right = min(citations), max(citations) + 1
		while left + 1 < right:
			mid = (left + right) // 2
			if sum(x // mid >= 1 for x in citations) >= mid:
				left = mid
			else:
				right = mid
		return left

# 15.每个小孩最多能分到多少糖果
class Solution1:
	def maximumCandies(self, candies, k):
		left, right = 0, max(candies) + 1
		while left + 1 < right:
			mid = (left + right) // 2
			if sum(x // mid for x in candies) >= k:
				left = mid
			else:
				right = mid
		return left

# 16.找出出现至少三次的最长特殊子字符串
class Solution1:
	def maximumLength(self, s):
		def check(mid, s):
			ans = 0
			s = list(s)
			for i, c in enumerate(s):
				if s[i] == s[i + 1]:
					continue
				else:

		left, right = 0, len(s)
		while left + 1 < right:
			mid = (left + right) // 2







