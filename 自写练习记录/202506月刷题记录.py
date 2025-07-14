# 1.可行数组的数目
class Solution:
	def longestPalindromicSubsequence(self, original, bounds):


#################### 栈复习 #################
# 2.简化路径
class Solution:
	def simplifyPath(self, path):
		path += '/'
		ans = []
		temp_s = ''
		for x in path:
			temp_s += x
			if temp_s == './':
				temp_s = ''
				continue
			elif temp_s == '../':
				if ans[-1] != '/':
					ans.pop()
				temp_s = ''
			elif x == '/': 
				if not ans or temp_s != '/':
					ans.append(temp_s)
				temp_s = ''
		ans = ''.join(ans)
		return ans[:-1] if len(ans) > 1 else ans
## 灵神题解
class Solution:
	def simplifyPath(self, path):
		stk = []
		for s in path.split('/'):
			if s == '' or s == '.':
				continue
			if s != '..':
				stk.append(s)
			elif stk:
				stk.pop()
		return '/' + '/'.join(stk)

# 3.删除星号以后字典序最小的字符串
class Solution:
	def clearStars(self, s):
		ord_a = ord('a')
		ans = []
		ori_lis = [[] for i in range(26)]
		for i, x in enumerate(s):
			if x == '*':
				for stk in ori_lis:
					if stk:
						stk.pop()
						break
			else:
				ori_lis[ord(x) - ord_a].append(i)
		for i, stk in enumerate(ori_lis):
			temp_chr = chr(i + ord_a)
			for j in stk:
				ans.append((j, temp_chr))
		ans.sort(key = lambda x:x[0])
		result = [x[1] for x in ans]
		return ''.join(result)
## 灵神题解优化：
class Solution:
	def clearStars(self, s):
		ord_a = ord('a')
		ans = list(s)
		ori_lis = [[] for i in range(26)]
		for i, x in enumerate(s):
			if x == '*':
				for stk in ori_lis:
					if stk:
						ans[stk.pop()] = '*'
						break
			else:
				ori_lis[ord(x) - ord_a].append(i)
		return ''.join(x for x in s if x != '*')

# 4.最小栈
class MinStack:

	def __init__(self):
		self.stk = []
		self.stk_dic = defaultdict(int)

	def push(self, val):
		self.stk.append(val)
		self.stk_dic[val] += 1
	

	def pop(self):
		pop_val = self.stk.pop()
		if self.stk_dic[pop_val] == 1:
			del self.stk_dic[pop_val]
		else:
			self.stk_dic[pop_val] -= 1
	
	def top(self):
		return self.stk[-1]
	
	def getMin(self):
		return min(self.stk_dic.keys())
## 灵神题解——栈底元素维护前缀最小值
class MinStack:

	def __init__(self):
		self.stk = [(0, inf)]

	def push(self, val):
		self.stk.append((val, min(self.stk[-1][1], val)))
	

	def pop(self):
		self.stk.pop()
	
	def top(self):
		return self.stk[-1][0]
	
	def getMin(self):
		return self.stk[-1][1]

# 5.设计一个支持增量操作的栈
class CustomStack:

	def __init__(self, maxSize):
		self.stk = []
		self.maxSize = maxSize

	def push(self, x):
		if len(self.stk) < self.maxSize:
			self.stk.append(x)


	def pop(self):
		return self.stk.pop() if self.stk else -1

	def increment(self, k, val):
		for i in range(min(k, len(self.stk))):
			self.stk[i] += val

# 6.函数的独占时间
class Solution:
	def exclusiveTime(self, n, logs):
		logs = [list(info.split(':')) for info in logs]
		cur_time = 0
		result = [0] * n
		st = []
		for id, tag, time in logs:
			id = int(id)
			time = int(time)
			if tag == 'end':
				st.pop()
				time += 1
				result[id] += time - cur_time
			else:
				if st:
					cur_id = st[-1]
					result[cur_id] += time - cur_time
				st.append(id)
			cur_time = time
		return result

# 7.有序数组的平方
class Solution:  # 错解，这个单调性是错的
	def sortedSquares(self, nums):
		n = len(nums)
		left, right = 0, n - 1
		while left <= right:
			if nums[left] ** 2 < nums[right] ** 2:
				nums[right] = nums[right] ** 2
				right -= 1
			else:
				temp = nums[left]
				nums[left] = nums[right]
				nums[right] = temp ** 2
				right -= 1
		return nums

# 8.使用机器人打印字典序最小的字符串
## 灵神题解——后缀最小值
class Solution:
	def robotWithString(self, s):
		n = len(s)
		suf_min = ['z'] * (n + 1)
		for i in range(n - 1, -1, -1):
			suf_min[i] = min(suf_min[i + 1], s[i])

		ans = []
		st = []
		for i, ch in enumerate(s):
			st.append(ch)
			while st and st[-1] <= suf_min[i + 1]:
				ans.append(st.pop())
		return ''.join(ans)

###### 队列 ##########
# 9.最近的请求次数
class RecentCounter:

	def __init__(self):
		self.queue = deque()
	
	def ping(self, t):
		while self.queue and self.queue[0] < t - 3000:
			self.queue.popleft()
		self.queue.append(t)
		return len(self.queue)

# 10.按递增顺序显示卡牌
# 按递增顺序显示卡牌
class Solution:
	def deckRevealedIncreasing(self, nums):
		nums.sort()
		index_lis = deque(range(len(nums)))

		ans = [0] * len(nums)
		for x in nums:
			ans[index_lis.popleft()] = x
			if index_lis:
				index_lis.append(index_lis.popleft())
		return ans

############ 堆 ############
# 11.最后一块石头的重量
class Solution:
	def lastStoneWeight(self, nums):
		nums = [-x for x in nums]
		heapq.heapify(nums)
		while len(nums) > 1:
			y = heapq.heappop(nums)
			x = heapq.heappop(nums)
			if y != x:
				heapq.heappush(nums, y - x)
		# return -heapq.heappop(nums) if nums else 0
		return -nums[-1] if nums else 0

# 12.20250630最长和谐子序列
class Solution:
	def findLHS(self, nums):
		nums.sort()
		left = ans = 0 
		for right, x in enumerate(nums):
			while left <= right and x - nums[left] > 1:
				left += 1
			if x - nums[left] == 1:
				ans = max(ans, right - left + 1)
		return ans
## 优化——空间换时间
class Solution:
	def findLHS(self, nums):
		dic_win = Counter(nums)
		ans = 0
		for x, c in dic_win.items():
			if dic_win[x + 1]:
				ans = max(ans, c + dic_win[x + 1])
		return ans

# 13.k次乘运算后的最终数组1
class Solution:
	def getFinalState(self, nums, k, multiplier):
		# nums = [(x, i) for i, x in enumerate(nums)]
		# heapq.heapify(nums)
		# while k > 0:
		# 	mn, i = heapq.heappop(nums)
		# 	heapq.heappush(nums, (mn * multiplier, i))
		# 	k -= 1
		# ans = sorted(nums, key = lambda x:x[1])
		# return [x for x in ans]
		pq = [(x, i) for i, x in enumerate(nums)]
		heapq.heapify(pq)
		for _ in range(k):
			mn, i = heapq.heappop(pq)
			nums[i] *= multiplier
			heapq.heappush(pq, (nums[i], i))
		return nums

# 14.从数量最多的堆取走礼物
class Solution:
	def pickGifts(self, gifts, k):
		gifts = [-x for x in gifts]
		heapq.heapify(gifts)
		for _ in range(k):
			mn = heapq.heappop(gifts)
			heapq.heappush(gifts, -isqrt(-mn))
		return -sum(gifts)

# 15.第k近障碍物查询
class Solution:
	def resultsArray(self, queries, k):
		result = []
		new_arr = []
		heapq.heapify(new_arr)
		for x, y in queries:
			heapq.heappush(new_arr, -(abs(x) + abs(y)))
			while len(new_arr) > k:
				heapq.heappop(new_arr)
			if len(new_arr) < k:
				result.append(-1)
			else:
				result.append(-new_arr[0])
		return result

# 16.座位预约管理系统
class SeatManager:

	def __init__(self, n):
		self.pq = [1]
		# heapq.heapify(self.pq)  # 有序数组无需堆化

	def reserve(self):
		x = heapq.heappop(self.pq)
		if not self.pq:
			heapq.heappush(self.pq, x + 1)
		return x

	def unreserve(self, seatNumber):
		heapq.heappush(self.pq, seatNumber)

# 17.将数组和减半的最少操作次数
class Solution:
	def halveArray(self, nums):
		nums = [-x for x in nums]
		heapq.heapify(nums)
		target_half = sum(nums) / 2
		temp_s = ans = 0
		while temp_s > target_half:
			x = heapq.heappop(nums)
			heapq.heappush(nums, x / 2)
			temp_s += x
			ans += 1
		return ans

# 18.k次增加后的最大乘积
class Solution:
	def maximumProduct(self, nums, k):
		mod = 10 ** 9 + 7
		ans = 1
		heapq.heapify(nums)
		for _ in range(k):
			# x = heapq.heappop(nums)
			# heapq.heappush(nums, x + 1)
			heapq.heapreplace(nums, nums[0] + 1)
		for x in nums:
			ans = (ans * x) % mod
		return ans % mod

# 19.最小未被占据椅子的编号
class Solution:
	def smallestChair(self, times, targetFriend):
		times = [(x, y, i) for i, (x, y) in enumerate(times)]
		heapq.heapify(times)
		pre_end = []
		# heapq.heapify(pre_end)
		ans = [0] 
		while times[0][2] != targetFriend:
			_, end, _ = heapq.heappop(times)
			index = heapq.heappop(ans)
			heapq.heappush(pre_end, (end, index))
			if not ans:
				heapq.heappush(ans, index + 1)
			while pre_end and pre_end[0][0] <= times[0][0]:
				heapq.heappush(ans, heapq.heappop(pre_end)[1])
		return ans[0]



