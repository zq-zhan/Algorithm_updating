# 1.H指数2
class Solution1:
	def check(self, citations, mid):
		for i,c in enumerate(citations):
			if c >= mid:
				break
		return (len(citations) - i) >= mid
	def hIndex(self, citations):
		left, right = -1, citations[-1] + 1
		while left + 1 < right:
			mid = (left + right) // 2
			if self.check(citations, mid):
				left = mid
			else:
				right = mid
		return left

## 灵神思路优化
class Solution2:
	def hIndex(self, citations):
		left, right = 0, len(citations) + 1
		while left + 1 < right:
			mid = (left + right) // 2
			if citations[-mid] >= mid:
				left = mid
			else:
				right = mid
		return left

# 2.每个小孩最多能分到多少糖果
class Solution1:
	def maximumCandies(self, candies, k):
		left, right = -1, min(candies)
		while left + 1 < right:
			mid = (left + right) // 2
			if sum((x // mid) for x in candies) >= k:
				left = mid
			else:
				right = mid
		return left

# 3.找出出现至少三次的最长特殊子字符串2
## 滑动窗口解法(不行)
class Solution1:
	def maximumLength(self, s):
		left, right = 0, 1
		n = len(s)
		ans = -1
		while left < n and right < n:
			if s[right] == s[right - 1]:
				right += 1
				continue
			if right - left >= 3:
				ans = max(ans, right - left - 2)
			left = right
			right += 1
		if right - left >= 3:
			ans = max(ans, right - left - 2)
		return ans
## 二分法
class Solution2:  # O((n + m)log n) m为字符集大小
	def check(self, s, mid):
		mid_dic = defaultdict(int)
		n = len(s)
		left = 0
		while left < n:
			right = left + 1
			while right < n and s[right] == s[right - 1]:
				right += 1
			if right - left >= mid:
				mid_dic[s[left:left + mid]] += max(0, right - left - mid + 1)
				if max(mid_dic.values()) >= 3:
					return True
			left = right
		return False

	def maximumLength(self, s):
		left, right = -1, len(s)
		while left + 1 < right:
			mid = (left + right) // 2
			if self.check(s, mid):
				left = mid
			else:
				right = mid
		return left if left > 0 else -1
## 灵神思路——贪心
class Solution3:
	def maximumLength(self, s):
		groups = defaultdict(list)
		cnt = 0
		for i, ch in enumerate(s):
			cnt += 1
			if i + 1 == len(s) or ch != s[i + 1]:
				groups[ch].append(cnt)  # 统计连续字符的长度
				cnt = 0

		ans = 0
		for a in groups.values():
			a.sort(reverse = True)
			a.extend([0, 0])
			ans = max(ans, a[0] - 2, min(a[0] - 1, a[1]), a[2])

		return ans if ans else -1

# 4.求出最多标记下标
class Solution1:  # 同向双指针
	def maxNumOfMarkedIndices(self, nums):
		nums.sort()
		# left, right = -1, len(nums) 
		p2 = len(nums) - 1
		ans = 0
		temp = mid = (len(nums) - 1) // 2
		# while left + 1 < right:
			# mid = (left + right) // 2
		while mid >= 0 and p2 > temp:
			if nums[mid] * 2 <= nums[p2]:
				mid -= 1
				p2 -= 1
				ans += 2
			else:
				mid -= 1
		return ans
## 灵神思路——二分法
class Solution2:
	def maxNumOfMarkedIndices(self, nums):
		nums.sort()
		left, right = 0, len(nums) // 2 + 1
		n = len(nums)
		while left + 1 < right:
			mid = (left + right) // 2
			# if all(nums[i] * 2 <= nums[i - mid] for i in range(mid)):
			if all(nums[i] * 2 <= nums[n - mid + i] for i in range(mid)):
				left = mid
			else:
				right = mid
		return left * 2

# 5.可移除字符的最大数目
class Solution1:
	def maximumRemovals(self, s, p, removable):
		left, right = 0, len(removable)
		n, m = len(s), len(p)
		while left + 1 < right:
			mid = (left + right) // 2
			new_removeable = removable[:mid]
			new_removeable.sort()
			p1 = p2 = p3 = 0
			while p3 < m:
				if p1 == new_removeable[p2]:
					p1 += 1
					p2 += 1
				else:
					if s[p1] == p[p3]:
						p3 += 1
					p1 += 1 
			if p3 == m:
				left = mid
			else:
				right = mid
		return left
## 优化
class Solution2:
	def check(self, s, p, removable, mid):
		set_ = set(removable[:mid])
		i = 0
		for j, c in enumerate(s):
			if j not in set_ and c == p[i]:
				i += 1
				if i == len(p):
					return True
		return False

	def maximumRemovals(self, s, p, removable):
		left, right = 0, len(removable) + 1
		while left + 1 < right:
			mid = (left + right) // 2
			if self.check(s, p, removable, mid):
				left = mid
			else:
				right = mid
		return left

# 6.有界数组中指定下标处的最大值
class Solution1:
	def check(self, n, index, maxSum, mid):
		ans = mid
		temp = mid
		for i in range(index + 1, n):
			# ans += max(temp - 1, 1)
			temp = max(temp - 1, 1)
			ans += temp
		temp = mid
		for i in range(0, index, -1):
			temp max(temp - 1, 1)
			ans += temp
		return ans <= maxSum

	def maxValue(self, n, index, maxSum):
		left, right = 1, maxSum - n + 1
		while left + 1 < right:
			mid = (left + right) // 2
			if self.check(self, n, index, maxSum, mid):
				left = mid
			else:
				right = mid
		return left
## 优化
class Solution2:
	def maxValue(self, n, index, maxSum):
		def sum(x, cnt):
			'''
			x 为数组最大值;cnt 为数组个数
			'''
			if x >= cnt:
				return (x + x - cnt + 1) * cnt // 2
			else:
				return x * (x + 1) // 2 + cnt - x
				left, right = 1, maxSum - n + 1

		left, right = 1, maxSum - n + 2
		while left + 1 < right:
			mid = (left + right) // 2
			if sum(mid - 1, index) + sum(mid, n - index) <= maxSum:
				left = mid
			else:
				right = mid
		return left

# 8.可以到达的最远建筑
class Solution1:
	def furthestBuilding(self, heights, bricks, ladders):
		def walk(mid):
			diff_lis = []
			for i in range(1, mid + 1):
				diff_lis.append(heights[i] - heights[i - 1])

			pos_lis = []
			for x in diff_lis:
				if x > 0:
					pos_lis.append(x)
			pos_lis.sort()
			if ladders > 0 and sum(pos_lis) - sum(pos_lis[-ladders:]) <= bricks:
				return True
			elif ladders == 0 and sum(pos_lis) <= bricks:
				return True
			else:
				return False

		left, right = 0, len(heights)
		while left + 1 < right:
			mid = (left + right) // 2
			if walk(mid):
				left = mid
			else:
				right = mid
		return left
# 优化
class Solution1:
	def furthestBuilding(self, heights, bricks, ladders):
		def walk(mid):
			pos_lis = []
			for i in range(1, mid + 1):
				if heights[i] - heights[i - 1] > 0:
					pos_lis.append(heights[i] - heights[i - 1])

			# pos_lis = []
			# for x in diff_lis:
			# 	if x > 0:
			# 		pos_lis.append(x)
			pos_lis.sort()
			if ladders > 0 and sum(pos_lis) - sum(pos_lis[-ladders:]) <= bricks:
				return True
			elif ladders == 0 and sum(pos_lis) <= bricks:
				return True
			else:
				return False

		left, right = 0, len(heights)
		while left + 1 < right:
			mid = (left + right) // 2
			if walk(mid):
				left = mid
			else:
				right = mid
		return left

# 9.最大合金数
class Solution1:
	def maxNumberOfAlloys(self, n, k, budget, composition, stock, cost):
		def check(mid):
			temp_min = inf
			for i in range(k):
				min_composition = - sum(a * b for a,b in zip(stock, cost))
				min_composition += sum(a * b for a,b in zip(composition[i], cost))
				temp_min = min(min_composition, temp_min)
			return temp_min <= budget

		left, right = 0, max(stock) + budget // sum(cost) + 1
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				left = mid
			else:
				right = mid
		return left 
## 灵神思路
class Solution2:
	def maxNumberOfAlloys(self, n, k, budget, composition, stock, cost):
		ans = 0
		mx = min(stock) + budget
		for comp in composition:
			def check(num):
				money = 0
				for s, base, c in zip(stock, comp, cost):
					if s < base * num:
						money += (base * num - s) * c
						if money > budget:
							return False
				return True

			left, right = ans, mx + 1
			while left + 1 < right:
				mid = (left + right) // 2
				if check(mid):
					left = mid
				else:
					right = mid
			ans = left
		return ans