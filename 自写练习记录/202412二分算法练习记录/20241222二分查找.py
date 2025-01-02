# 1.在排序数组中查找元素的第一个和最后一个位置
class Solution1:
	def searchRange(self,nums,target):
		def lower_bound(nums,target):
			left = 0
			right = len(nums) - 1
			while left <= right:
				mid = (left + right) // 2
				if nums[mid] < target:
					left = mid + 1
				else:
					right = mid - 1
			return left
		start = lower_bound(nums,target)
		if start == len(nums) or nums[start] != target:
			return [-1,-1]
		end = lower_bound(nums,target + 1) - 1
		return [start,end]

# 2.搜索插入位置
class Solution1:
	def searchInsert(self,nums,target):
		def lower_bound(nums,target):
			left = 0
			right = len(nums) - 1
			while left <= right:
				mid = (left + right) // 2
				if nums[mid] < target:
					left = mid + 1
				else:
					right = mid - 1
			return left
		ans = lower_bound(nums,target)
		return ans

# 3.二分查找
class Solution1:
	def search(self,nums,target):
		def lower_bound(nums,target):
			left = 0
			right = len(nums) - 1
			while left <= right:
				mid = (left + right) // 2
				if nums[mid] < target:
					left = mid + 1
				else:
					right = mid - 1
			return left
		ans = lower_bound(nums,target)
		if ans == len(nums) or nums[ans] != target:
			return -1
		else:
			return ans

# 4.寻找比目标字母大的最小字母
class Solution1:
	def nextGreatestLetter(self,letter,target):
		def lower_bound(letter,target):
			left = 0
			right = len(letter) - 1
			while left <= right:
				mid = (left + right) // 2
				if letter[mid] < target:
					left = mid + 1
				else:
					right = mid - 1
			return left
		ans = lower_bound(letter,chr(ord(target) + 1))
		if ans == len(letter):
			return letter[0]
		else:
			return letter[ans]

# 5.正整数和负整数的最大计数
class Solution1:
	def maximumCount(self,nums):
		def lower_bound(nums,target):
			left, right = 0, len(nums) - 1
			while left <= right:
				mid = (left + right) // 2
				if nums[mid] < target:
					left = mid + 1
				else:
					right = mid - 1
			return left
		end = lower_bound(nums,1) # >= 1
		start = lower_bound(nums,0) - 1 # <= -1
		return max(start + 1, len(nums) - end)

# 6.两个数组间的距离值
class Solution1:
	def findTheDistanceValue(self,arr1,arr2,d):
		def lower_bound(nums,target):
			left = 0
			right = len(nums) - 1
			while left <= right:
				mid = (left + right) // 2
				if nums[mid] < target:
					left = mid + 1
				else:
					right = mid - 1
			return left
		ans = 0
		for x in arr1:
			new_arr = []
			new_arr = [-abs(x - y) for y in arr2]
			new_arr.sort()
			find = lower_bound(new_arr,-d)
			if find == len(new_arr):
				ans += 1
			else:
				continue
		return ans
## 二分优化：
class Solution2:
	def findTheDistanceValue(self,arr1,arr2,d):
		arr2.sort()
		ans = 0
		for x in arr1:
			find = bisect_left(arr2,x - d)
			if find == len(arr2) or arr2[find] > d + x:
				ans += 1
		return ans


## 方法二：双指针
class Solution3:
	def findTheDistanceValue(self,arr1,arr2,d):
		arr1.sort()
		arr2.sort()
		ans = 0
		p1 = p2 = 0
		n, m = len(arr1), len(arr2)
		while p1 < n:
			while p2 < m:
				if arr1[p1] - arr2[p2] > d:
					p2 += 1
				elif arr1[p1] - arr2[p2] < -d:
					ans += 1
					break
				else:
					break
			if p2 == m:
				ans += n - p1
				break
			p1 += 1
		return ans

# 7.咒语和药水的成功对数
class Solution1:
	def successfulPairs(self,spells,potions,success):
		ans = []
		potions.sort()
		for x in spells:
			find = bisect_left(potions, success/x)
			if find == len(potions):
				ans.append(0)
			else:
				ans.append(len(potions) - find)
		return ans

# 8.和有限的最长子序列
class Solution1:
	def answerQueries(self,nums,queries):
		ans = []
		new_arr = [0] * len(nums)
		nums.sort()
		for i,x in enumerate(nums):
			if i == 0:
				new_arr[i] = nums[i]
			else:
				new_arr[i] = nums[i] + new_arr[i - 1]
		for i in range(len(queries)):
			find = bisect_left(new_arr,queries[i] + 1) - 1
			if find == len(new_arr) - 1:
				ans.append(0)
			else:
				ans.append(find + 1)
		return ans
## 灵神思路
class Solution2:
	def answerQueries(self, nums, queries):
		nums.sort()
		for i in range(1,len(nums)):
			nums[i] += nums[i - 1]  # 原地求前缀和
		for i, q in enumerate(queries):
			queries[i] = bisect_right(nums, q)
		return queries

# 9.比较字符串最小字母出现频次
class Solution1:
	def numSmallerByFrequency(self,queries,words):
		def f(s):
			s_set = set(s).sort()
			s_dic = Counter(s)
			return s_dic[s_set[0]]
		ans = []
		for i, c in enumerate(words):
			words[i] = f(c)
		words.sort() 
		for x in queries:
			find = bisect_left(words, f(x) + 1)
			ans.append(len(words) - find)
		return ans

# 10.区间内查询数字的频率
## 灵神思路
class RangeFreqQuery:
	def __init__(self,arr):
		pos = defaultdict(list)
		for i, x in enumerate(arr):
			pos[x].append(i)  # 保存目标值的下标
		self.pos = pos
	def query(self,left,right,value):
		a = self.pos[value]
		left_bound = bisect_left(a, left)
		right_bound = bisect_left(a, right)  #不存在时，right_cound-1也不一定就是==right
		return right_bound - left_bound + 1
class RangeFreqQuery:
	def __init__(self,arr):
		pos = defaultdict(list)
		for i, x in enumerate(arr):
			pos[x].append(i)  # 保存目标值的下标
		self.pos = pos
	def query(self,left,right,value):
		a = self.pos[value]
		left_bound = bisect_left(a, left)
		right_bound = bisect_left(a, right + 1)  #>=闭区间要写成这样！！
		return right_bound - left_bound

class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        pos = defaultdict(list)
        for i, x in enumerate(arr):
            pos[x].append(i)
        self.pos = pos

    def query(self, left: int, right: int, value: int) -> int:
        a = self.pos[value]
        return bisect_right(a, right) - bisect_left(a, left)

# 11.统计公平数对的数目
class Solution1:
	def countFairPairs(self,nums,lower,upper):
		nums.sort()
		ans = 0
		for i,c in enumerate(nums):
			find_right = bisect_right(nums,upper - c, 0, j) - 1
			find_left = bisect_left(nums, lower - c, 0, j)
			ans += find_right - find_left - 1 + 1
		return ans

# 12.删除数对后的最小数组长度
## 灵神思路
class Solution1:
	def minLengthAfterRemovals(self,nums):
		n = len(nums)
		mid = nums[n // 2]
		max_cnt = bisect_right(nums,mid) - bisect_left(nums,mid)
		return max(max_cnt * 2 - n, n % 2)
## 中位数思路
class Solution2:
	def minLengthAfterRemovals(self,nums):



