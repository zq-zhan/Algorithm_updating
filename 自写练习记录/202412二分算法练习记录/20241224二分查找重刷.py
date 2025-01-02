# 1.在排序数组中查找元素的第一个和最后一个
class Solution1:
	def searchRange(self,nums,target):
		start = bisect_left(nums,target)  # >=
		if start == len(nums) or nums[start] != target:
			return [-1, -1]
		end = bisect_right(nums, target) - 1  # <= 等价于 >x - 1

		return [start, end]
## 灵神二分模版
### 闭区间写法
class Solution:
    # lower_bound 返回最小的满足 nums[i] >= target 的下标 i
    # 如果数组为空，或者所有数都 < target，则返回 len(nums)
    # 要求 nums 是非递减的，即 nums[i] <= nums[i + 1]
    def lower_bound(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1  # 闭区间 [left, right]
        while left <= right:  # 区间不为空
            # 循环不变量：
            # nums[left-1] < target
            # nums[right+1] >= target
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1  # 范围缩小到 [left, mid-1]
            else:
                left = mid + 1  # 范围缩小到 [mid+1, right]
        # 循环结束后 left = right+1
        # 此时 nums[left-1] < target 而 nums[left] = nums[right+1] >= target
        # 所以 left 就是第一个 >= target 的元素下标
        return left

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.lower_bound(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]  # nums 中没有 target
        # 如果 start 存在，那么 end 必定存在
        end = self.lower_bound(nums, target + 1) - 1
        return [start, end]
### 开区间写法
def lower_bound(self, nums: List[int], target: int) -> int:
    left, right = -1, len(nums)  # 开区间 (left, right)
    while left + 1 < right:  # 区间不为空
        mid = (left + right) // 2
        # 循环不变量：
        # nums[left] < target
        # nums[right] >= target
        if nums[mid] >= target:
            right = mid  # 范围缩小到 (left, mid)
        else:
            left = mid  # 范围缩小到 (mid, right)
    # 循环结束后 left+1 = right
    # 此时 nums[left] < target 而 nums[right] >= target
    # 所以 right 就是第一个 >= target 的元素下标
    return right


# 2.搜索插入位置
class Solution1:
	def searchInsert(self, nums, target):
		find = bisect_right(nums, target)
		if nums[find - 1] == target:
			return find - 1
		else:
			return find
## 仔细思考: >= 的情况时，bisect_left返回的就是找到的该目标值的索引；> 的情况时，返回的就是目标不存在时应该被插入的索引
## 			而这种情况，>= 无论是否找到目标值返回的索引都可以满足（因为没找到时返回的索引就是>的索引）
class Solution2:
	def searchInsert(self, num, target):
		return bisect_left(nums, target)

# 3.二分查找
class Solution1:
	def search(self,nums,target):
		find = bisect_left(nums, target)
		if find == len(nums) or nums[find] != target:
			return -1
		return find

# 4.寻找比目标字母大的最小字母
class Solution1:
	def nextGreatestLetter(self,letters,target):
		find = bisect_right(letters, target)
		if find == len(letters):
			return letters[0]
		return letters[find]

# 5.正整数和负整数的最大计数
class Solution1:
	def maximumCount(self, nums):
		neg_find = bisect_left(nums, 0) - 1
		pos_find = bisect_right(nums, 0)
		return max(neg_find + 1, len(nums) - pos_find)

# 6.两个数组间的距离值
class Solution1:
	def findTheDistanceValue(self, arr1, arr2, d):
		arr2.sort()
		ans = 0
		for x in arr1:
			left = bisect_left(arr2, x - d)  # >= x - d 且这个数还满足 >x + d，于是arr2中[:left]小于x-d、[left:]>x+d
			if left == len(arr2) or arr2[find] > d + x :
				ans += 1
		return ans
## 开区间写法
class Solution2:
	def findTheDistanceValue(self, arr1, arr2, d):
		def lower_bound(nums, target):
			left, right = -1, len(nums)
			while left + 1 < right:  # 区间不为空
				mid = (left + right) // 2
				if nums[mid] >= target:
					right = mid
				else:
					left = mid
			return right

		arr2.sort()
		ans = 0
		for x in arr1:
			find = lower_bound(arr2,x - d)
			if find == len(arr2) or arr2[find] > x + d:
				ans += 1
		return ans

# 7.咒语和药水的成功对数
class Solution1:
	def successfulPairs(self, spells, potions, success):
		def lower_bound(nums, target):
			left, right = -1, len(nums)
			while left + 1 < right:
				mid = (left + right) // 2
				if nums[mid] >= target:
					right = mid
				else:
					left = mid
			return right
		ans = []
		potions.sort()
		for x in spells:
			find = lower_bound(potions, success/x)
			ans.append(len(potions) - find)
		return ans

# 8.和有限的最长子序列
class Solution1:
	def answerQueries(self,nums,queries):
		def lower_bound(nums, target):  # 找到>=target的最小序号
			left, right = 0, len(nums) 
			while left + 1 < right:
				mid = (left + right) // 2
				if nums[mid] >= target:
					right = mid
				else:
					left = mid
			return right
		nums.sort()
		for i in range(1, len(nums)):
			nums[i] = nums[i] + nums[i - 1]
		ans = []
		for x in queries:
			find = lower_bound(nums, x + 1) - 1
			if find == -1:
				ans.append(0)
			else:
				ans.append(find + 1)
		return ans
## 优化思路：<=x的子序列的长度等于>x的序号，故可以直接写成bisect_right(nums,x)或bisect_left(nums,x+1)
class Solution2:
	def answerQueries(self, nums, queries):
		nums.sort()
		for i in range(1,len(nums)):
			nums[i] += nums[i - 1]  # 原地求前缀和
		for i, q in enumerate(queries):
			queries[i] = bisect_left(nums, q + 1)
		return queries

# 9.比较字符串最小字母出现频次
class Solution1:
	def numSmallerByFrequency(self, queries, words):
		def f(s):
			s_set = sorted(set(s))
			s_dic = Counter(s)
			return s_dic[s_set[0]]
		def lower_bound(nums, target):
			left, right = -1, len(nums)
			while left + 1 < right:
				mid = (left + right) // 2
				if nums[mid] >= target:
					right = mid
				else:
					left = mid
			return right

		for i in range(len(words)):
			words[i] = f(words[i])

		words.sort()
		ans = []
		for x in queries:
			find = lower_bound(words, f(x) + 1)
			ans.append(len(words) - find)
		return ans

# 10.区间内查询数字的频率
class RangeFreqQuery:
	def __init__(self,arr):
		pos = defaultdict(list)
		for i in range(len(arr)):
			pos[arr[i]].append(i)
		self.pos = pos
	def query(self, left, right, value):
		nums = self.pos[value]
		lower_find = bisect_left(nums, left)  # >=left的个数为 len(nums) - left
		upper_find = bisect_right(nums, right)  # >right的个数为len(nums) - right
		# 故闭区间[left, right]的个数为 >=left的个数 - >right的个数
		return upper_find - lower_find

# 11.统计公平数对的数目
class Solution1:
	def countFairPairs(self, nums, lower, upper):
		nums.sort()
		ans = 0
		for j in range(len(nums)):
			left_find = bisect_left(nums, lower - nums[j], 0, j)  # 从[0:j]（不包含j）中找到满足>=lower-nums[j]的索引
			right_find = bisect_right(nums, upper - nums[j], 0, j)
			ans += right_find - left_find
		return ans

# 12.删除数对后的最小数组长度
class Solution1:
	def minLengthAfterRemovals(self,nums):
		# nums_dic = Counter(nums)
		n = len(nums)
		target = nums[n // 2]
		max_cnt = bisect_right(nums, target) - bisect_left(nums, target)
		return max(2 * max_cnt - n, n % 2)

# 13.基于时间的键值存储
class TimeMap:

	def __init__(self):
		pos = defaultdict(list)
		self.pos = pos
		# self.pos = defaultdict(list)


	def set(self, key: str, value: str, timestamp: int) -> None:
		pos = self.pos
		pos[key].append([timestamp,value])
		# self.pos[key].append([timestamp,value])

	def get(self, key: str, timestamp: int) -> str:
		arr = self.pos[key]
		if not arr or arr[0][0] > timestamp:
			return ''
		if arr[-1][0] <= timestamp:
			return arr[-1][1]
		nums = []
		for x in arr:
			nums.append(x[0])
		find = bisect_right(nums, timestamp) - 1
		if find == -1:
			return ''
		else:
			return arr[find][1]
		
# 14.快照数组
class SnapshotArray:
	def __init__(self, length):
		self.arr = [0] * length
		self.cnt = -1
		self.snap_arr = []
		self.nums = []
		

	def set(self, index, val):
		self.arr[index] = val

	def snap(self):
		self.cnt += 1
		self.nums.append(self.cnt)
		self.snap_arr.append(self.arr.copy())
		return self.cnt

	def get(self, index, snap_id):
		nums = self.nums
		find = bisect_left(nums, snap_id)
		if find > self.cnt:
			return ''
		else:
			return self.snap_arr[find][index]
## 灵神思路:记录添加修改的快照编号和val
class SnapshotArray:
	def __init__(self, length):
		self.cur_snap_id = 0
		self.history = defaultdict(list)  # 每个index的历史修改记录,甚至都不需要原数组，因为不存在0直接返回0

	def set(self, index, val):
		self.history[index].append((self.cur_snap_id, val))

	def snap(self):
		self.cur_snap_id += 1
		return self.cur_snap_id - 1

	def get(self, index, snap_id):
		# 找快照编号<=snap_id的最后一次修改记录
		find = bisect_left(self.history[index], (snap_id + 1,)) - 1
		if find == -1:
			return 0
		else:
			return self.history[index][find][1]

# 15.找到k格最接近的元素
## 思路：二分法+双指针
class Solution1:
	def findClosestElements(self,arr,k,x):
		find = bisect_left(arr, x)
		if find == 0:
			return arr[:k]
		elif find == len(arr):
			return arr[-k:]

		n = len(arr)
		left = find - 1
		right = find
		while right < n and left >= 0 and right - left <= k:
			left_distance = abs(arr[left] - x)
			right_distance = abs(arr[right] - x)
			if left_distance <= right_distance:
				left -= 1
			else:
				right += 1
		if right - left > k:
			return arr[left + 1:right]
		elif left == 0:
			return arr[:k]
		elif right == n:
			return arr[-k:]

class Solution:
    def findClosestElements(self, arr, k, x):
        idx = bisect_left(arr, x)
        left, right = idx - 1, idx
        res = []

        while k > 0:
            if left < 0:
                res.append(arr[right])
                right += 1
            elif right >= len(arr):
                res.append(arr[left])
                left -= 1
            else:
                if abs(arr[left] - x) <= abs(arr[right] - x):
                    res.append(arr[left])
                    left -= 1
                else:
                    res.append(arr[right])
                    right += 1
            k -= 1
        
        return sorted(res)









