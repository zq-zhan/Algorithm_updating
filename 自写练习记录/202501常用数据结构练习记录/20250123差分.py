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

		# ans = 2051
		temp_s = 0
		for i, s in enumerate(list(accumulate(d))):
			# temp_s += s
			if s > temp_s:
				temp_s = s
				ans = i + 1949
		return ans

class Solution1:
	def maximumPopulation(self, logs):
		d = [0] * (100 + 1)
		for birth, death in logs:
			d[birth - 1950] += 1
			d[death - 1950] -= 1

		# ans = 2051
		temp_s = 0
		for i, s in enumerate(list(accumulate(d))):
			# temp_s += s
			if s > temp_s:
				temp_s = s
				ans = i + 1950
		return ans

## 方法二
class Solution2:
	def maximumPopulation(self, logs):
		d = defaultdict(int)
		for birth, death in logs:
			d[birth] += 1
			d[death] -= 1

		# ans = 2051
		temp_s = max_s = 0
		for year, s in sorted(d.items()):
			temp_s += s
			if max_s < temp_s:
				max_s = temp_s
				ans = year
		return ans

# 5.统计已测试设备
class Solution1:
	def countTestedDevices(self, batteryPercentages):
		ans = 0
		for i, x in enumerate(batteryPercentages):
			x -= ans
			if x > 0:
				ans += 1
		return ans

# 6.航班预订统计
class Solution1:
	def corpFlightBookings(self, booking, n):
		max_end = max(last for _, last, _ in bookings)
		d = [0] * (max_end + 1)
		for first, last, seat in booking:
			d[first] += seat
			d[last + 1] -= seat

		ans = list(accumulate(d))
		return ans

# 7.零数组变换1
class Solution1:
	def isZeroArray(self, nums, queries):
		d = [0] * (max(nums) + 1)
		for left, right in queries:
			d[left] -= 1
			d[right + 1] += 1

		diff_sum = list(accumulate(d))[:-1]
		return all(x + y <= 0 for x, y in zip(nums, diff_sum))

# 8.合并区间
class Solution1:
	def merge(self, intervals):
		intervals.sort(key = lambda x: x[0])

		ans = []
		for left, right in intervals:
			if ans and left <= ans[-1][1]:
				ans[-1][1] = max(right, ans[-1][1])
			else:
				ans.append([left, right])
		return ans

# 9.插入区间
class Solution1:
	def insert(self, intervals, newInterval):
		intervals.append(newInterval)
		intervals.sort()

		ans = []
		for left, right in intervals:
			if ans and ans[-1][1] >= left:
				ans[-1][1] = max(ans[-1][1], right)
			else:
				ans.append([left, right])
		return ans
## 一次遍历思路
class Solution2:
	def insert(self, intervals, newInterval):
		n_start, n_end = newInterval
		ans = []

		for start, end in intervals:
			if end < n_start or start > n_end:
				ans.append([start, end])
				continue
			n_start = min(n_start, start)
			n_end = max(n_end, end)
		ans.append([n_start, n_end])
		ans.sort()
		return ans

# 10.我的日程安排表3
class MyCalendarThree:
	def __init__(self):
		self.calendar = SortedDict()
		# self.new_dict = self.calendar

	def book(self, startTime, endTime):
		new_arr = self.calendar
		new_arr[startTime] = new_arr.get(startTime, 0) + 1
		new_arr[endTime] = new_arr.get(endTime, 0) - 1 

		s = ans = 0
		for v in new_arr.values():
			s += v
			ans = max(ans, s)
		return ans

# 11.将区间分为最小组数
class Solution1:
	def minGroups(self, intervals):
		max_num = max(end for _, end in intervals)
		d = [0] * (max_num + 2)
		for start, end in intervals:
			d[start] += 1
			d[end + 1] -= 1

		return max(list(accumulate(d)))

# 12. 字母移位2
class Solution1:
	def shiftingLetters(self, s, shifts):
		d = [0] * (len(s) + 1)
		for start, end, direction in shifts:
			if direction == 0:
				d[start] -= 1
				d[end + 1] += 1
			else:
				d[start] += 1
				d[end + 1] -= 1

		ans = list(accumulate(d))[:-1]
		ans_char = ''
		ord_a = ord('a')
		for i, c in enumerate(ans):
			ans_char += chr((ord(s[i]) - ord_a + c) % 26 + ord_a)
		return ans_char

# 13.K连续位的最小翻转次数
## 方法一：差分
class Solution1:
	def minKBitFlips(self, nums, k):
		n = len(nums)

		d = [0] * (n + 1)
		s = ans = 0
		for i in range(n):
			s += d[i]
			if (nums[i] + s) % 2 == 0:
				if i + k > n:
					return -1
				ans += 1
				s += 1
				d[i + k] -= 1
		return ans

###################### 二维差分 ####################
# 1.用邮票贴满网格图
## 灵神二维差分思路
class Solution1:
    def possibleToStamp(self, grid, stampHeight, stampWidth):
        m, n = len(grid), len(grid[0])

        # 1.计算grid的二维前缀和
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + v

        # 2.计算二维差分
        ## 为方便计算，在d数组的最上面和最左边各家了一行
        d = [[0] * (n + 2) for _ in range(m + 2)]
        for i2 in range(stampHeight, m + 1):
            for j2 in range(stampWidth, n + 1):
                i1 = i2 - stampHeight + 1
                j1 = j2 - stampWidth + 1
                if s[i2][j2] - s[i2][j1 - 1] - s[i1 - 1][j2] + s[i1 - 1][j1 - 1] == 0:
                    d[i1][j1] += 1
                    d[i1][j2 + 1] -= 1
                    d[i2 + 1][j1] -= 1
                    d[i2 + 1][j2 + 1] += 1

        # 3. 还原二维差分矩阵对应的计数矩阵（原地计算）
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                d[i + 1][j + 1] += d[i + 1][j] + d[i][j + 1] - d[i][j]
                if v == 0 and d[i + 1][j + 1] == 0:
                    return False
        return True

# 2.子矩阵元素加1
class Solution1:
	def rangeAddQueries(self, n, queries):
		mat = [[0] * n for _ in range(n)]

		# 1.计算二维前缀和
		# s = [[0] * (n + 1) for _ in range(n + 1)]  # 前缀和全是0

		# 2.计算二维差分
		d = [[0] * (n + 2) for _ in range(n + 2)]
		for r1, c1, r2, c2 in queries:
			# for  in querie:
			d[r1 + 1][c1 + 1] += 1
			d[r1 + 1][c2 + 2] -= 1
			d[r2 + 2][c1 + 1] -= 1
			d[r2 + 2][c2 + 2] += 1

		# 3.计算二维前缀和、还原计数矩阵
		for i in range(1, n + 1):
			for j in range(1, n + 1):
				d[i][j] += d[i][j - 1] + d[i - 1][j] - d[i - 1][j - 1]
				mat[i - 1][j - 1] = d[i][j]
		return mat
## 灵神题解
class Solution:
    def rangeAddQueries(self, n, queries):
        # 二维差分
        diff = [[0] * (n + 2) for _ in range(n + 2)]
        for r1, c1, r2, c2 in queries:
            diff[r1 + 1][c1 + 1] += 1
            diff[r1 + 1][c2 + 2] -= 1
            diff[r2 + 2][c1 + 1] -= 1
            diff[r2 + 2][c2 + 2] += 1

        # 计算 diff 的二维前缀和（原地修改）
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                diff[i][j] += diff[i][j - 1] + diff[i - 1][j] - diff[i - 1][j - 1]

        # 保留中间 n*n 的部分，即为答案
        diff = diff[1:-1]
        for i, row in enumerate(diff):
            diff[i] = row[1:-1]
        return diff
# 3.二维区域和检索——矩阵不可变
class NumMatrix:
	def __init__(self,matrix):
		m = len(matrix)
		n = len(matrix[0])

		# 1.计算二维前缀和
		# ans = 0
		s = [[0] * (n + 1) for _ in range(m + 1)]
		for i, row in enumerate(matrix):
			for j, v in enumerate(row):
				s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + v

		self.s = s
	def sumRegion(self, row1, col1, row2, col2):
		# new_arr = self.matrix
		# m = len(new_arr)
		# n = len(new_arr[0])

		# # 1.计算二维前缀和
		# # ans = 0
		# s = [[0] * (n + 1) for _ in range(m + 1)]
		# for i, row in enumerate(new_arr):
		# 	for j, v in enumerate(row):
		# 		s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + v
		s = self.s
		return s[row2 + 1][col2 + 1] - s[row2 + 1][col1] - s[row1][col2 + 1] + s[row1][col1]

