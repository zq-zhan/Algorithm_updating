# 一维差分（扫描线）
# 1.拼车
## 灵神题解1:复杂度O(n+U)，U为trips长度
class Solution1:
	def carPooling(self, trips, capacity):
		d = [0] * 1001
		for num, from_, to in trips:  # trips[i]相当于把a中下标from到to-1的数都增加numPassengers
			d[from_] += num
			d[to] -= num
		return all(s <= capacity for s in accumulate(d))
## 灵神题解2:哈希表+差分
class Solution2:
	def carPooling(self, trips, capacity):
		d = Counter()
		for num, from_, to in trips:
			d[from_] += num
			d[to] -= num

		s = 0
		for k in sorted(d):
			s += d[k]
			if s > capacity:
				return False
		return True

# 2.与车相交的点
class Solution1:
	def numberOfPoints(self, nums):
		max_num = max(end for from_, end in nums)
		d = [0] * (max_num + 2)
		for from_, end in nums:
			d[from_] += 1
			d[end + 1] -= 1
		return sum(s > 0 for s in accumulate(d))

## 灵神题解
class Solution2:
	def numberOfPoints(self, nums):
		max_end = max(end for _, end in nums)
		diff = [0] * (max_end + 2)
		for start, end in nums:
			diff[start] += 1
			diff[end + 1] -= 1
		return sum(s > 0 for x in accumulate(diff))
## 方法二
class Solution3:
	def numberOfPoints(self, nums):
		d = defaultdict(int)
		for start, end in nums:
			d[start] += 1
			d[end + 1] -= 1
		ans = temp_sum = last = 0
		for k in sorted(d):
			ans += k - last if temp_sum > 0 else 0
			temp_sum += d[k]
			last = k
		return ans

# 3.检查是否区域内所有整数都被覆盖
class Solution1:
	def isCovered(self, ranges, left, right):
		# max_num = max(end for _, end in ranges)
		d = [0] * (50 + 2)
		for start, end in ranges:
			d[start] += 1
			d[end + 1] -= 1

		a = list(accumulate(d))
		return right - left + 1 == sum(x > 0 for x in a[left:right + 1])

# 4.人口最多的年份
class Solution1:
	def maximumPopulation(self, logs):
		d = [0] * (100 + 2)
		for birth, death in logs:
			d[birth - 1950 + 1] += 1
			d[death - 1950 + 1] -= 1

		ans = 2051
		temp_s = 0
		for i, s in enumerate(list(accumulate(d))):
			# temp_s += s
			if s > temp_s:
				temp_s = s
				ans = i + 1949
		return ans
## 方法二
class Solution2:
	def maximumPopulation(self, logs):
		d = defaultdict(int)
		for birth, death in logs:
			d[birth] += 1
			d[death] -= 1

		ans = 2051
		temp_s = max_s = 0
		for year, s in sorted(d.items()):
			temp_s += s
			if max_s < temp_s:
				max_s = temp_s
				ans = year
		return ans





