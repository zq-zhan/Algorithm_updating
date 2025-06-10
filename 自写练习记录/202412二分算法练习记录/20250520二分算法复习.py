###### 二分查找 ##########
# 1.在排序数组中查找元素的第一个和最后一个位置
class Solution1:
	def searchRange(self, nums, target):
		# 闭区间写法
		def lower_bound(nums, target):
			left, right = 0, len(nums) - 1
			while left <= right:
				mid = (left + right) // 2
				if nums[mid] < target:
					left = mid + 1
				else:
					right = mid - 1
			return left
		# 左闭右开区间写法
		def lower_bound2(nums, target):
			left, right = 0, len(nums)
			while left < right:
				mid = (left + right) // 2
				if nums[mid] < target:
					left = mid + 1
				else:
					right = mid
			return left
		# 开区间写法
		def lower_bound3(nums, target):
			left, right = -1, len(nums)
			while left + 1 < right:
				mid = (left + right) // 2
				if nums[mid] < target:
					left = mid
				else:
					right = mid
			return right

		start = lower_bound(nums, target)
		if start == len(nums) or nums[start] != target:
			return [-1, -1]
		end = lower_bound(nums, target + 1) - 1
		return [start, end]
 
# 2.搜索插入位置
class Solution1:
	def searchInsert(self, nums, target):
		return bisect_left(nums, target)

# 3.二分查找
class Solution1:
	def search(self, nums, target):
		def lower_bound(target):
			left, right = -1, len(nums)
			while left + 1 < right:
				mid = (left + right) // 2
				if nums[mid] < target:
					left = mid
				else:
					right = mid
			return right
		ans = lower_bound(target)
		if ans < len(nums) and nums[ans] == target:
			return ans
		else:
			return -1

# 4.寻找比目标字母大的最小字母
class Solution1:
	def nextGreatestLetter(self, letters, target):
		def lower_bound(target):
			left, right = -1, len(letters)
			while left + 1 < right:
				mid = (left + right) // 2
				if letters[mid] < target:
					left = mid
				else:
					right = mid
			return right

		target = chr(ord(target) + 1)
		ans = lower_bound(target)
		if ans != len(letters):
			return letters[ans]
		else:
			return letters[0]

# 5.正整数和负整数的最大计数
class Solution1:
	def maximumCount(self, nums):
		def lower_bound(target):
			left, right = -1, len(nums)
			while left + 1 < right:
				mid = (left + right) // 2
				if nums[mid] < target:
					left = mid
				else:
					right = mid
			return right

		pos_num = len(nums) - lower_bound(1)
		neg_num = lower_bound(0) - 1 + 1
		return max(pos_num, neg_num)

# 6.咒语和药水的成功对数
class Solution1:
	def successfulPairs(self, spells, potions, success):
		def lower_bound(nums, target):
			left, right = -1, len(nums)
			while left + 1 < right:
				mid = (left + right) // 2
				if nums[mid] < target:
					left = mid
				else:
					right = mid
			return right

		potions.sort()
		ans = []
		n = len(potions)
		for spell in spells:
			ans.append(n - lower_bound(potions, success / spell))
		return ans

# 7.两个数组间的距离值
class Solution1:
	def findTheDistanceValue(self, arr1, arr2, d):
		p1 = p2 = 0
		arr1.sort()
		arr2.sort()
		n, m = len(arr1), len(arr2)

		while p1 < n:
		while p1 < n and p2 < m:
			if arr1[p1] - arr2[p2] > d:
				break
			elif -d <= arr1[p1] - arr2[p2] <= d:
				p2 += 1
			else:
				p1 += 1
		if p2 == m:
			ans += 1


class Solution1:
	def findTheDistanceValue(self, arr1, arr2, d):
		def lower_bound(nums, target):
			left, right = -1, len(nums)
			while left + 1 < right:
				mid = (left + right) // 2
				if nums[mid] < target:
					left = mid
				else:
					right = mid
			return right

		ans = 0
		for x in arr1:
			new_arr = [abs(x - y) for y in arr2]
			new_arr.sort()
			temp = lower_bound(new_arr, d + 1)
			ans += int(temp == 0)
		return ans
## 灵神题解1:排序+二分查找
class Solution1:
	def findTheDistanceValue(self, arr1, arr2, d):
		arr2.sort()
		ans = 0
		for x in arr1:
			i = bisect_left(arr2, x - d)
			if i == len(arr2) or arr2[i] > x + d:
				ans += 1
		return ans
## 灵神题解2:排序+双指针
'''关键思路：利用两个数组的排序找到指针变化的单调性'''
class Solution2:
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

# 8.距离最小相等元素查询
class Solution1:
	def solveQueries(self, nums, queries):
		nums_cnt = defaultdict(list)
		for i, c in enumerate(nums):
			nums_cnt[c].append(i)

		n = len(queries)
		ans = [-1] * n
		for i, x in enumerate(queries):
			temp = nums_cnt[nums[x]]
			p0 = temp[0]
			temp.insert(0, temp[-1] - len(nums))
			temp.append(p0 + len(nums))
			m = len(temp)
			if m > 3:
				j = bisect_left(temp, x)
				ans[i] = min(x - temp[j - 1], temp[j + 1] - x)
		return ans
## 灵神题解
class Solution1:
	def solveQueries(self, nums, queries):
		nums_cnt = defaultdict(list)
		for i, x in enumerate(nums):
			nums_cnt[x].append(i)

		n = len(nums)
		for p in nums_cnt.values():
			i0 = p[0]
			p.insert(0, p[-1] - n)  # 前后哨兵
			p.append(i0 + n)

		for qi, i in enumerate(queries):
			p = nums_cnt[nums[i]]
			if len(p) == 3:
				queries[qi] = -1
			else:
				j = bisect_left(p, i)
				queries[qi] = min(i - p[j - 1], p[j + 1] - i)
		return queries

# 9.和有限的最长子序列
class Solution1:
	def answerQueries(self, nums, queries):
		def lower_bound(nums, target):
			left, right = -1, len(nums)
			while left + 1 < right:
				mid = (left + right) // 2
				if nums[mid] < target:
					left = mid
				else:
					right = mid
			return right

		nums.sort()
		for i in range(1, len(nums)):
			nums[i] = nums[i] + nums[i - 1]

		ans = []
		for x in queries:
			ans.append(lower_bound(nums, x + 1))
		return ans

# 10.比较字符串最小字母出现频次
class Solution1:
	def numSmallerByFrequency(self, queries, words):
		def f(substr):
			substr = list(substr)
			substr.sort()
			ans = 1
			for i in range(1, len(substr)):
				if substr[i] == substr[i - 1]:
					ans += 1
				else:
					return ans

		def lower_bound(nums, target):
			left, right = -1, len(nums)
			while left + 1 < right:
				mid = (left + right) // 2
				if nums[mid] < target:
					left = mid
				else:
					right = mid
			return right

		queries = [f(querie) for querie in queries]
		words = [f(word) for word in words]
		words.sort()
		ans = []
		for target in queries:
			ans.append(len(words) - lower_bound(words, target + 1))
		return ans

# 11.区间内查询数字的频率
class RangeFreqQuery:
	def __init__(self, arr):
		self.arr = arr

	def query(self, left, right, value):
		nums = self.arr[left:right + 1]
		nums.sort()
		return bisect_right(nums, value) - bisect_left(nums, value)
## 灵神题解
class RangeFreqQuery:
	def __init__(self, arr):
		pos = defaultdict(list)
		for i, x in enumerate(arr):
			pos[x].append(i)
		self.pos = pos

	def query(self, left, right, val):
		a = self.pos[val]
		return bisect_right(a, right) - bisect_left(a, left)

# 12.每一个查询的最大美丽值
class Solution1:
	def maximumBeauty(self, items, queries):
		def lower_bound(nums, target):
			left, right = -1, len(nums)
			while left + 1 < right:
				mid = (left + right) // 2
				if nums[mid] < target:
					left = mid
				else:
					right = mid
			return right

		items_dic = defaultdict(int)
		for price, beauty in items:
			items_dic[price] = max(beauty, items_dic[price])

		ans = [0] * len(queries)
		item_price = list(items_dic.keys())
		item_price.sort()
		for i, querie in enumerate(queries):
			find = lower_bound(item_price, querie + 1)
			temp = 0
			for j in range(find):
				temp = max(temp, items_dic[item_price[j]])
			ans[i] = temp
		return ans

class Solution2:
	def maximumBeauty(self, items, queries):
		def lower_bound(nums, target):
			left, right = -1, len(nums)
			while left + 1 < right:
				mid = (left + right) // 2
				if nums[mid] < target:
					left = mid
				else:
					right = mid
			return right

		items = sorted(items, key = lambda x:x[0])
		items_dic = defaultdict(int)
		pre_price = 0
		for price, beauty in items:
			pre_price = max(pre_price, beauty)
			items_dic[price] = pre_price
		ans = []
		item_price = list(items_dic.keys())
		for querie in queries:
			find = lower_bound(item_price, querie + 1) - 1
			if find == -1:
				ans.append(0)
			else:
				ans.append(items_dic[item_price[find]])
		return ans
## 灵神题解
class Solution2:
	def maximumBeauty(self, items, queries):
		items.sort(key = lambda item:item[0])
		for i in range(1, len(items)):
			items[i][1] = max(items[i][1], items[i - 1][1])

		for i, q in enumerate(queries):
			j = bisect_right(items, q, key = lambda item:item[0])
			queries[i] = items[j - 1][1] if j else 0
		return queries

# 13.快照数组
class SnapshotArray:

	def __init__(self, length):
		self.arr = [0] * length
		self.nums = [self.arr]
		self.snap_id = 0


	def set(self, index, val):
		self.arr[index] = val
		self.nums[self.snap_id] = self.arr

	def snap(self):
		self.snap_id += 1
		self.nums.append(self.arr)
		return self.snap_id - 1

	def get(self, index, snap_id):
		return self.nums[snap_id][index]
## 灵神思路
class SnapshotArray:

	def __init__(self, length):
		self.nums_dic = defaultdict(list)
		self.snap_id = 0

	def set(self, index, val):
		self.nums_dic[index].append((self.snap_id, val))

	def snap(self):
		self.snap_id += 1
		return self.snap_id - 1

	def get(self, index, snap_id):
		find = bisect_left(self.nums_dic[index], (snap_id + 1,)) - 1
		if find == -1:
			return 0
		else:
			return self.nums_dic[index][find][1]

# 14.基于时间的键值存储
class TimeMap:

	def __init__(self):
		self.dic_win = defaultdict(list)


	def set(self, key, value, timestamp) -> None:
		self.dic_win[key].append((timestamp, value))


	def get(self, key, timestamp) -> str:
		find = bisect_left(self.dic_win[key], (timestamp + 1,)) - 1
		if find == -1:
			return ''
		else:
			return self.dic_win[key][find][1]

# 15.设计路由器
class Router:
	def __init__(self, memoryLimit):
		self.arr = []
		self.memoryLimit = memoryLimit

	def addPacket(self, source, destination, timestamp):
		# if (source, timestamp) in self.dic_win[destination]:
		set_temp = set(self.arr)
		if (source, destination, timestamp) in set_temp:
			return False
		else:
			if self.memoryLimit == 0:
				self.arr.pop(0)
			else:
				self.memoryLimit -= 1
			self.arr.append((source, destination, timestamp))
			return True

	def forwardPacket(self):
		if len(self.arr) == 0:
			return []
		else:
			self.memoryLimit += 1
			return self.arr.pop(0)

	def getCount(self, destination, startTime, endTime):
		ans = 0
		for s, d, t in self.arr:
			if d == destination and startTime <= t <= endTime:
				ans += 1
		return ans
## 队列 + 哈希表
class Router:
	def __init__(self, memoryLimit):
		self.set_temp = set()
		self.memoryLimit = memoryLimit
		self.dic_win = defaultdict(deque)
		self.deque_temp = deque()

	def addPacket(self, source, destination, timestamp):
		packet = (source, destination, timestamp)
		if packet in self.set_temp:
			return False
		if len(self.deque_temp) == self.memoryLimit:
			self.forwardPacket()

		self.set_temp.add(packet)
		self.dic_win[destination].append(timestamp)
		self.deque_temp.append(packet)
		return True

	def forwardPacket(self):
		if len(self.deque_temp) == 0:
			return []

		packet = self.deque_temp.popleft()
		self.set_temp.remove(packet)
		self.dic_win[packet[1]].popleft()
		return list(packet)

	def getCount(self, destination, startTime, endTime):
		nums = self.dic_win[destination]
		find_right = bisect_right(nums, endTime) - 1
		find_left = bisect_left(nums, startTime)
		return find_right - find_left + 1

# 16.找到k个最接近的元素
class Solution1:
	def findClosestElements(self, arr, k, x):
		range_num = max(x - arr[0], arr[-1] - x)
		for target in range(1, range_num + 2):
			find_left = bisect_left(arr, x - target)
			find_right = bisect_right(arr, x + target)
			if min(find_right, len(arr) - 1) - find_left >= k:
				return arr[find_left:find_right + 1][:k]
class Solution:
	def findClosestElements(self, arr, k, x):
		n = len(arr)
		left, right = 0, n - 1
		while right - left + 1 > k:
			a = arr[left]
			b = arr[right]
			if abs(a - x) > abs(b - x):
				left += 1
			elif abs(a - x) < abs(b - x):
				right -= 1
			else:
				right -= 1
		return arr[left: right + 1]

# 17.绝对差值和
class Solution1:
	def minAbsoluteSumDiff(self, nums1, nums2):
		mod = 10 ** 9 + 7
		new_lis = []
		n = len(nums1)
		ans = 0
		for i in range(n):
			new_lis.append((i, abs(nums1[i] - nums2[i])))
			ans += abs(nums1[i] - nums2[i])

		new_lis.sort(key = lambda x:x[1])
		k = new_lis[-1][0]

		nums1_set = set(nums1)
		temp_s = ans_ori = ans
		for x in nums1_set:
			temp_s += abs(x - nums2[k]) - abs(nums1[k] - nums2[k])
			ans_ori = min(ans_ori, temp_s)
			temp_s = ans
		return ans_ori % mod
'''
二分查找，找到绝对值减少得最多的一对
'''
class Solution2:
	def minAbsoluteSumDiff(self, nums1, nums2):
		n = len(nums1)
		st = sorted(nums1)
		s, mx = 0, 0
		for x, y in zip(nums1, nums2):
			if x == y:
				continue
			z = abs(x - y)
			s += z
			## 二分查找，找到nums1中最接近y的两个元素
			left, right = -1, n
			while left + 1 < right:
				mid = (left + right) // 2
				if st[mid] < y:
					left = mid
				else:
					right = mid
			mx = max(mx, z - min(abs(st[right] - y) if right < n else z, abs(st[right - 1] - y) if 0 <= right - 1 <= n - 1 else z))
		return (s - mx) % (10 ** 9 + 7)


################# 二分查找 ###############
# 1.使结果不超过阈值的最小除数
class Solution1:
	def smallestDivisor(self, nums, threshold):
		def check(target):
			if sum((x - 1) // target for x in nums) <= threshold - len(nums):
				return True
			else:
				return False

		left, right = 0, max(nums) + 1  # 可优化为0,max(nums)，因为只需要在不确定区间做二分,max(num)一定满足要求
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				right = mid
			else:
				left = mid
		return right

# 2.完成旅途的最少时间
class Solution:
	def minimumTime(self, time: List[int], totalTrips: int) -> int:
		left, right = min(time) * totalTrips - 1, max(time) * totalTrips
		while left + 1 < right:
			mid = (left + right) // 2
			if sum(mid // x for x in time) >= totalTrips:
				right = mid
			else:
				left = mid
		return right

# 3.在D天内送达包裹的能力
class Solution1:
	def shipWithinDays(self, weights, days):
		def check(target):
			temp_s = cnt = 0
			for x in weights:
				if temp_s + x <= target:
					temp_s += x
					continue
				temp_s = x
				cnt += 1
			return cnt + 1 <= days

		left, right = max(weights) - 1, sum(weights)
		while left + 1 < right:
			mid = (left + right) // 2
			if mid >= min(weights) and check(mid):
				right = mid
			else:
				left = mid
		return right

# 4.爱吃香蕉的珂珂
class Solution1:
	def minEatingSpeed(self, piles, h):
		left, right = min(piles) - 1, max(piles)
		while left + 1 < right:
			mid = (left + right) // 2
			if sum((x - 1) // mid for x in piles) <= h - len(piles):
				right = mid
			else:
				left = mid
		return right

# 5.移山所需的最少秒数
class Solution1:
	def minNumberOfSeconds(self, mountainHeight, workerTimes):
		def check(target):
			ans = 0
			for x in workerTimes:
				ans += (sqrt(1 + 8 * target / x) - 1) // 2
			return ans >= mountainHeight

		mx = max(workerTimes)
		left, right = 0, mx * mountainHeight * (mountainHeight + 1) // 2
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				right = mid
			else:
				left = mid
		return right
## 灵神题解2——最小堆模拟
class Solution1:
	def minNumberOfSeconds(self, mountainHeight, workerTimes):
		h = [(t, t, t) for t in workerTimes]
		heapify(h)
		for _ in range(mountainHeight):
			nxt, delta, base = h[0]
			# 工作后总用时，当前工作用时，workerTimes[i]
			heapreplace(h, (nxt + delta + base, delta + base, base))
		return nxt

# 6.供暖器
class Solution1:  # 超时
	def findRadius(self, houses, heaters):
		def check(target):
			heaters_new = []
			for i in range(len(heaters)):
				if i > 0 and heaters[i] - target <= heaters[i - 1] + target + 1:
					heaters_new[-1] = heaters[i] + target
					continue
				heaters_new.append(heaters[i] - target)
				heaters_new.append(heaters[i] + target)
			n = len(heaters_new)
			new_arr = set()
			for j in range(0, n, 2):
				new_arr.add(x for x in range(heaters_new[j], heaters_new[j + 1] + 1))
			for y in houses:
				if y in new_arr:
					continue
				return False
			return True


		houses.sort()
		left, right = 0, max(abs(max(houses) - min(heaters)),abs(min(houses) - max(heaters)))
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				right = mid
			else:
				left = mid
		return right 
## 思路：找到离每个house[i]最近的heater[i]
class Solution2:
	def findRadius(self, houses, heaters):
		houses.sort()
		heaters.sort()
		heaters = [-inf] + heaters + [inf]
		res, n = 0, len(heaters)
		for i, x in enumerate(houses):
			left, right = 0, n - 1
			while left + 1 < right:
				mid = (left + right) // 2
				if heaters[mid] >= x:
					right = mid
				else:
					left = mid
			res = max(res, min(abs(heaters[right] - x), abs(heaters[left] - x)))
		return res

# 7.修车的最少时间
class Solution1:
	def repairCars(self, ranks, cars):
		left, right = 0, max(ranks) * cars ** 2
		while left + 1 < right:
			mid = (left + right) // 2
			if sum(isqrt(mid // x) for x in ranks) >= cars:
				right = mid
			else:
				left = mid
		return right

# 8.制作m束花所需的最少天数
class Solution1:
	def minDays(self, bloomDay, m, k):
		if len(bloomDay) < m * k:
			return -1

		def check(target):
			ans = cnt = 0
			for x in bloomDay:
				if x <= target:
					cnt += 1
					if cnt >= k:
						ans += 1
						cnt = 0
						if ans >= m:
							return True
				else:
					cnt = 0
			return False

		left, right = min(bloomDay) - 1, max(bloomDay)
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				right = mid
			else:
				left = mid
		return right

################ 求最大 ###################
# 1.H指数2
class Solution:
	def hIndex(self, citations):
		left, right = 0, len(citations) + 1
		while left + 1 < right:
			mid = (left + right) // 2
			# if sum(int(x >= mid) for x in citations) >= mid:
			if citations[-mid] >= mid:
				left = mid
			else:
				right = mid
		return left

# 2.每个小孩最多能分到多少糖果
class Solution1:
	def maximumCandies(self, candies, k):
		left, right = 0, min(candies) + 1
		while left + 1 < right:
			mid = (left + right) // 2
			if sum(x // mid for x in candies) >= k:
				left = mid
			else:
				right = mid
		return left

# 3.找出出现至少三次的最长特殊子字符串2
class Solution1:
	def maximumLength(self, s):
		def check(target):
			ans = left = 0
			for right in range(len(s)):
				if s[right] == s[left]:

		n = len(s)
		left, right = 0, n
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				left = mid
			else:
				right = mid
		return left if left > 0 else -1
## 灵神题解
class Solution2:
	def maximumLength(self, s):
		groups = defaultdict(list)
		cnt = 0
		for i, x in enumerate(s):
			cnt += 1
			if i + 1 == len(s) or x != s[i + 1]:
				groups[x].append(cnt)
				cnt = 0

		ans = 0
		for val in groups.values():
			val.sort(reverse = True)
			val.extend([0, 0])
			ans = max(ans, val[0] - 2, min(val[0] - 1, val[1]), val[2])
		return ans if ans else -1
# 二分法
class Solution3:  # O((n + m)log n) m为字符集大小
	# def check(self, s, mid):
	# 	mid_dic = defaultdict(int)
	# 	n = len(s)
	# 	left = 0
	# 	while left < n:
	# 		right = left + 1
	# 		while right < n and s[right] == s[right - 1]:
	# 			right += 1
	# 		if right - left >= mid:
	# 			mid_dic[s[left:left + mid]] += max(0, right - left - mid + 1)
	# 		# mid_dic[s[left]] += max(0, right - left - mid + 1)  # 优化,字符串小于mid的话，right - left - mid + 1 为负数，不影响对符合特殊子串的计数
	# 			if max(mid_dic.values()) >= 3:
	# 				return True
	# 		left = right
	# 	return False

	def maximumLength(self, s):
		def check(target):
			target_dic = defaultdict(int)
			ans = left = 0
			for right in range(1, len(s)):
				if right > 0 and s[right] == s[right - 1]:
					continue
				if right - left >= mid:
					temp_str = s[left:left + target]
					target_dic[temp_str] += max(0, right - left - mid + 1)
					if target_dic[temp_str] >= 3:
						return True
				left = right
			return True

		left, right = -1, len(s)
		while left + 1 < right:
			mid = (left + right) // 2
			if self.check(mid):
				left = mid
			else:
				right = mid
		return left if left > 0 else -1

# 4.求出最多标记下标
class Solution1:
	def maxNumOfMarkedIndices(self, nums):
		def check(target):
			ans = 0
			p2 = n - 1
			p1 = p2 - 1
			while p1 >= 0 and p2 > 0:
				if 2 * nums[p1] <= nums[p2]:
					ans += 2
					p2 -= 1
					if ans >= target:
						return True
				p1 -= 1
			return False

		nums.sort()
		n = len(nums)
		left, right = 0, n + 1
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				left = mid
			else:
				right = mid
		return left if left % 2 == 0 else left - 1

class Solution:
	def maxNumOfMarkedIndices(self, nums):
		nums.sort()
		n = len(nums)
		ans = 0
		p2 = n - 1
		p1 = n // 2 - 1
		while p1 >= 0 and p2 > 0:
			if 2 * nums[p1] <= nums[p2]:
				ans += 2
				p2 -= 1
			p1 -= 1
		return ans

# 5.可移除字符的最大数目
class Solution1:
	def maximumRemovals(self, s, p, removable):
		# def check(target):  # O(nlog2u)
		# 	new_lis = sorted(removable[:target])
		# 	p1 = p2 = 0
		# 	for i, x in enumerate(s):
		# 		if p2 < target and i == new_lis[p2]:
		# 			p2 += 1
		# 			continue
		# 		elif x == p[p1]:
		# 				p1 += 1
		# 				if p1 == m:
		# 					return True
		# 	return False
		def check(target):  # O(nlogU)
			new_lis = set(removable[:target])
			p1 = 0
			for i, x in enumerate(s):
				if i not in new_lis and x == p[p1]:
					p1 += 1
					if p1 == m:
						return True
			return False

		n, m = len(s), len(p)
		left, right = 0, len(removable) + 1
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				left = mid
			else:
				right = mid
		return left

# 6.有界数组中指定下标处的最大值
class Solution1:
	def maxValue(self, n, index, maxSum):
		# def check(target):
		# 	temp = target
		# 	ans = 0
		# 	for i in range(index, -1, -1):
		# 		ans += max(temp, 1)
		# 		temp -= 1
		# 	for i in range(index + 1, n):
		# 		target -= 1
		# 		ans += max(target, 1)
		# 	return ans <= maxSum
		def sum(x, cnt):
			'''
			x 为target，cnt为数组个数
			'''
			if x >= cnt:
				return (x + x - cnt + 1) * cnt // 2
			else:
				return x * (x + 1) // 2 + cnt - x

		left, right = 1, maxSum - n + 2
		while left + 1 < right:
			mid = (left + right) // 2
			if sum(mid - 1, index) + sum(mid, n - index) <= maxSum:
				left = mid
			else:
				right = mid
		return left

# 7.可以到达的最远建筑
class Solution1:
	def furthestBuilding(self, heights, bricks, ladders):
		def check(target):
			ans = [0] * (target + 1)
			for i in range(1, target + 1):
				ans[i] = max(heights[i] - heights[i - 1], 0)
			ans.sort()
			temp_brick = bricks
			temp_ladder = ladders
			for x in ans:
				if temp_brick >= x:
					temp_brick -= x
				elif temp_ladder > 0:
					temp_ladder -= 1
				else:
					return False
			return True


		n = len(heights)
		left, right = 0, n
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				left = mid
			else:
				right = mid
		return left

# 8.最大合金数
class Solution1:
	def maxNumberOfAlloys(self, n, k, budget, composition, stock, cost):
		def check(target):
			for target_composition in composition:
				ans = 0
				for i, x in enumerate(target_composition):
					ans += max((target * x - stock[i]), 0) * cost[i]
				if ans <= budget:
					return True
			return False

		# composition.sort(key = lambda x: sum(x))
		left, right = 0, budget + max(stock) + 1
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				left = mid
			else:
				right = mid
		return left

# 9.价值和小于等于k的最大数字
class Solution:
	def findMaximumNumber(self, k, x):
		def check(target):
			ans = 0
			for num in range(1, mid + 1):
				bin_num = bin(num)[2:]
				ans += sum([bin_num[i] for i in range(0, len(bin_num), x)])
				if ans > k:
					return False
			return True

		left, right = 1, (isqrt(1 + 8 * k) - 1) // 2
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				left = mid
			else:
				right = mid
		return left

################### 二分间接值 ##############
# 1.正方形中的最多点数
class Solution1:
	def maxPointsInsideSquare(self, points, s):
		ans = 0
		def check(target):
			temp_ans = 0
			for _, value in dic_win.items():
				cnt = 0
				for x, y in value:
					if abs(x) <= target and abs(y) <= target:
						cnt += 1
						if cnt > 1:
							return False
				if cnt == 1:
					temp_ans += 1
			nonlocal ans
			ans = max(ans, temp_ans)
			return True


		mx_right = mn_right = 0
		dic_win = defaultdict(list)
		for i, x in enumerate(s):
			dic_win[x].append(points[i])
			mx_right = max(mx_right, points[i][0], points[i][1])
			mn_right = min(mn_right, points[i][0], points[i][1])

		left, right = 0, mx_right - mn_right + 1
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				left = mid
			else:
				right = mid
		return ans
# 2.销售价值减少的颜色球
class Solution1:
	def maxProfit(self, inventory, orders):
		mod = 10 ** 9 + 7
		inventory = [-x for x in inventory]
		heapq.heapify(inventory)
		ans = 0
		while orders > 0:
			x = heapq.heappop(inventory)
			heapq.heappush(inventory, 1 + x)
			ans += -x
			orders -= 1
		return ans % mod
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:

        inventory.sort(reverse=True) #如果不reverse，就要从后往前遍历了
        sell = 0
        ans = 0

        def get(start,cnt,repeat,times): #处理不满的一轮
            ful,left = divmod(times,repeat)
            #并列项数的整数倍部分按照等差数列求和公式，余数乘上卖出整数倍之后的价值
            return (2*start-ful+1)*ful*repeat//2+(start-ful)*left 

        p = 0 
        while p<len(inventory):
            while p<len(inventory)-1 and inventory[p]==inventory[p+1]: #重复项合并处理
                p+=1
            #cnt为每种当前价值最高的球能卖出的数量，注意如果没有下一项，cnt就是当前项本身
            cnt = inventory[p]-inventory[p+1] if p<len(inventory)-1 else inventory[p] 

            if (p+1)*cnt+sell<=orders: #注意数组的下标从0开始，所以并列价值最高的项数是p+1
                #等差数列求和公式，尾项是是当前项减去cnt再加1，不要忘了乘上并列的数量
                ans=(ans+(2*inventory[p]-cnt+1)*(p+1)*cnt//2)%(10**9+7) 
                sell+=(p+1)*cnt
            else: 
                #这种情况对应这轮已经不满，这时可以直接return了
                return (ans+get(inventory[p],cnt,p+1,orders-sell))%(10**9+7)
            p+=1
        return ans #如果没有这一行，orders=sum(inventory)的情况就缺少返回值
## 二分法
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        # 二分查找
        # 提示2：存在某个值k，其中所有价值大于k的球均卖出，部分（可能为0）价值为k的球卖出
        # 要想求出最大总价值和，应该让k尽可能小，这样在卖出一样球的情况下，k越小，所累加的价值就越高
        # 检查对于价值大于k的球的个数，是否超过orders，找到最小的k
        # 找到k之后，说明最初价值大于k的球都会卖出，卖的个数为(inventory[i]-k)，这部分球的卖出的价值可以用等差数列求和
        # ans += (inventory[i] + k + 1) * (inventory[i] - k) // 2 if inventory[i] > k
        # 剩下一部分价值为k的球（可能没有）需要卖出，才能够卖出orders，那么这部分球的个数rest = orders - sum
        # 这一部分球的价值和再加到最终答案中，ans += rest * k
        
        mod = 10**9+7
        l = 0
        r = max(inventory)
        while l <= r:
            mid = (l + r) >> 1
            # 假设价值大于mid的球全部卖出
            s = sum(x - mid for x in inventory if x > mid)
            # 如果价值大于mid的球的个数大于需要卖出的球的个数，说明这个k值应该更大才对
            if s > orders:
                l = mid + 1
            # 否则这个k值应该更小才对
            else:
                r = mid - 1
        k = l
        range_sum = lambda x, y : (x + y) * (y - x + 1) // 2
        rest = orders - sum(x - k for x in inventory if x > k)
        ans = 0
        for x in inventory:
            if x > k:
                ans += range_sum(k+1, x)
        ans += rest * k
        return ans % mod

################### 最小化最大值 ################
# 1.分割数组的最大值
class Solution:
	def splitArray(self, nums, k):
		def check(target):
			cnt = temp_s = 0
			for x in nums:
				if temp_s + x <= target:
					temp_s += x
				else:
					cnt += 1
					temp_s = x
			return cnt + 1 <= k

		left, right = max(nums) - 1, sum(nums)
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				right = mid
			else:
				left = mid
		return right
# 2.分配给商店的最多商品的最小值
class Solution:
	def minimizedMaximum(self, n, quantities):
		def check(target):
			cnt = 0
			for x in quantities:
			# 	while x > 0:
			# 		cnt += 1
			# 		x -= target
			# 		if cnt > n:
			# 			return False
			# return True
				cnt += (x - 1) // target + 1
			return cnt <= n

		left, right = max(quantities) // n - 1, max(quantities)
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				right = mid
			else:
				left = mid
		return right



