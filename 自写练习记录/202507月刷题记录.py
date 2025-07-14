# 1.20250701找到初始输入字符串1
class Solution:
	def possibleStringCount(self, word):
		left = ans = 0
		word += '0'
		for right, c in enumerate(word):
			if c == word[left]:
				continue
			ans += right - left - 1
			left = right
		return ans + 1

# 2.积压订单中的订单总数
class Solution:
	def getNumberOfBacklogOrders(self, orders):
		mod = 10 ** 9 + 7
		buy_lis = []
		sell_lis = []
		for price, amount, orderType in orders:
			if orderType == 0:  # 采购订单
				while sell_lis and amount and sell_lis[0][0] <= price:
					if sell_lis[0][1] <= amount:
						amount -= sell_lis[0][1]
						heapq.heappop(sell_lis)
					else:
						sell_lis[0][1] -= amount
						amount = 0
				if amount > 0:
					heapq.heappush(buy_lis, [-price, amount])
			else:
				while buy_lis and amount and -buy_lis[0][0] >= price:
					if buy_lis[0][1] <= amount:
						amount -= buy_lis[0][1]
						heapq.heappop(buy_lis)
					else:
						buy_lis[0][1] -= amount
						amount = 0
				if amount > 0:
					heapq.heappush(sell_lis, [price, amount])
		ans = 0
		for _, amount in buy_lis:
			ans += amount
		for _, amount in sell_lis:
			ans += amount
		return ans % mod

# 3.选出和最大的k个元素
class Solution:
	def findMaxSum(self, nums1, nums2, k):
		new_arr = [(x, i) for i, x in enumerate(nums1)]
		new_arr.sort(key = lambda x:x[0])

		n = len(nums1)
		ans = []
		for i in range(0, n):
			target = nums1[i]
			target_num = []
			for x, index in new_arr:
				if x < target:
					heapq.heappush(target_num, -nums2[index])
				else:
					break
			temp_s = 0
			for _ in range(k):
				if target_num:
					temp_s += -heapq.heappop(target_num)
				else:
					break
			ans.append(temp_s)
		return ans
## 灵神题解
class Solution:
	def findMaxSum(self, nums1, nums2, k):
		new_arr = sorted((x, y, i) for i, (x, y) in enumerate(zip(nums1, nums2)))

		n = len(new_arr)
		ans = [0] * n
		temp_lis = []
		temp_s = i = 0
		while i < n:
			start = i
			target = new_arr[start][0]
			while i < n and new_arr[i][0] == target:
				ans[new_arr[i][2]] = temp_s
				i += 1
			for j in range(start, i):
				y = new_arr[j][1]
				temp_s += y
				heapq.heappush(temp_lis, y)
				if len(temp_lis) > k:
					temp_s -= heapq.heappop(temp_lis)
		return ans
class Solution:
    def findMaxSum(self, nums1, nums2, k):
        a = sorted((x, y, i) for i, (x, y) in enumerate(zip(nums1, nums2)))
        n = len(a)
        ans = [0] * n
        h = []
        s = 0
        for i, (x, y, idx) in enumerate(a):
            ans[idx] = ans[a[i - 1][2]] if i and x == a[i - 1][0] else s
            s += y
            heappush(h, y)
            if len(h) > k:
                s -= heappop(h)
        return ans

# 4.不含AAA或BBB的字符串
class Solution:
	def strWithout3a3b(self, a, b):
		ans = ''
		while a > 0 or b > 0:
			if a > b:
				if b > 0:
					ans += 'a' * min(a, 2) + 'b'
				else:
					ans += 'a' * min(a, 2)
				a -= min(a, 2)
				b -= 1
			elif a == b:
				if ans and ans[-1] == 'a':
					ans += 'b' * min(a, 2) + 'a' * min(b, 2)
				else:
					ans += 'a' * min(a, 2) + 'b' * min(b, 2)
				a -= min(a, 2)
				b -= min(b, 2)
			else:
				if a > 0:
					ans += 'b' * min(b, 2) + 'a'
				else:
					ans += 'b' * min(b, 2)
				a -= 1
				b -= min(b, 2)
		return ans

# 5.20250702找到初始输入字符串2
## 灵神题解：前缀和+多重背包（不会！）
class Solution:
	def possibleStringCount(self, word, k):

# 6.重构字符串
class Solution:
	def reorganizeString(self, s):
		n = len(s)
		s_dic = Counter(s)
		s_lis = [(cnt, x) for x, val in s_dic.items()]
		ans = ''
		while len(ans) < n:
			cnt, x = heapq.heappop(s_lis)
			ans += x
			if cnt > 0:
				heapq.heappush(s_lis, (cnt - 1, x))

# 7.丑数2
class Solution:
	def nthUglyNumber(self, n):


############### 链表 ##################
# 8.二进制链表转整数
class Solution:
	def getDecimalValue(self, head):
		ans = ''
		while head:
			ans += str(head.val)
			head = head.next
		return int(ans, 2)

# 9.找出临界点之间的最小和最大距离
class Solution:
	def nodesBetweenCriticalPoints(self, head):
		ans = []
		pre_val = head.val
		head = head.next
		index = 1
		temp_ans = inf
		while head.next:
			x = head.val
			nxt_val = head.next.val
			if (x > pre_val and x > nxt_val) or (x < pre_val and x < nxt_val):
				ans.append(index)
				if len(ans) >= 2:
					temp_ans = min(ans[-1] - ans[-2], temp_ans)
			index += 1
			head = head.next
			pre_val = x

		return [temp_ans, ans[-1] - ans[0]] if temp_ans < inf else [-1, -1]

# 10.合并零之间的节点
class Solution:
	def mergeNodes(self, head):
		ans = ListNode(0)  # 哨兵节点
		cur = ans 
		temp_s = 0
		head = head.next
		while head:
			if head.val != 0:
				temp_s += head.val
			else:
				cur.next = ListNode(temp_s)
				cur = cur.next
				temp_s = 0
			head = head.next
		return ans.next
## 灵神题解
class Solution:
	def mergeNodes(self, head):
		tail = head
		cur = head.next
		while cur.next:
			if cur.val:
				tail.val += cur.val
			else:
				tail = tail.next
				tail.val = 0
			cur = cur.next
		tail.next = None
		return head

# 11.分隔链表
class Solution:
	def splitListToParts(self, head, k):
		cur = head
		n = 0
		while cur:
			n += 1
			cur = cur.next
		ori_cnt = (n - 1) // k + 1
		target_len = []
		if n <= k:
			target_len = [1] * n + [0] * (k - n)
		else:
			for _ in range(k):
				target_len.append(ori_cnt)
				ori_cnt -= 1
			target_len[-1] += n - sum(target_len)

		ans = []
		temp_lis = []
		index = 0
		while head:
			temp_lis.append(head.val)
			if len(temp_lis) == target_len[index]:
				ans.append(temp_lis)
				temp_lis = []
				index += 1
			head = head.next
		while len(ans) < k:
			ans.append([])
		return ans

class Solution:
    def splitListToParts(self, root: ListNode, k: int):
        total_len = 0
        cur = root
        while cur:
            total_len += 1
            cur = cur.next
        length = total_len // k   # 每段的基础长度
        m = total_len % k         # 前 l 段需要在基础长度上+1

        res = []
        cur = root
        for i in range(k):
            res.append(cur)
            size = length + (1 if m > 0 else 0)   # 算出每段的长度
            if cur:   # 这里判断cur是否存在，防止cur.next不存在报错
                for j in range(size-1):
                    cur = cur.next
                m -= 1
                tmp = cur.next   # 把后面一段截掉，后面一段需在后面继续划分
                cur.next = None
                cur = tmp
        return res

# 12.20250703找出第k个字符1
class Solution:
	def kthCharacter(self, k):
		ord_a = ord('a')
		ans = 'a'
		while len(ans) < k:
			n = len(ans)
			for i in range(n):
				ans += chr((ord(ans[i]) - ord_a + 1) % 26 + ord_a)
				if len(ans) == k:
					return ans[-1]
		return ans[-1]

# 13.链表组件
class Solution:
	def numComponents(self, head, nums):
		cur = head
		while cur.next:
			cur = cur.next
		cur.next = ListNode(-1)

		left = right = ans = 0
		nums = set(nums)
		while head:
			if head.val not in nums:
				ans += 1 if left != right else 0
				left = right
			else:
				right += 1
			head = head.next
		return ans

############## 删除节点 #########
# 14.移除链表元素
class Solution:
	def removeElements(self, head, val):
		temp_node = ListNode(None)
		temp_node.next = head
		cur = temp_node
		while cur.next:
			if cur.next.val == val:
				cur.next = cur.next.next
			else:
				cur = cur.next
		return temp_node.next

# 15.从链表中移除在数组中存在的节点
class Solution:
	def modifiedList(self, nums, head):
		dummy = ListNode(next = head)
		cur = dummy
		nums = set(nums)
		while cur.next:
			if cur.next.val in nums:
				cur.next = cur.next.next
			else:
				cur = cur.next
		return dummy.next

# 16.删除排序链表中的重复元素2
class Solution:
	def deleteDuplicates(self, head):
		dummy = ListNode(next = head)
		cur = dummy
		while cur.next and cur.next.next:
			val = cur.next.val
			if cur.next.next.val == val:
				while cur.next and cur.next.val == val:
					cur.next = cur.next.next
			else:
				cur = cur.next
		return dummy.next

# 17.删除链表中的节点
class Solution:
	def deleteNode(self, node):
		node.val = node.next.val
		node.next = node.next.next

# 18.合并两个链表
class Solution:
	def mergeInBetween(self, list1, a, b, list2):
		dummy = ListNode(next = list1)
		cur = dummy
		cnt = 0
		while cnt <= b:
			if cnt == a:
				temp = cur.next
				while cnt <= b:
					temp = temp.next
					cnt += 1
				cur.next = list2
				while cur.next:
					cur = cur.next
				cur.next = temp
				break
			else:
				cur = cur.next
				cnt += 1
		return dummy.next

# 19.从链表中移除节点
class Solution:
	def removeNodes(self, head):
		head_lis = []
		cur = head
		while cur:
			head_lis.append(cur.val)
			cur = cur.next
		dummy = ListNode(None)
		mx = head_lis[-1]
		n = len(head_lis)
		ans = []
		for i in range(n - 1, -1, 0):
			if head_lis[i] >= mx:
				ans.append(head_lis[i])
				mx = max(head_lis[i], mx)
		cur = dummy
		for x in ans[::-1]:
			cur.next = ListNode(x)
			cur = cur.next
		return dummy.next

# 20.20250707最多可以参加的会议数目
class Solution:
	def maxEvents(self, events):
		events.sort(key = lambda x:x[1])
		mx = max(x for _, x in events)
		new_arr = [0] * (mx + 1)
		for start, end in events:
			new_arr[start - 1] += 1
			new_arr[end] -= 1


class Solution:
	def maxEvents(self, events):
		mx = max(x for _, x in events)
		groups = [[] for _ in range(mx + 1)]
		for e in events:
			groups[e[0]].append(e[1])
		ans = 0
		h = []
		for i, g in enumerate(groups):
			while h and h[0] < i:
				heapq.heappop(h)
			for end_day in g:
				heapq.heappush(h, end_day)
			if h:
				ans += 1
				heapq.heappop(h)
		return ans

# 21.对链表进行插入排序
class Solution:
	def insertionSortList(self, head):
		dummy = ListNode(next = head)
		left = dummy
		right = left.next
		while right.next:
			if right.next.val < right.val:
				temp = right.next.next
				cur = left.next
				left.next = right.next
				left.next.next = cur
				right.next = temp
		return dummy.next
## 灵神题解
class Solution:
	def insertionSortList(self, head):
		dummy = ListNode(0)
		cur = head
		while cur:
			next_node = cur.next
			pre = dummy
			while pre.next and pre.next.val < cur.val:
				pre = pre.next
			cur.next = pre.next
			pre.next = cur
			cur = next_node
		return dummy.next

# 22.反转链表
class Solution:
	def reverseList(self, head):
		pre = None
		cur = head
		while cur:
			nxt = cur.next
			cur.next = pre
			pre = cur
			cur = nxt
		return pre

# 23.反转链表2
class Solution:
	def reverseBetween(self, head, left, right):
		dummy = ListNode(next = head)
		p0 = dummy
		for _ in range(left - 1):
			p0 = p0.next

		cur = p0.next
		pre = None
		for _ in range(right - left + 1):
			nxt = cur.next
			cur.next = pre
			pre = cur
			cur = nxt

		p0.next.next = cur
		p0.next = pre
		return dummy.next

# 24.两两交换链表中的节点
class Solution:
	def swapPairs(self, head):
		dummy = ListNode(next = head)
		p0 = dummy
		pre = None
		cur = p0.next
		while cur and cur.next:
			for _ in range(2):
				nxt = cur.next
				cur.next = pre
				pre = cur
				cur = nxt
			nxt = p0.next
			p0.next.next = cur
			p0.next = pre
			p0 = nxt
		return dummy.next

# 25.k个一组翻转链表
class Solution:
	def reverseKGroup(self, head, k):
		n = 0
		cur = head
		while cur:
			cur = cur.next
			n += 1

		dummy = ListNode(next = head)
		pre = None
		p0 = dummy
		cur = p0.next
		while n >= k:
			n -= k
			for _ in range(k):
				nxt = cur.next
				cur.next = pre
				pre = cur
				cur = nxt
			nxt = p0.next
			p0.next.next = cur
			p0.next = pre
			p0 = nxt
			# if n < k:
			# 	break
		return dummy.next

# 26.反转偶数长度组的节点
class Solution:
	def reverseEvenLengthGroups(self, head):
		n = 0
		cur = head
		while cur:
			cur = cur.next
			n += 1

		k = 1
		p0 = dummy = ListNode(next = head)
		pre = p0
		cur = p0.next
		while n > 0:
			target = min(n, k)
			n -= k
			k += 1
			if target % 2:
				for _ in range(target):
					cur = cur.next
					p0 = p0.next
			else:
				for _ in range(target):
					nxt = cur.next
					cur.next = pre
					pre = cur
					cur = nxt
				nxt = p0.next
				p0.next.next = cur
				p0.next = pre
				p0 = nxt
		return dummy.next

# 27.删除链表的倒数第N个结点
class Solution:
	def removeNthFromEnd(self, head, n):
		dummy = ListNode(next = head)
		right = dummy
		for _ in range(n):
			right = right.next

		left = dummy
		while right.next:
			left = left.next
			right = right.next
		left.next = left.next.next
		return dummy.next

# 28.重新安排会议得到最多空余时间1
## 灵神题解——转换为滑动窗口题目，合并至多连续k + 1个空闲时间段时得到的结果最大
class Solution:
	def maxFreeTime(self, eventTime, k, startTime, endTime):
		n = len(startTime)
		free = [0] * (n + 1)
		free[0] = startTime[0]  # 最左边的空余时间段
		for i in range(1, n):
			free[i] = startTime[i] - endTime[i - 1]
		free[n] = eventTime - endTime[-1]

		ans = s = 0
		for i, f in enumerate(free):
			s += f
			if i < k:
				continue
			ans = max(ans, s)
			s -= free[i - k]
		return ans

# 29.旋转链表
class Solution:
	def rotateRight(self, head, k):
		n = 0
		cur = head
		while cur:
			n += 1
			cur = cur.next

		p0 = dummy = ListNode(next = head)
		pre = None
		for _ in range(k):
			right = p0
			while right.next.next:
				right = right.next
			
			nxt = p0.next
			p0.next = right.next
			p0.next.next = nxt
			right.next = None
		return dummy.next
## 题解：题意等价于将链表后k % n个节点移到链表最前面
class Solution:
	def rotateRight(self, head, k):
		n = 0
		cur = head
		while cur:
			n += 1
			cur = cur.next
		if n == 0:
			return head

		k = k % n
		p0 = dummy = ListNode(next = head)
		right = dummy
		for _ in range(n - k):
			right = right.next

		nxt = p0.next
		p0.next = right.next
		while p0.next:
			p0 = p0.next
		p0.next = nxt
		right.next = None
		return dummy.next
## 前后指针解法
class Solution:
	def rotateRight(self, head, k):
		if not head or not head.next:
			return head
		n = 0
		cur = head
		while cur:
			n += 1
			cur = cur.next

		k = k % n
		if k == 0:
			return head

		p0 = dummy = ListNode(next = head)
		right = dummy
		for _ in range(k):
			right = right.next
		left = dummy
		while right.next:
			left = left.next
			right = right.next

		nxt = p0.next
		p0.next = left.next
		right.next = nxt
		left.next = None
		return dummy.next

# 30.交换链表中的节点
class Solution:
	def swapNodes(self, head, k):
		dummy = ListNode(next = head)
		right = dummy
		for _ in range(k):
			right = right.next
		temp_node = right
		left = dummy
		while right.next:
			right = right.next
			left = left.next
		temp_node.val, left.next.val = left.next.val, temp_node.val
		return dummy.next

# 31.20250710重新安排会议得到最多空余时间2
## 灵神题解——转换为滑动窗口题目，合并至多连续k + 1个空闲时间段时得到的结果最大
class Solution:
	def maxFreeTime(self, eventTime, startTime, endTime):
		n = len(startTime)
		free = [0] * (n + 1)
		free[0] = startTime[0]  # 最左边的空余时间段
		for i in range(1, n):
			free[i] = startTime[i] - endTime[i - 1]
		free[n] = eventTime - endTime[-1]

		ans = s = 0
		for i, f in enumerate(free):
			s += f
			if i < 1:
				continue
			ans = max(ans, s)
			s -= free[i - 1]
		return ans

########### 快慢指针 ########
# 32.链表的中间节点
class Solution:
	def middleNode(self, head):
		slow = head
		fast = head
		while fast or fast.next:
			slow = slow.next
			fast = fast.next
		return slow

# 33.删除链表的中间节点
class Solution:
	def deleteMiddle(self, head):
		dummy = ListNode(next = head)
		slow = dummy
		fast = dummy.next
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
		slow.next = slow.next.next
		return dummy.next

# 34.回文链表
## 灵神题解——快慢指针+反转链表
class Solution:
	def isPalindrome(self, head):
		dummy = ListNode(next = head)
		slow = dummy
		fast = dummy.next
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
		pre = None
		cur = slow.next
		while cur:
			nxt = cur.next
			cur.next = pre
			pre = cur
			cur = nxt
		# slow.next = None
		cur = dummy.next
		while cur and pre:
			if cur.val != pre.val:
				return False
			cur = cur.next
			pre = pre.next
		return True

# 35.链表最大孪生和
class Solution:
	def pairSum(self, head):
		dummy = ListNode(next = head)
		slow = dummy
		fast = dummy.next
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next

		pre = None
		cur = slow.next
		while cur:
			nxt = cur.next
			cur.next = pre
			pre = cur
			cur = nxt

		ans = 0
		cur = dummy.next
		while pre:
			ans = max(ans, pre.val + cur.val)
			cur = cur.next
			pre = pre.next
		return ans

# 36.重排链表
class Solution:
	def reorderList(self, head):
		dummy = ListNode(next = head)
		slow = dummy.next
		fast = dummy.next
		p0 = head
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next

		pre = None
		cur = slow
		while cur:
			nxt = cur.next
			cur.next = pre
			pre = cur
			cur = nxt
		# slow.next = pre
		
		while pre.next:
			nxt = p0.next
			nxt2 = pre.next
			p0.next = pre
			p0.next.next = nxt
			p0 = nxt
			pre = nxt2


# 37.20250711无需开会的工作日
class Solution:  # 前缀和求解超时 O(n + d)，当d远大于n时会超时，本题days就是10^9，而meetings的长度是10^5
	def countDays(self, days, meetings):
		pre_lis = [0] * (days + 1)
		for start, end in meetings:
			pre_lis[start - 1] += 1
			pre_lis[end] -= 1

		new_arr = list(accumulate(pre_lis))
		return days - sum(x > 0 for x in new_arr)

class Solution:  
	def countDays(self, days, meetings):
		meetings.sort(key = lambda x:x[0])
		start, end = 1, 0
		for s, e in meetings:
			if s > end:
				days -= end - start + 1
				start = s
			end = max(end, e)
		days -= end - satrt + 1
		return days

class Solution:  # O(nlogn)
	def countDays(self, days, meetings):
		new_arr = [[1, 0]]
		meetings.sort(key = lambda x:x[0])
		ans = 0
		n = len(meetings)
		for i in range(n):
			ans += max(0, meetings[i][0] - new_arr[-1][1] - 1)
			if meetings[i][0] <= new_arr[-1][1] + 1:
				new_arr[-1][1] = max(meetings[i][1], new_arr[-1][1])
			else:
				new_arr.append(meetings[i])
		ans += max(0, days - new_arr[-1][1])
		return ans
	
# 38.环形链表
class Solution:
	def hasCycle(self, head):
		slow = head
		fast = head
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
			if slow is fast:
				return True
		return False

# 39.环形链表2
class Solution:
	def detectCycle(self, head):
		slow = head
		fast = head    
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
			if slow is fast:
				while slow is not head:
					slow = slow.next
					head = head.next
				return slow
		return None

# 40.环形数组是否存在循环
class Solution:
	def circularArrayLoop(self, nums):

# 41.奇偶链表
class Solution:
	def oddEvenList(self, head):
		if not head:
			return head
		cur1 = head
		cur2 = head.next
		p0 = head.next
		while cur1.next and cur2.next:
			nxt = cur2.next
			cur1.next = nxt
			cur2.next = nxt.next
			cur1 = nxt
			cur2 = nxt.next
		cur1.next = p0
		return head

# 42.分隔链表
class Solution:
	def partition(self, head, x):
		p1 = cur1 = ListNode(0)
		p2 = cur2 = ListNode(1)
		while head.next:
			if head.val < x:
				cur1.next = head
				cur1 = cur1.next
			else:
				cur2.next = head
				cur2 = cur2.next
			head = head.next
		cur2.next = None
		cur1.next = p2.next
		return p1.next

# 43.相交链表
## 灵神题解——在相交节点状态找到符合的条件
class Solution:
	def getIntersectionNode(self, headA, headB):
		p1, p2 = headA, headB
		while p1 is not p2:
			p1 = p1.next if p1 else headB
			p2 = p2.next if p2 else headA
		return p1


############################ 二叉树 ###########################
# 44. 二叉树的前序遍历
class Solution:  # 根-左-右
	def preorderTraversal(self, root):
		ans = []
		def dfs(root):
			if not root:
				return
			nonlocal ans
			ans.append(root.val)
			dfs(root.left)
			dfs(root.right)
		dfs(root)
		return ans

# 45.二叉树的中序遍历
class Solution:  # 左-根-右
	def inorderTraversal(self, root):
		ans = []
		def dfs(root):
			if not root:
				return 
			dfs(root.left)
			ans.append(root.val)
			dfs(root.right)
		dfs(root)
		return ans

# 46.二叉树的后序遍历
class Solution:  # 左-右-根
	def postorderTraversal(self, root):
		ans = []
		def dfs(root):
			if not root:
				return 
			dfs(root.left)
			dfs(root.right)
			nonlocal ans
			ans.append(root.val)
		dfs(root)
		return ans

# 47.叶子相似的树
class Solution:
	def leafSimilar(self, root1, root2):
		ans1 = []
		ans2 = []
		def dfs(root, ans):
			if not root:
				return 
			if root.left is None and root.right is None:
				ans.append(root.val)
			dfs(root.left, ans)
			dfs(root.right, ans)
		dfs(root1, ans1)
		dfs(root2, ans2)
		return ans1 == ans2
# 48.运动员和训练师的最大匹配数
class Solution:
	def matchPlayersAndTrainers(self, players, trainers):
		players.sort()
		trainers.sort()
		p1 = p2 = 0
		ans = 0
		n, m = len(players), len(trainers):
		while p1 < n and p2 < m:
			if players[p1] <= trainers[p2]:
				ans += 1
				p1 += 1
				p2 += 1
			else:
				p2 += 1
		return ans

# 49.开幕式焰火
class Solution:
	def numColor(self, root):
		temp_set = set()
		def dfs(root):
			if not root:
				return 
			nonlocal temp_set
			temp_set.add(root.val)
			dfs(root.left)
			dfs(root.right)
		dfs(root)
		return len(temp_set)

# 50.左叶子之和
class Solution:
	def sumOfLeftLeaves(self, root):
		ans = 0
		def dfs(root, tag):
			if not root:
				return 
			if root.left is None and root.right is None and tag == 'left':
				nonlocal ans
				ans += root.val
			dfs(root.left, 'left')
			dfs(root.right, 'right')
		dfs(root, 'right')
		return ans

# 51.二叉树中第二小的节点
class Solution:
	def findSecondMinimumValue(self, root):
		ans = []
		def dfs(root):
			if not root:
				return 
			if len(ans) < 2 and (not ans or root.val != ans[-1]):
				ans.append(root.val)
			elif ans[-1] > root.val and ans[0] != root.val:
				ans[-1] = root.val
			dfs(root.left)
			dfs(root.right)
		dfs(root)
		return ans[-1] if len(ans) == 2 else -1
## 更简单直接的做法——第一个root.val一定是最小的，所以等价于找大于root.val的最小值
class Solution:
	def findSecondMinimumValue(self, root):
		ans = inf
		def dfs(node):
			if not node:
				return 
			if node.val > root.val:
				nonlocal ans
				ans = min(ans, node.val)
			dfs(node.left)
			dfs(node.right)
		dfs(root)
		return ans if ans < inf else -1 

# 52.二叉树的最大深度
## 自顶向下遍历
class Solution:
	def maxDepth(self, root):
		ans = 0
		def dfs(root, length):
			if not root:
				return 
			length += 1
			nonlocal ans
			ans = max(ans, length)
			dfs(root.left, length)
			dfs(root.right, length)
		dfs(root, 0)
		return ans
## 自底向上遍历
class Solution:
	def maxDepth(self, root):
		if not root:
			return 0
		l_maxdepth = self.maxDepth(root.left)
		r_maxdepth = self.maxDepth(root.right)
		return max(l_maxdepth, r_maxdepth) + 1

# 53.路径总和
class Solution:
	def hasPathSum(self, root, target):
		ans = False
		def dfs(root, temp_s):
			if not root:
				return
			temp_s += root.val
			if not root.left and not root.right:
				nonlocal ans
				ans |= (temp_s == target)
			dfs(root.left, temp_s)
			dfs(root.right, temp_s)
		dfs(root, 0)
		return ans
## 自底向上遍历
class Solution:
	def hasPathSum(self, root, target):
		if not root:
			return False
		if not root.left and not root.right:
			return target == root.val
		l_sum = self.hasPathSum(root.left, target - root.val)
		r_sum = self.hasPathSum(root.right, target - root.val)
		return l_sum | r_sum

# 54.求根节点到叶节点数字之和
class Solution:
	def sumNumbers(self, root):
		ans = 0
		def dfs(root, temp_s):
			if not root:
				return 
			temp_s = temp_s * 10 + root.val
			if not root.right and not root.left:
				nonlocal ans
				ans += temp_s
			dfs(root.left, temp_s)
			dfs(root.right, temp_s)
		dfs(root, 0)
		return ans
## 自底向上遍历
class Solution:
	def sumNumbers(self, root, x = 0):
		if not root:
			return 0
		x = x * 10 + root.val
		if not root.left and not root.right:
			return x
		return self.sumNumbers(root.left, x) + self.sumNumbers(root.right, x)

# 55.二叉树的右视图
class Solution:
	def rightSideView(self, root):
		ans = []
		def dfs(root, depth):
			if not root:
				return 
			if depth == len(ans):
				ans.append(root.val)
			dfs(root.right, depth + 1)
			dfs(root.left, depth + 1)
		dfs(root, 0)
		return ans

# 56.统计二叉树中好节点的数目
class Solution:
	def goodNodes(self, root):
		ans = 0
		def dfs(root, temp_mx):
			if not root:
				return 
			nonlocal ans
			ans += int(root.val >= temp_mx)
			temp_mx = max(temp_mx, root.val)
			dfs(root.left, temp_mx)
			dfs(root.right, temp_mx)
		dfs(root, -inf)
		return ans
## 自底向上
class Solution:
	def goodNodes(self, root, temp_mx):
		if not root:
			return 0
		if root.val >= temp_mx:
			return self.goodNodes(root.left, root.val) + self.goodNodes(root.right, root.val) + 1
		else:
			return self.goodNodes(root.left, temp_mx) + self.goodNodes(root.right, temp_mx)
class Solution:
	def goodNodes(self, root, temp_mx = - inf):
		if not root:
			return 0
		left = self.goodNodes(root.left, max(temp_mx, root.val))
		right = self.goodNodes(root.right, max(temp_mx, root.val))
		return left + right + (temp_mx <= root.val)

# 57.二叉树中的伪回文路径
class Solution:
	def pseudoPalindromicPaths(self, root):
		ans = 0
		def dfs(root, temp_dic):
			nonlocal ans
			if not root:
				return
			temp_dic[root.val] += 1
			if not root.left and not root.right:
				cnt = 0
				for key, val in temp_dic.items():
					if val % 2:
						cnt += 1
					if cnt > 1:
						break
				ans += (cnt <= 1)
			dfs(root.left, temp_dic)
			dfs(root.right, temp_dic)
			temp_dic[root.val] -= 1
		dfs(root, defaultdict(int))
		return ans

# 58.祖父节点值为偶数的节点和
class Solution:
	def sumEvenGrandparent(self, root):
		ans = 0
		def dfs(root, parent_val, grandparent_val):
			nonlocal ans
			if not root:
				return
			if grandparent_val % 2 == 0:
				ans += root.val
			dfs(root.left, root.val, parent_val)
			dfs(root.right, root.val, parent_val)
		dfs(root, -1, -1)
		return ans			

# 59.二进制链表转整数
class Solution:
	def getDecimalValue(self, head):
		ans = ''
		# cur = head
		while head:
			ans += str(head.val)
			head = head.next
		return int(ans, 2)
