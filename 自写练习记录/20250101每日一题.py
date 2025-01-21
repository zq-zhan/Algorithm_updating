# 1、将日期转换为二进制表示
class Solution1:
	def convertDateToBinary(self, date):
		a_lis = date.split('-')
		for i in range(len(a_lis)):
			a_lis[i] = bin(a_lis[i])[2:]
		return '-'.join(a_lis)

# 2、我的日程安排表1
class MyCalendar:
	def __init__(self):
		self.caledar_dic = []

	def book(self, startTime, endTime):
		if len(self.caledar_dic) == 0:
			self.caledar_dic.append([startTime, endTime])
			return True
		caledar_dic = self.caledar_dic
		caledar_dic.sort(key = lambda x: x[0])
		for i in range(len(caledar_dic)):
			if caledar_dic[i][1] <= startTime:
				if i == len(caledar_dic) - 1:
					self.caledar_dic.append([startTime, endTime])
					return True
				continue
			else:
				if caledar_dic[i][0] >= endTime:
					self.caledar_dic.append([startTime, endTime])
					return True
				else:
					return False
## 二分法
class MyCalendar2:
	def __init__(self):
		self.calendar = []

	def book(self, start, end):
		left, right = -1, len(self.calendar)
		while left + 1 < right:
			mid = (left + right) // 2
			s, e = self.calendar[mid]
			if end <= s:
				right = mid
			elif start >= e:
				left = mid
			elif s < end and e > start:
				return False
		self.calendar.insert(left, (start, end))
		self.calendar.sort(key = lambda x: x[0])
		return True


# 3.我的日程安排表2
## 方法一：差分
from sortedcontainers import SortedDict

class MyCalendarTwo:

    def __init__(self):
        self.sd = SortedDict()

    def book(self, startTime: int, endTime: int) -> bool:
        self.sd[startTime] = self.sd.get(startTime, 0) + 1
        self.sd[endTime] = self.sd.get(endTime, 0) - 1
        s = 0
        for v in self.sd.values():
            s += v
            if s > 2:
                self.sd[startTime] -= 1
                self.sd[endTime] += 1
                return False
        return True

# 4.我的日程安排表3
class MyCalendarThree:
	def __init__(self):
		self.calendar = SortedDict()

	def book(self, startTime, endTime):
		self.calendar[startTime] = self.calendar.get(startTime, 0) + 1
		self.calendar[endTime] = self.calendar.get(endTime, 0) - 1
		s = 0
		ans = 0
		for v in self.caledar.values():
			s += v
			ans = max(ans, s)
		return ans

# 5.不含特殊楼层的最大连续楼层数
class Solution1:
	def maxConsecutive(self, bottom, top, special):
		new_arr = [bottom - 1] + special + [top + 1]
		new_arr.sort()
		ans = 0
		for i in range(1, len(new_arr)):
			ans = max(ans, new_arr[i] - new_arr[i - 1] - 1)
		return ans

# 6.按键变更的次数
class Solution1:
	def countKeyChanges(self, s):
		ans = 0
		n = len(s)
		for i in range(1, n):
			if s[i].lower() == s[i - 1].lower():
				continue
			ans += 1
		return ans

# 7.字符串中最大的3位相同数字
class Solution1:
	def largestGoodInteger(self, nums):
		ans = ''
		for i in range(2, len(nums)):
			if nums[i] == nums[i - 1] == nums[i - 2]:
				if nums[i] > ans:
					ans = nums[i]
		return ans * 3
## 灵神优化
class Solution2:
	def largestGoodInteger(self, nums):
		mx = ''
		cnt = 1
		for i in range(1, len(nums)):
			if nums[i] != nums[i - 1]:
				cnt = 1
				continue
			cnt += 1
			if cnt == 3 and nums[i] > mx:
				mx = nums[i]
		return mx * 3

# 8.统计重新排列后包含另一个字符串的子字符串数目1
class Solution1:
	def validSubstringCount(self, word1, word2):
		word2_dic = Counter(word2)
		# word2_dic_copy = word2_dic.copy()
		left = right = 0
		n = len(word1)
		ans = 0
		while right < n and left < n:
			if word1[right] in word2:
				word2_dic[word1[right]] -= 1
				# right += 1
			while max(word2_dic.values()) <= 0:
				ans += n - right
				word2_dic[word1[left]] += 1 if word1[left] in word2 else 0
				left += 1
			right += 0 if max(word2_dic.values()) <= 0 else 1
		return ans

# 20250111——求出数字答案
class Solution1:
	def generateKey(self, nums1, nums2, nums3):
		nums1 = str(nums1)
		nums2 = str(nums2)
		nums3 = str(nums3)
		nums1 = (4 - len(nums1)) * '0' + nums1
		nums2 = (4 - len(nums2)) * '0' + nums2
		nums3 = (4 - len(nums3)) * '0' + nums3
		ans = '0'
		for i in range(4):
			char = min(nums1[i], nums2[i], nums3[i])
			if i == 0 and char > '0':
				ans += char
			elif i > 0:
				ans += char
		return ans[1:] if len(ans) > 1 else ans
## 字符串解法
class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        num1, num2, num3 = str(num1), str(num2), str(num3)
        num1 ="0"*(4-len(num1))+num1
        num2 = "0"*(4-len(num2))+num2
        num3 = "0"*(4-len(num3))+num3

        ans = []
        for i in range(4):
            ans.append(str(min(int(num1[i]), int(num2[i]), int(num3[i]))))
        return int("".join(ans))
## 灵神题解
class Solution:
    def generateKey(self, x, y, z):
        ans = 0
        pow10 = 1
        while x and y and z:
            ans += min(x % 10, y % 10, z % 10) * pow10
            x //= 10
            y //= 10
            z //= 10
            pow10 *= 10
        return ans

# 20250112——按位与结果大于零的最长组合
class Solution1:
	def largestCombination(self, candidates):
		ans = 1
		left = 0
		n = len(candidates)
		
		while left < n:
			right = left + 1
			temp_result = candidates[left]
			temp_ans = 1
			while right < n:
				if temp_result & candidates[right] > 0:
					temp_ans += 1
				right += 1
			ans = max(ans, temp_ans)
		return ans
## 灵神思路：枚举比特位
class Solution2:
	def largestCombination(self, candidates):
		m = max(candidates).bit_length()
		return max(sum(x >> i & 1 for x in candidates) for i in range(m))

# 20250113——分割数组的方案数
class Solution1:
	def waysToSplitArray(self, nums):
		# cum_sum_1 = []
		ans = 0
		temp_sum = 0
		nums_sum = sum(nums)
		for i in range(len(nums) - 1):
			temp_sum += nums[i]
			if temp_sum >= nums_sum - temp_sum:
				ans += 1
		return ans
# 20250114——超过阈值的最少操作次数1
class Solution1:  # 复杂度：nlogn
	def minOperations(self, nums, k):
		nums.sort()
		ans = 0
		for x in nums:
			if x < k:
				ans += 1
			else:
				break
		return ans
## 灵神题解:复杂度：n
class Solution2:
	def minOperations(self, nums, k):
		return sum(x < k for x in nums)

# 20250115——超过阈值的最少操作数2(最小堆模拟)
class Solution1:
	def minOperations(self, nums, k):
		nums.sort()
		new_arr = nums.copy()
		ans = 0
		while min(new_arr.values()) < k:
			new_arr.append(new_arr[0] * 2 + new_arr[1])
			new_arr = new_arr[2:]
			new_arr.sort()
			ans += 1
		return ans
class Solution2:
	def minOperations(self, nums, k):
		nums.sort()
		ans = 0
		n = len(nums)
		left = 2
		while min(nums) < k:
			temp = nums[ans] * 2 + nums[ans + 1]
			nums[ans] = inf
			while left < n and nums[left] <= temp:
				nums[left - 1] = nums[left]
				left += 1
			nums[left - 1] = temp
			ans += 1
		return ans

# 20250116——或值至少k的最短子数组1
class Solution1:
	def minimumSubarrayLength(self, nums, k):
		ans = len(nums) + 1
		left = 0
		temp = []
		temp_ori = 0
		for right, c in enumerate(nums):
			temp.append(c)
			for x in temp:
				temp_ori != x 
			while temp_ori >= k:
				ans = min(ans, right - left + 1)
				temp = temp[1:]
				left += 1
		return ans
## 灵神题解
class Solution2:
	def minimumSubarrayLength(self, nums, k):
		ans = inf
		left = bottom = right_or = 0
		for right, x in enumerate(nums):
			right_or |= x
			while left <= right and nums[left] | right_or >= k:
				ans = min(ans, right - left + 1)
				left += 1
				if bottom < left:
					# 构建一个栈
					for i in range(right - 1, left - 1, -1):
						nums[i] |= nums[i + 1]
					bottom = right
					right_or = 0
		return ans if ans < inf else -1

# 20250118求出数组中的最大序列值（不会！）
class Solution1:
	def maxValue(self, nums, k):


# 20250120找到最接近0的数字
class Solution1:
	def findClosestNumber(self, nums):
		ans = inf
		temp_dis = inf
		for x in nums:
			if temp_dis > abs(x) or (temp_dis == abs(x) and x > ans):
				temp_dis = abs(x)
				ans = x
		return ans




