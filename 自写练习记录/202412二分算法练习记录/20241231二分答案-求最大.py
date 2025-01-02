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
# 二分法
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


