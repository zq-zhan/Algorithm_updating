# 1.最后一块石头的重量
class Solution1:
	def lastStoneWeight(self, nums):
		nums.sort()
		while len(nums) > 1:
			y = nums.pop()
			x = nums.pop()
			if x == y:
				continue
			else:
				nums.append(y - x)
				nums.sort()
		return 0 if not nums else nums[-1]
## python最小堆：堆顶元素是最小的
class Solution2:
	def lastStoneWeight(self, stones):
		heap = [-stone for stone in stones]
		heapq.heapify(heap)

		while len(heap) > 1:
			x, y = heapq.heappop(heap), heapq.heappop(heap)
			if x != y:
				heapq.heappush(heap, x - y)  # 堆：删除和添加一个元素的时间复杂度都是O(logn)

		if heap:
			return -heap[0]
		else:
			return 0
## 最大堆手写实现
class Heap:
	def __init__(self, desc = False):
		self.heap = []
		self.desc = desc

	def size(self):
		return len(self.heap)

	def top(self):
		''' 返回堆顶元素 '''
		if self.size:
			return self.heap[0]
		return None

	def push(self, item):
		''' 
		添加元素 
		step1:元素添加到数组末尾
		step2:将末尾元素向上调整
		'''
		self.heap.append(item)
		self._shift_up(self.size - 1)

	def pop(self):
		'''
		弹出堆顶
		step1：记录堆顶元素的值
		step2：交换堆顶元素与末尾元素
		step3：删除数组末尾元素
		step4：新的堆顶元素乡下调整
		step5：返回答案
		'''
		item = self.heap[0]
		self._swap(0, self.size - 1)
		self.heap.pop()
		self._shift_down(0)
		return item

	def _smaller(self, lhs, rhs):
		return lhs > rhs if self.desc else lhs < rhs

	def _shift_up(self, index):
		'''
		向上调整
		若父节点和当前节点满足交换关系，则持续将当前节点向上调整
		（对小顶堆父节点元素更小，对大顶堆父节点元素更大）
		'''
		while index:
			parent = (index - 1) // 2
			if self._smaller(self.heap[parent], self.heap[index]):
				break
			self._swap(parent, index)
			index = parent

	def _shift_down(self, index):
		'''
		向下调整
		若子节点和当前节点满足交换关系，则持续将当前节点向下调整
		（对小顶堆子节点元素更大，对大顶堆子节点元素更小）
		'''
		while index * 2 + 1 < self.size:  # 存在子节点
			smallest = index
			left = index * 2 + 1
			right = index * 2 + 2
			if self._smaller(self.heap[left], self.heap[smallest]):
				smallest = left
			if right < self.size and self._smaller(self.heap[right], self.heap[smallest]):
				smallest = right
			if smallest == index:
				break
			self._swap(index, smallest)
			index = smallest

	def _swap(self, i, j):
		self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 初始化大顶堆
        heap = Heap(desc=True)
        for stone in stones:
            heap.push(stone)

        # 模拟
        while heap.size > 1:
            x,y = heap.pop(),heap.pop()
            if x != y:
                heap.push(x-y)
        if heap.size: return heap.heap[0]
        return 0

# 2.k次乘运算后的最终数组1
class Solution1:  # 错解
	def getFinalState(self, nums, k, multiplier):
		heapq.heapify(nums)
		while k > 0:
			x = heapq[0]
			heapq.heappop(nums)
			heapq.heappush(nums, x * multiplier)
			k -= 1
		return nums
##
class Solution2:
	def getFinalState(self, nums, k, multiplier):
		pq = [(x, i) for i, x in enumerate(nums)]
		heapq.heapify(pq)
		for _ in range(k):
			_, i = heapq.heappop(pq)
			nums[i] *= multiplier
			heapq.heappush(pq, (nums[i], i))
		return nums

class Solution:
    def getFinalState(self, nums, k, multiplier):
        for t in range(k):
            m = nums[0]
            index = 0
            for i in range(1, len(nums)):
                if nums[i] < m:
                    m, index = nums[i], i
            nums[index] *= multiplier
        return nums

##
class Solution3:
	def getFinalState(self, nums, k, multiplier):
		pq = [(x, i) for i, x in enumerate(nums)]
		heapq.heapify(pq)
		for _ in range(k):
			_, i = heapq.heappop(pq)  # 存储最小值的索引
			nums[i] *= multiplier
			heapq.heappush(pq, (nums[i], i))  # 将变换后的x根据其索引放回堆中
		return nums

## 最后一块石头的重量
class Solution1:
	def lastStoneWeight(self, stones):
		stones = [-x for x in stones]
		heapq.heapify(stones)
		while len(stones) > 1:
			x = heapq.heappop(stones)
			y = heapq.heappop(stones)
			if x == y:
				continue
			else:
				heapq.heappush(stones, x - y)
		if stones:
			return -stones[-1]
		return 0
# 按递增顺序显示卡牌
class Solution1:
	def deckRevealedIncreasing(self, nums):
		nums.sort()
		index_lis = deque(range(len(nums)))

		ans = [0] * len(nums)
		for x in nums:
			ans[index_lis.popleft()] = x
			if index_lis:
				index_lis.append(index_lis.popleft())
		return ans

# 3.从数量最多的堆取走礼物
class Solution1:
	def pickGifts(self, gifts, k):
		ans = sum(gifts)
		gifts = [-x for x in gifts]
		heapq.heapify(gifts)
		# ans = sum(gifts)
		for i in range(k):
			push_gift = heapq.heappop(gifts)
			sqrt_push = int(sqrt(-push_gift))
			heapq.heappush(gifts, -sqrt_push)
			ans -= -push_gift - sqrt_push
		return ans

# 4.无限集中的最小数字
class SmallestInfiniteSet:  # 堆解法
	def __init__(self):
		self.heap_lis = [i + 1 for i in range(1000)]  # list(range(1, 1001))
		heapq.heapify(self.heap_lis)

	def popSmallest(self):
		return heapq.heappop(self.heap_lis)

	def addBack(self, num):
		if num not in self.heap_lis:
			heapq.heappush(self.heap_lis, num)
## 有序集合做法
class SmallestInfiniteSet:
	def __init__(self):
		self.s = SortedSet(range(1, 1001))

	def popSmallest(self):
		x = self.s[0]
		self.s.remove(x)
		return x

	def addBack(self, num):
		self.s.add(num)

# 5.执行k次操作后的最大分数
class Solution1:
	def maxKelements(self, nums, k):
		nums = [-x for x in nums]
		heapq.heapify(nums)
		ans = 0
		for _ in range(k):
			pop_num = heapq.heappop(nums)
			ans += -pop_num
			heapq.heappush(nums, pop_num // 3 - 1)
		return ans

# 6.移除石子使总数最小
class Solution1:
	def minStoneSum(self, piles, k):
		piles = [-x for x in piles]
		heapq.heapify(piles)
		for _ in range(k):
			heapq.heapreplace(piles, piles[0] + (-piles[0]) // 2)
		return -sum(piles)
## 灵神思路
class Solution2:
	def minStoneSum(self, piles, k):
		piles = [-x for x in piles]
		heapq.heapify(piles)
		for _ in range(k):
			heapq.heapreplace(piles, piles[0] // 2)  # 负数向下取整等于正数向上取整
		return -sum(piles)

# 7.数据流中的第K大元素
class KthLargest:
	def __init__(self, k, nums):
		self.nums = [-x for x in nums]
		self.k = k

	def add(self, val):
		self.nums.append(-val)
		temp_heap = self.nums.copy()
		heapq.heapify(temp_heap)
		# heapq.heappush(temp_heap, -val)
		for _ in range(self.k - 1):
			heapq.heappop(temp_heap)
		return heapq.heappop(temp_heap)
## 优化
class KthLargest:
	def __init__(self, k, nums):
		self.nums = nums
		self.k = k
		heapq.heapify(self.nums)

	def add(self, val):
		heapq.heappush(self.nums, val)
		while len(self.nums) > self.k:
			heapq.heappop(self.nums)
		return self.nums[0]

# 8.不含AAA或BBB的字符串
class Solution1:
	def strWithout3a3b(self, a, b):
		ans = ''
		while a > 0 or b > 0:
			if a == b:
				ans += 'ab'
				a -= 1
				b -= 1
			elif a > b and b > 0:
				ans += 'aab'
				a -= 2
				b -= 1
			elif a < b and a > 0:
				ans += 'bba'
				a -= 1
				b -= 2
			elif a == 0:
				ans += 'b' * b
				b = 0
			elif b == 0:
				ans += 'a' * a
				a = 0
		return ans
##
class Solution2:
    def strWithout3a3b(self, A, B):
        if A == B:
            return "ab" * A

        ans = ""

        la = A
        lb = B

        while la > 0 and lb > 0:
            if la > lb:
                ans += "aab"
                la -= 2
                lb -= 1
            elif la < lb:
                ans += "bba"
                la -= 1
                lb -= 2
            else:
                if A > B:
                    ans += "ab" * la
                else:
                    ans += "ba" * la
                la = 0
                lb = 0
        if A > B:
            ans += "a" * la + "b" * lb
        else:
            ans += "b" * lb + "a" * la

        return ans


# 9.重构字符串
## 灵神解法：O(n + |sigma|)
class Solution1:
	def reorganizeString(self, s):
		s_dic = Counter(s)
		n = len(s)
		ch, m = s_dic.most_common(1)[0]  # 获取最常出现的字符及其次数
		if m > n - m + 1:
			return ''

		ans = [''] * n
		i = m * 2
		ans[:i:2] = [ch] * m
		del s_dic[ch]

		for ch, cnt in s_dic.items():
			for _ in range(cnt):
				if i >= n:
					i = 1  
				ans[i] = ch
				i += 2
		return ''.join(ans)



# 10.距离相等的条形码
class Solution1:
	def rearrangeBarcodes(self, barcodes):
		n = len(barcodes)
		bar_dict = Counter(barcodes)
		ch, m = bar_dict.most_common(1)[0]
		ans = [0] * n

		i = m * 2
		ans[:i:2] = [ch] * m
		del bar_dict[ch]
		for ch, cnt in bar_dict.items():
			for _ in range(cnt):
				if i > n:
					i = 1
				ans[i] = ch
				i += 2
		return ans
##
class Solution2:
	def rearrangeBarcodes(self, barcodes):
		n = len(barcodes)
		bar_dict = Counter(barcodes).most_common()  # O(n + klogk)
		if bar_dict[0][1] > (n - 1) // 2 + 1:
			return ''

		ans = [0] * n
		idx = 0
		for ch, cnt in bar_dict: # O(k)
			for _ in range(cnt):
				ans[idx] = ch
				idx += 2
				if idx >= n:
					idx = 1
		return ans

# 11.你可以工作的最大周数
class Solution1:  # 错解
	def numberOfWeeks(self, milestones):
		n = sum(milestones)
		temp_dict = defaultdict()
		# max_char = max_cnt = 
		for i, x in enumerate(milestones):  # O(k)
			temp_dict[i] = x

		ans_lis = [0] * n
		idx = 0
		for ch, cnt in temp_dict.items():
			for _ in range(cnt):
				ans_lis[idx] = ch
				idx += 2
				if idx >= n:
					idx = 1
					break
		ans = 1
		for i in range(1, n):
			if ans_lis[i] == ans_lis[i - 1]:
				break
			ans += 1
		return ans
## 灵神题解
class Solution1:
	def numberOfWeeks(self, milestones):
		n = sum(milestones)
		m = max(milestones)
		return (n - m) * 2 + 1 if  m > n - m + 1 else n


# 12.最长快乐字符串
## 参考解法
class Solution1:
	def longestDiverseString(self, a, b, c):
		ans = ''
		temp_dic = {'a':a, 'b':b, 'c':c}
		while True:
			# 动态获取当前剩余字符里三个字符
			less, mid, most = sorted(temp_dic.keys(), key = lambda x:temp_dic[x])
			if (len(ans) < 2 or not ans[-2] == ans[-1] == most) and temp_dic[most] > 0:
				ans += most
				temp_dic[most] -= 1
			elif (len(ans) >= 2 and not ans[-2] == ans[-1] == mid) and temp_dic[mid] > 0:
				ans += mid
				temp_dic[mid] -= 1
			else:
				return ans
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
        题目要求：给定固定数量的字母a,b,c，返回一个尽可能长的字符串s，s满足最多有a个字母'a'、b个字母'b'、c个字母'c'且
                不含有任何'aaa''bbb'或'ccc' 这样的子串
        :param a: 给定字母a的数量
        :param b: 给定字母b的数量
        :param c: 给定字母c的数量
        :return: 返回满足要求的最长字符串
        """
        # 解题思路：题目本质很容易理解，仅使用不超过给定数量的字母a,b,c，构造出不能连续三个相同字母的字符串
        # 尽可能长，不能想到采用贪心策略，每次尽可能优先使用当前数量最多的字母，因为最后同一种字母剩余的越多，越容易出现字母连续相同的情况
        # 如果不满足条件，再使用剩余数量次多的字母，由于只有三种字母，实际上每次只会在数量最多和次多的字母中选择一个
        # 如果尝试所有的字母都无法使用，则直接结束，此时构成的字符串即为所求
        count = {'a': a, 'b': b, 'c': c}  # 初始化三种字母的数量
        res = ''  # 返回的结果字符串
        while True:
            _, mid, most = sorted(count.keys(), key=lambda x: count[x])  # 按照剩余数量排序，取出最多和次多的字母
            # 当最多的字母还有时，且结果字符串长度小于2或者最后两个字符不全为most，均可使用most
            if (len(res) < 2 or not res[-2] == res[-1] == most) and count[most]:
                res += most  # 接在结果后面
                count[most] -= 1  # 数量减一
            elif count[mid]:  # 否则使用次多的字母mid(进入这个elif,意味着结尾两个字符必然为most,故只需要mid字符还有就可以用)
                res += mid  # 接在结果后面
                count[mid] -= 1  # 数量减一
            else:  # 没有字母可以用了，结束
                break
        return res

# 13.丑数2
## 参考题解
class Solution1:
	def nthUglyNumber(self, n):
		res, a, b, c = [1] * n, 0, 0, 0
		for i in range(1, n):
			n2, n3, n5 = res[a] * 2, res[b] * 3, res[c] * 5
			res[i] = min(n2, n3, n5)
			if res[i] == n2: a += 1
			if res[i] == n3: b += 1
			if res[i] == n5: c += 1
		return res[-1]

# 14.第K近障碍物查询
class Solution1:
	def resultsArray(self, queries, k):
		nums = []
		ans = []
		heapq.heapify(nums)
		for i, querie in enumerate(queries):
			heapq.heappush(nums, abs(querie[0]) + abs(querie[1]))
			if i >= k - 1:
				if i == k - 1:
					for _ in range(k - 1):
						heapq.heappop(nums)
				ans.append(nums[0])
			else:
				ans.append(-1)

		return ans
## 灵神题解：第k小——最大堆
class Solution2:
	def resultsArray(self, queries, k):
		ans = [-1] * len(queries)
		# heapq.heapify(ans)
		h = []
		for i, (x, y) in enumerate(queries):
			heapq.heappush(h, -abs(x) - abs(y))
			if len(h) > k:
				heapq.heappop(h)
			if len(h) == k:
				ans[i] = -h[0]
		return ans





