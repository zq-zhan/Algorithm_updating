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

# 60.从叶节点开始的最小字符串
class Solution:
	def smallestFromLeaf(self, root):
		ans = 'z' * 8500
		ord_a = ord('a')
		def dfs(root, temp_str):
			nonlocal ans
			if not root:
				return 
			temp_str = chr(root.val + ord_a) + temp_str
			if not root.left and not root.right:
				if temp_str < ans:
					ans = temp_str
			dfs(root.left, temp_str)
			dfs(root.right, temp_str)
		dfs(root, '')
		return ans

# 61.节点与其祖先之间的最大差值
class Solution:
	def maxAncestorDiff(self, root):
		ans = 0
		def dfs(root, mx_pre, mn_pre):
			nonlocal ans
			if not root:
				return 
			ans = max(ans, abs(root.val - mx_pre), abs(root.val - mn_pre))
			mx_pre = max(mx_pre, root.val)
			mn_pre = min(mn_pre, root.val)
			dfs(root.left, mx_pre, mn_pre)
			dfs(root.right, mx_pre, mn_pre)
		dfs(root, root.val, root.val)
		return ans
## 自底向上写法——错解法
class Solution:
	def maxAncestorDiff(self, root, ans=0, mx_pre=root.val, mn_pre=root.val):
		if not root:
			return ans
		ans = max(ans, abs(ans - mx_pre), abs(ans - mn_pre))
		mx_pre = max(mx_pre, root.val)
		mn_pre = min(mn_pre, root.val)
		left = self.maxAncestorDiff(root.left, ans, mx_pre, mn_pre)
		right = self.maxAncestorDiff(root.right, ans, mx_pre, mn_pre)
		return max(left, right)
## 自底向上——归
class Solution:
	def maxAncestorDiff(self, root):
		ans = 0
		def dfs(node):
			if not node:
				return inf, -inf
			l_mn, l_mx = dfs(node.left)
			r_mn, r_mx = dfs(node.right)
			mn = min(node.val, l_mn, r_mn)
			mx = max(node.val, l_mx, r_mx)
			nonlocal ans
			ans = max(ans, node.val - mn, mx - node.val)
			return mn, mx
		dfs(root)
		return ans


# 62.从根到叶的二进制数之和
class Solution:
	def sumRootToLeaf(self, root):
		ans = 0
		def dfs(root, temp_str):
			nonlocal ans
			if not root:
				return
			temp_str += str(root.val)
			if not root.left and not root.right:
				ans += int(temp_str, 2)
			dfs(root.left, temp_str)
			dfs(root.right, temp_str)
		dfs(root, '')
		return ans

################### 自底向上dfs ###################
# 63.平衡二叉树
class Solution:
	def isBalanced(self, root):
		def get_height(node):
			if not node:
				return 0
			left_height = get_height(node.left)
			if left_height == -1:
				return -1
			right_height = get_height(node.right)
			if right_height == -1 or abs(left_height - right_height) > 1:
				return -1
			return max(left_height, right_height) + 1
		return get_height(root) != -1

# 64.二叉树的最大深度
class Solution:
	def maxDepth(self, root):
		if not root:
			return 0
		return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# 65.二叉树的最小深度
## 灵神题解-自底向上遍历
class Solution:
	def minDepth(self, root):
		if not root:
			return 0
		elif not root.left and not root.right:  # 与最大深度不同，必须要求叶节点
			return 1

		l_depth = self.minDepth(root.left) if root.left else inf
		r_depth = self.minDepth(root.right) if root.right else inf
		return min(l_depth, r_depth) + 1
## 自顶向下遍历
class Solution:
	def minDepth(self, root):
		ans = inf
		def dfs(root, depth):
			nonlocal ans
			if not root:
				return 
			depth += 1
			if depth >= ans:
				return 
			if not root.left and not root.right:
				ans = min(ans, depth)
				return 
			dfs(root.left, depth)
			dfs(root.right, depth)
		dfs(root, 0)
		return ans if root else 0

# 66.20250715有效单词
class Solution:
	def isValid(self, word):
		cnt1 = cnt2 = 0   # 记录元音字母个数
		if len(word) < 3:
			return False
		for x in word:
			if not x.isdigit() and not x.isalpha():
				return False
			if x.isalpha():
				if x in 'aeiouAEIOU':
					cnt1 += 1
				else:
					cnt2 += 1
		return True if cnt1 > 0 and cnt2 > 0 else False
## 灵神题解——巧妙用元音和辅音的判断
class Solution:
	def isValid(self, word):
		if len(word) < 3:
			return False
		f = [False] * 2
		for c in word:
			if c.isalpha():
				f[c.lower() in "aeiou"] = True
			elif not c.isdigit():
				return False
		return all(f)

# 67.单值二叉树
class Solution:
	def isUnivalTree(self, root, set_lis = set()):
		if not root:
			return len(set_lis) == 1
		if len(set_lis) > 1:
			return False
		set_lis.add(root.val)
		left = self.isUnivalTree(root.left, set_lis)
		right = self.isUnivalTree(root.right, set_lis)
		return left and right
class Solution:
	def isUnivalTree(self, root, dic_win = defaultdict(int)):
		if not root:
			return len(dic_win) == 1
		if len(dic_win) > 1:
			return False
		dic_win[root.val] += 1
		left = self.isUnivalTree(root.left, dic_win)
		right = self.isUnivalTree(root.right, dic_win)
		if dic_win[root.val] == 1:
			del dic_win[root.val]
		else:
			dic_win[root.val] += 1
		return left and right
class Solution:
	def isUnivalTree(self, root):
		v = root.val
		def dfs(node):
			return not node or (node.val == v and dfs(node.left) and dfs(node.right))
		return dfs(root)
class Solution:
	def isUnivalTree(self, root):
		if not root:
			return True
		if root.left and root.left.val != root.val:
			return False
		if root.right and root.right.val != root.val:
			return False
		return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
## 自顶向下
class Solution:
	def isUnivalTree(self, root):
		ans_set = set()
		def dfs(root):
			if not root:
				return
			ans_set.add(root.val)
			dfs(root.left)
			dfs(root.right)
		dfs(root)
		return len(ans_set) <= 1

# 68.相同的树
class Solution:
	def isSameTree(self, p, q):
		if not p and not q:
			return True
		elif (not p and q) or (p and not q) or (p.val != q.val):
			return False
		left = self.isSameTree(p.left, q.left)
		right = self.isSameTree(p.right, q.right)
		return left and right
## 灵神题解——简洁
class Solution:
	def isSameTree(self, p, q):
		if not p or not q:
			return p is q  # 都得是None
		return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# 69.对称二叉树
class Solution:
	def isSameTree(self, p, q):
		if not p or not q:
			return p is q  # 都得是None
		return p.val == q.val and self.isSameTree(p.left, q.right) and self.isSameTree(p.right, q.left)

	def isSymmetric(self, root):
		return self.isSameTree(root.left, root.right)


# 70.找出有效子序列的最大长度1
class Solution:
	def maximumLength(self, nums):
		ans = 0
		n = len(nums)
		def dfs(i, pre_num):
			if nums[i]

# 71.翻转等价二叉树
class Solution:
	def maximumLength(self, root1, root2):
		if not root1 or not root2:
			return root1 is root2
		if root1.val == root2.val:
			return (self.maximumLength(root1.left, root2.left) and self.maximumLength(root1.right, root2.right)) \
			or (self.maximumLength(root1.left, root2.right) and self.maximumLength(root1.right, root2.left))
		else:
			return False
		return self.maximumLength(root1, root2)

# 72.找出克隆二叉树中的相同节点
class Solution:
	def getTargetCopy(self, original, cloned, target):
		ans = ''
		def dfs(cloned):
			if not cloned:
				return
			elif cloned.val == target.val:
				nonlocal ans
				ans = cloned
				return
			dfs(cloned.left)
			dfs(cloned.right)
		dfs(cloned)
		return ans
## 灵神题解
class Solution:
	def getTargetCopy(self, original, cloned, target):
		if original is None or original is target:
			return cloned
		return self.getTargetCopy(original.left, cloned.left, target) or \
			self.getTargetCopy(original.right, cloned.right, target)

# 73.平衡二叉树
## 后序遍历+剪枝
class Solution:
	def isBalanced(self, root):
		def get_height(node):
			if not node:
				return 0
			left_height = get_height(node.left)
			if left_height == -1:
				return -1
			right_height = get_height(node.right)
			if right_height == -1 or abs(left_height - right_height) > 1:
				return -1
			return max(left_height, right_height) + 1
		return get_height(root) != 1
## 先序遍历+判断深度
class Solution:
	def isBalanced(self, root):
		if not root:
			return True
		return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and \
			self.isBalanced(root.left) and self.isBalanced(root.right)

	def depth(self, root):
		if not root:
			return 0
		return max(self.depth(root.left), self.depth(root.right)) + 1

# 74.翻转二叉树
class Solution:
	def invertTree(self, root):
		if not root:
			return root
		def chans(node1, node2):
			if not node1 or not node2:
				return
			node1.val, node2.val = node2.val, node1.val
			chans(node1.left, node2.left)
			chans(node1.right, node2.right)
		chans(root.left, root.right)
		return root

class Solution:
	def invertTree(self, root):
		if not root:
			return root

		def chans(node):
			if not node:
				return 
			node.left.val, node.right.val = node.right.val, node.left.val
## 灵神题解
### 自底向上
class Solution:
	def invertTree(self, root):
		if not root:
			return None
		left = self.invertTree(root.left)
		right = self.isUnivalTree(root.right)
		root.left = right
		root.right = left
		return root
### 自上向下
class Solution:
	def invertTree(self, root):
		if not root:
			return None
		root.left, root.right = root.right, root.left
		self.invertTree(root.left)
		self.invertTree(root.right)
		return root

# 75.合并二叉树
class Solution:
	def mergeTrees(self, root1, root2):
		if not root1 and not root2:
			return None
		if not root1:
			return root2
			# 当这里写成root1 = root2时，赋值改变的是局部变量，不回传递回上层，所以root1.left还是会报错
		if not root2:
			return root1
		# 下面是root1和root2都存在的情况
		root1.val += root2.val
		left = self.mergeTrees(root1.left, root2.left)
		right = self.mergeTrees(root1.right, root2.right)
		root1.left = left
		root1.right = right
		return root1

# 76.计算布尔二叉树的值
class Solution:
	def evaluateTree(self, root):
		if not root.left and not root.right:
			# return True if root.val else False
			return bool(root.val)
		left = self.evaluateTree(root.left)
		right = self.evaluateTree(root.right)
		if root.val == 2:
			return left or right
		else:
			return left and right

# 77.出现次数最多的子树元素和
class Solution:
	def findFrequentTreeSum(self, root):
		if not root.left and not root.right:
			return [root.val]
		dic_win = defaultdict(int)
		def get_sum(root):
			if not root:
				return 0
			# if not root.left and not root.right:
			# 	return root.val
			left = get_sum(root.left)
			if left != 0:
				dic_win[left] += 1
			right = get_sum(root.right)
			if right != 0:
				dic_win[right] += 1
			dic_win[left + right + root.val] += 1
		get_sum(root)
		mx_cnt = max(cnt for _, cnt in dic_win.items())
		ans = []
		for key, val in dic_win.items():
			if val == mx_cnt:
				ans.append(key)
		return ans
class Solution:
	def findFrequentTreeSum(self, root):
		if not root:
			return []

		dic_win = defaultdict(int)
		def get_sum(node):
			if not node:
				return 0
			left = get_sum(node.left)
			right = get_sum(node.right)
			curr_sum = left + right + node.val
			dic_win[curr_sum] += 1
			return curr_sum
		get_sum(root)
		mx_cnt = max(dic_win.values())
		return [s for s, cnt in dic_win.items() if cnt == mx_cnt]

# 78.删除子文件夹
class Solution:
	def removeSubfolders(self, folder):
		folder.sort(key = lambda x:len(x))
		set_win = set()
		ans = []
		for i, file_path in enumerate(folder):
			tag = False
			for path in set_win:
				n = len(path)
				if path in file_path and file_path[:n] == path and file_path[n] == '/':
					tag = True
					break
			if not tag:
				ans.append(i)
				set_win.add(file_path)
		return [folder[i] for i in ans]
## 灵神思路
'''按字典序排序后只需要与上一个未被删除的路径比较即可'''
class Solution:
	def removeSubfolders(self, folder):
		folder.sort()
		ans = [folder[0]]
		for s in folder[1:]:
			last = ans[-1]
			if not s.startswith(last) or s[len(last)] != '/':
				ans.append(s)
		return ans

# 79.二叉树的坡度
class Solution:
	def findTilt(self, root):
		ans = 0
		def dfs(node):
			nonlocal ans
			if not node:
				return 0
			if not node.left and not node.right:
				return node.val
			left = dfs(node.left)
			right = dfs(node.right)
			ans += abs(left - right)
			return left + right + node.val
		dfs(root)
		return ans

# 80.根据二叉树创建字符串
class Solution:
	def tree2str(self, root):
		ans = ''
		def dfs(node):
			nonlocal ans
			if not node:
				return
			ans += str(node.val) + '('
			dfs(node.left)
			dfs(node.right)
			ans += ')'
		dfs(root)
		result = []
		for i in range(1, len(ans)):
			if ans[i] == ')' and result[-1] == '(':
				result.pop()
			else:
				result.append(ans[i])
		return ''.join(result)

# 81.统计值等于子树平均值的节点数
class Solution:
	def averageOfSubtree(self, root):
		ans = 0
		def dfs(node):
			if not node:
				return (0, 0)
			left_sum, left_cnt = dfs(node.left)
			right_sum, right_cnt = dfs(node.right)

			total_sum = left_sum + right_sum + node.val
			total_cnt = left_cnt + right_cnt + 1
			avg = total_sum // total_cnt
			nonlocal ans
			ans += int(node.val == avg)
			return (total_sum, total_cnt)
		dfs(root)
		return ans

# 72.第k大的完美二叉子树的大小
class Solution:  # 错解
	def kthLargestPerfectSubtree(self, root, k):
		ans = []
		def dfs(node):
			if not node:
				return 0, 0
			if node.left and node.right:
				tag = True
			else:
				tag = False
			l_depth, l_cnt = dfs(node.left)
			r_depth, r_cnt = dfs(node.right)
			if tag and l_depth == r_depth:
				ans.append(l_cnt + r_cnt + 1)
			return max(l_depth, r_depth) + 1, l_cnt + r_cnt + 1
		dfs(root)
		ans.sort()
		return ans[-k] if len(ans) >= k else -1
## 正确题解
class Solution:
	def kthLargestPerfectSubtree(self, root, k):
		ans = []
		def dfs(node):
			if not node:
				return True, 0, 0
			l_tag, l_depth, l_cnt = dfs(node.left)
			r_tag, r_depth, r_cnt = dfs(node.right)
			is_tag = l_tag and r_tag and l_depth == r_depth

			size = l_cnt + r_cnt + 1
			depth = max(l_depth, r_depth) + 1
			if is_tag:
				ans.append(size)
			return is_tag, depth, size
		dfs(root)
		ans.sort()
		return ans[-k] if len(ans) >= k else -1
## 灵神思路
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        hs = []
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            left_h = dfs(node.left)
            right_h = dfs(node.right)
            if left_h < 0 or left_h != right_h:
                return -1  # 不合法
            hs.append(2 ** (left_h + 1) - 1)
            return left_h + 1
        dfs(root)

        if k > len(hs):
            return -1
        hs.sort()
        return hs[-k] if len(hs) >= k else -1

# 73.打折购买糖果的最小开销
class Solution:
	def minimumCost(self, cost):
		ans = 0
		temp_lis = []
		cost.sort(reverse = True)
		for i in range(len(cost)):
			if len(temp_lis) >= 2 and temp_lis[-1] >= cost[i]:
				temp_lis = []
				continue
			temp_lis.append(cost[i])
			ans += cost[i]
		return ans

# 74.分裂二叉树的最大乘积
class Solution:
	def maxProduct(self, root):
		total_s = 0
		mod = 10 ** 9 + 7
		def dfs(node):
			if not node:
				return
			nonlocal total_s
			total_s += node.val
			dfs(node.left)
			dfs(node.right)
		dfs(root)

		ans = 0
		def sub_dfs(node):
			if not node:
				return 0
			left = sub_dfs(node.left)
			right = sub_dfs(node.right)
			nonlocal ans
			temp_s = left + right + node.val
			ans = max(ans, (total_s-temp_s) * temp_s)
			return left + right + node.val
		sub_dfs(root)
		return ans % mod

# 75.二叉树剪枝
class Solution:
	def pruneTree(self, root):
		def dfs(node):
			if not node:
				return None
			node.left = dfs(node.left)
			node.right = dfs(node.right)
			if node.val == 0 and not node.left and not node.right:
				return None
			return node
		return dfs(root)  # 这个返回值才是真正剪枝后的新根节点
		# dfs(root)
		# return root  # 这样的话仍然返回原始root的根节点，当剪枝后是None就错了

# 76.删除给定值的叶子节点
class Solution:
	def removeLeafNodes(self, root, target):
		def dfs(node):
			if not node:
				return None
			node.left = dfs(node.left)
			node.right = dfs(node.right)
			if not node.left and not node.right and node.val == target:
				return None
			return node
		return dfs(root)

# 77.删点成林
class Solution:
	def delNodes(self, root, to_delete):
		ans = []
		to_delete = set(to_delete)
		def dfs(node):
			if not node:
				return None
			node.left = dfs(node.left)
			node.right = dfs(node.right)
			if node.val in to_delete:
				if node.left:
					ans.append(node.left)
				if node.right:
					ans.append(node.right)
				return None
			return node
		root = dfs(root)
		if root:
			ans.append(root)
		return ans

# 78.删除字符使字符串变好
class Solution:
	def makeFancyString(self, s):
		n = len(s)
		s += '0'
		ans = temp_s = ''
		for i in range(n):
			temp_s += s[i]
			if s[i] == s[i + 1]:
				continue
			ans += temp_s[:2]
			temp_s = ''
		return ans
## 灵神题解——用cnt计数
class Solution:
	def makeFancyString(self, s):
		ans = []
		cnt = 0
		for i, x in enumerate(s):
			cnt += 1
			if cnt < 3:
				ans.append(x)
			if i < len(s) - 1 and x != s[i + 1]:
				cnt = 0
		return ''.join(ans)

# 79.二叉树的直径
class Solution:
	def diameterOfBinaryTree(self, root):
		ans = 0
		def dfs(node):
			if not node:
				return -1
			left = dfs(node.left)
			right = dfs(node.right)
			nonlocal ans
			ans = max(ans, left + right + 2)  # 以当前节点为中间节点的最长直径
			return max(left, right) + 1  # 以当前节点为根的子树的最长链
		dfs(root)
		return ans

# 80.最长同值路径
class Solution:  # 错解
	def longestUnivaluePath(self, root):
		ans = 0
		def dfs(node):
			if not node:
				return -1
			if not node.left and not node.right:
				return 0
			left = dfs(node.left)
			right = dfs(node.right)
			nonlocal ans
			if node.left and node.val != node.left:
				ans = max(ans, right + 1)
				return right + 1
			elif node.right and node.val != node.right:
				ans = max(ans, left + 1)
				return left + 1
			else:
				ans = max(ans, left + right + 2)
				return max(left, right) + 1
		dfs(root)
		return ans
class Solution:  
	def longestUnivaluePath(self, root):
		ans = 0
		def dfs(node):
			if not node:
				return 0
			left_len = dfs(node.left)  # 一定要先递归再判断！！！
			right_len = dfs(node.right)

			left_path = right_path = 0
			if node.left and node.left.val == node.val:
				left_path = left_len + 1
			if node.right and node.right.val == node.val:
				right_path = right_len + 1

			nonlocal ans
			ans = max(ans, left_path + right_path)
			return max(left_path, right_path)  # 返回父节点最长单边路径
		dfs(root)
		return ans

# 81.二叉树中的最大路径和
class Solution:
	def maxPathSum(self, root):
		ans = -inf
		def dfs(node):
			if not node:
				return 0
			left = max(dfs(node.left), 0)  # 左子树和为负数时就剪枝
			right = max(dfs(node.right), 0)
			nonlocal ans
			ans = max(ans, left + right + node.val)
			return max(left, right) + node.val
		dfs(root)
		return ans

# 82.二叉树的所有路径
class Solution:
	def binaryTreePaths(self, root):
		ans = []
		def dfs(node, temp_s):
			if not node:
				return
			temp_s += str(node.val) + '->'
			if not node.left and not node.right:
				temp_s = temp_s[:-2]
				ans.append(temp_s)
				return
			dfs(node.left, temp_s)
			dfs(node.right, temp_s)
		dfs(root, '')
		return ans
## 灵神思路——回溯
class Solution:
	def binaryTreePaths(self, root):
		ans = []
		path = []
		def dfs(node):
			if not node:
				return 
			path.append(node.val)
			if not node.left and not node.right:
				ans.append('->'.join(path))
				# return
			dfs(node.left)
			dfs(node.right)
			path.pop()
		dfs(root)
		return ans
			
# 83.删除子数组的最大得分
class Solution:
	def maximumUniqueSubarray(self, nums):
		set_win = set()
		ans = temp_s = left = 0
		for right, x in enumerate(nums):
			temp_s += x
			while x in set_win:
				set_win.remove(nums[left])
				temp_s -= nums[left]
				left += 1
			set_win.add(x)
			ans = max(ans, temp_s)
		return ans

# 84.路径总和2
class Solution:
	def pathSum(self, root, targetSum):
		ans = []
		path = []
		def dfs(node):
			if not node:
				return 
			path.append(node.val)
			if not node.left and not node.right and sum(path) == targetSum:
				ans.append(path.copy())
			else:
				dfs(node.left)
				dfs(node.right)
			path.pop()
		dfs(root)
		return ans

# 85.路径总和3
class Solution:
	def pathSum(self, root, targetSum):
		ans = 0
		path = [0]
		def dfs(node):
			nonlocal ans 
			if not node:
				pre_s_dic = Counter(pre_s)
				for x in pre_s:
					pre_s_dic[x] -= 1
					ans += pre_s_dic[x + targetSum]
					# pre_s_dic[x] += 1
				return
			path.append(node.val + path[-1])
			dfs(node.left)
			dfs(node.right)
			path.pop()
		dfs(root)
		return ans
## 上面错解的修改
class Solution:
    def pathSum(self, root, targetSum):
        self.ans = 0
        path = [0]  # 初始前缀和为0（模拟从根之前的空路径）

        def dfs(node):
            if not node:
                return

            # 当前路径和 = 父路径和 + 当前值
            curr_sum = path[-1] + node.val
            path.append(curr_sum)

            # 枚举前缀，判断是否有 curr_sum - old_sum == targetSum
            for pre_sum in path[:-1]:  # 排除当前的自己
                if curr_sum - pre_sum == targetSum:
                    self.ans += 1

            # 递归左右子树
            dfs(node.left)
            dfs(node.right)

            path.pop()  # 回溯

        dfs(root)
        return self.ans

## 灵神题解
class Solution:
	def pathSum(self, root, targetSum):
		ans = 0
		cnt = defaultdict(int)
		cnt[0] = 1
		def dfs(node, s):
			if not node:
				return
			nonlocal ans
			s += node.val  # 把node当作路径的终点，统计有多少个起点
			ans += cnt[s - targetSum]
			cnt[s] += 1  # 注意顺序，排除当前的s
			dfs(node.left, s)
			dfs(node.right, s)
			cnt[s] -= 1
		dfs(root, 0)
		return ans

# 86.删除子字符串的最大得分
## 思路一：贪心+两次栈
class Solution:
	def maximumGain(self, s, x, y):
		def remove_pair(s, first, second, score):
			stack = []
			total = 0
			for c in s:
				if stack and stack[-1] == first and c == second:
					stack.pop()
					total += score
				else:
					stack.append(c)
			return ''.join(stack), total

		ans = 0

# 87.二叉树的最近公共祖先
class Solution:
	def lowestCommonAncestor(self, root, p, q):
		 if not root or root is p or root is q:
		 	return root
		 left = self.lowestCommonAncestor(root.left, p, q)
		 right = self.lowestCommonAncestor(root.right, p, q)
		 if left and right:
		 	return root
		 if left:
		 	return left
		 return right

# 88.二叉搜索的最近公共祖先
class Solution:
	def lowestCommonAncestor(self, root, p, q):
		x = root.val
		if p.val < x and q.val < x:
			return self.lowestCommonAncestor(root.left, p, q)
		if p.val > x and q.val > x:
			return self.lowestCommonAncestor(root.right)
		return root

# 89.电话号码的字母组合
class Solution:  # O(n4^n)
	def letterCombinations(self, digits):
		n = len(digits)
		if n == 0:
			return []

		mapping = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
		ans = []
		path = [''] * n
		def dfs(i):
			if i == n:
				ans.append(''.join(path))
				return 
			for c in mapping[int(digits[i])]:
				path[i] = c
				dfs(i + 1)
		dfs(0)
		return ans

# 90.子集
class Solution:  # O(n2^n)
	def subsets(self, nums):
		n = len(nums)

		ans = []
		path = []
		def dfs(i):
			if i == n:
				ans.append(path.copy())  # 列表复制的复杂度是O(n)
				return

			dfs(i + 1)  # 不选的情况，这里因为本身就没有改变路径结构，所以不需要回溯，不必ifelse区分场景分别回溯

			path.append(nums[i])
			dfs(i + 1)  # 选的情况
			path.pop()
		dfs(0)
		return ans

# 91.找出所有子集的异或总和再求和
class Solution:
	def subsetXORSum(self, nums):
		n = len(nums)
		ans = path = 0
		def dfs(i):
			nonlocal ans, path
			if i == n:
				ans += path
				return

			dfs(i + 1)  # 不选
			path ^= nums[i]  # 选
			dfs(i + 1)
			path ^= nums[i]  # 回溯
		dfs(0)
		return ans

# 92.字母大小写全排列
class Solution:  # 避免了回溯，因为每次进入dfs时重新修改和判断path[i]的值
	def letterCasePermutation(self, s):
		ans = set()
		n = len(s)
		path = [''] * n
		def dfs(i):
			if i == n:
				ans.add(''.join(path))
				return

			path[i] = s[i]
			dfs(i + 1)
			if s[i].isupper():
				path[i] = s[i].lower()
				dfs(i + 1)  # 转换
			elif s[i].islower():
				path[i] = s[i].upper()
				dfs(i + 1)  # 转换
			
			# path.pop()
		dfs(0)
		return list(ans)

# O(n*2^k) k为字母的个数
class Solution:
	def letterCasePermutation(self, s):
		ans = []
		n = len(s)
		path = []
		def dfs(i):
			if i == n:
				ans.append(''.join(path))
				return
			if s[i].isalpha():
				path.append(s[i].lower())  # 对于本题，转变与不转变才是选与不选问题，要放在一起而不能用ifelse，才可以让每一种情况都有可能发生
				dfs(i + 1)
				path.pop()

				path.append(s[i].upper())
				dfs(i + 1)
				path.pop()
			else:
				path.append(s[i])
				dfs(i + 1)
				path.pop()
		dfs(0)
		return ans

# 93.字母组合迭代器
class CombinationIterator:

	def __init__(self, characters, combinationLength):
		self.ans = []
		n = len(characters)
		path = []
		def dfs(i):
			if i == n:
				if len(path) == combinationLength:
					self.ans.append(''.join(path))
				return
		# 	dfs(i + 1)  # 不选
		# 	path.append(characters[i])
		# 	dfs(i + 1)  # 选
		# 	path.pop()
		# dfs(0)
		# self.ans.sort()

		# 优化——要求有序必须先选
			path.append(characters[i])
			dfs(i + 1)  # 选
			path.pop()
			dfs(i + 1)  # 不选
		dfs(0)

	def next(self):
		return self.ans.pop(0)

	def hasNext(self):
		return len(self.ans) > 0

		#枚举选那个
		path = []
		self.queue = []
		def dfs(i):
			if len(path) == combinationLength:
				self.queue.append(''.join(path))
				return 
			for j in range(i, len(characters)):
				path.append(characters[j])
				dfs(j+1)
				path.pop()
		dfs(0)

# 94.目标和
class Solution:  # 超时，O(n*2^n)
	def findTargetSumWays(self, nums, target):
		ans = path = 0
		n = len(nums)
		def dfs(i):
			nonlocal ans, path
			if i == n:
				if path == target:
					ans += 1
				return

			path += nums[i]  # + 的情况
			dfs(i + 1)
			path -= nums[i]

			path -= nums[i]  # - 的情况
			dfs(i + 1)
			path += nums[i]
		dfs(0)
		return ans
## 记忆化搜索,O(n*sum(nums))
class Solution:  
	def findTargetSumWays(self, nums, target):
		n = len(nums)
		@cache
		def dfs(i, temp_s):
			if i == n:
				return int(temp_s == target)
			return dfs(i + 1, temp_s + nums[i]) + dfs(i + 1, temp_s - nums[i])
		return dfs(0, 0)
## 灵神题解——01背包思路,O(nm)
class Solution:
	def findTargetSumWays(self, nums, target):
		s = sum(nums) - abs(target)
		if s < 0 or s % 2:
			return 0

		@cache
		def dfs(i, c):
			if i < 0:
				return int(c == 0)
			if c < nums[i]:
				return dfs(i - 1, c)  # 只能不选
			return dfs(i - 1, c) + dfs(i - 1, c - nums[i])  # 不选 + 选
		m = s // 2
		return dfs(len(nums) - 1, m)

# 95.删除后的最大子数组元素和
class Solution:  # 这个题解是解原数组中的连续子数组最大和
	def maxSum(self, nums):
		pre_s = list(accumulate(nums, initial = 0))
		ans = -inf
		left = 0
		dic_win = defaultdict(int)
		for right, x in enumerate(pre_s[1:]):
			dic_win[nums[right]] += 1
			while dic_win[nums[right]] > 1:
				dic_win[nums[left]] -= 1
				left += 1
			ans = max(ans, x - min(pre_s[left:right]))
		return ans
## 优化
class Solution:
    def maxSum(self, nums):
        pre_s = list(accumulate(nums, initial=0))
        ans = float('-inf')
        left = 0
        dic_win = defaultdict(int)
        s = SortedList()
        s.add(pre_s[0])

        for right, x in enumerate(pre_s[1:]):
            dic_win[nums[right]] += 1

            while dic_win[nums[right]] > 1:
                s.remove(pre_s[left])
                dic_win[nums[left]] -= 1
                left += 1

            ans = max(ans, x - s[0])
            s.add(x)

        return ans
## 原题解法
class Solution:
	def maxSum(self, nums):
		nums = list(set(nums))
		temp_s = 0
		nums.sort(reverse = True)
		for x in nums:
			if x <= 0:
				break
			temp_s += x
		return temp_s if temp_s > 0 else x
class Solution:
	def maxSum(self, nums):
		nums = set(nums)
		temp_s = 0
		mx = -inf
		for x in nums:
			if x >= 0:
				temp_s += x
			mx = max(mx, x)
		return temp_s if temp_s > 0 else mx

# 96.统计数组中峰和谷的数量
class Solution:
	def countHillValley(self, nums):
		ans = tag = pre_tag = 0
		for i, x in enumerate(nums):
			if i == 0 or i == len(nums):
				continue
			for j in range(i - 1, -1, -1):
				if nums[j] > x:
					tag = 1  # 谷的情况
					break
				elif nums[j] < x:
					tag = -1  # 峰的情况
					break
			if tag == 0:
				pre_tag = 0
				continue
			for k in range(i + 1, len(nums)):
				if (nums[k] > x and tag == 1):
					ans += 1
					(nums[k] < x and tag == -1):
					ans += 1
					break
		return ans
## 优化——遇到相同的直接继续循环到最后一个
class Solution:
	def countHillValley(self, nums):
		ans = 0
		pre_num = nums[0]
		for i, x in enumerate(nums):
			if i == 0 or i == len(nums)-1 or nums[i] == nums[i + 1]:
				continue
			if (pre_num > x and nums[i + 1] > x) or \
				(pre_num > x and nums[i + 1] > x):
				ans += 1
			pre_num = nums[i]
		return ans
## 灵神解法
class Solution:
	def countHillValley(self, nums):
		ans = 0
		pre = nums[0]
		for i in range(1, len(nums) - 1):
			cur = nums[i]
			nxt = nums[i + 1]
			if cur == nxt:
				continue
			if pre != cur and (pre < cur) == (cur > nxt):
				ans += 1
			pre = cur
		return ans

# 97.等积子集的划分方案
class Solution:
	def checkEqualPartitions(self, nums, target):
		plus_s = 1
		n = len(nums)
		for x in nums:
			plus_s *= x
		@cache
		def dfs(i, temp_plus):
			if i == n:
				return temp_plus == target and plus_s // temp_plus == target
			return dfs(i + 1, temp_plus * nums[i]) or dfs(i + 1, temp_plus)
		return dfs(0, 1)

# 98.烹饪料理
class Solution:
	def perfectMenu(self, material, cookbooks, attribute, limit):
		ans = -1
		n = len(cookbooks)
		m = len(cookbooks[0])
		path = [0] * m
		def dfs(i, temp_x, temp_y):
			nonlocal ans
			if i == n:
				if temp_y >= limit:
					ans = max(ans, temp_x)
				return 
			dfs(i + 1, temp_x, temp_y)  # 如果放在选这之后要注意temp_x, temp_y也被修改了需要回溯
			if all(path[j] + cookbooks[i][j] <= material[j] for j in range(m)):
				temp_x += attribute[i][0]
				temp_y += attribute[i][1]
				for j in range(m):
					path[j] += cookbooks[i][j]
				dfs(i + 1, temp_x, temp_y)
				for j in range(m):
					path[j] -= cookbooks[i][j]
		dfs(0, 0, 0)
		return ans
class Solution:
	def perfectMenu(self, material, cookbooks, attribute, limit):
		ans = -1
		n = len(cookbooks)
		m = len(cookbooks[0])
		path = [0] * m
		def dfs(i, temp_x, temp_y):
			nonlocal ans
			if i == n:
				if temp_y >= limit:
					ans = max(ans, temp_x)
				return 

			if all(path[j] + cookbooks[i][j] <= material[j] for j in range(m)):
				for j in range(m):
					path[j] += cookbooks[i][j]
				dfs(i + 1, temp_x + attribute[i][0], temp_y + attribute[i][1])
				for j in range(m):
					path[j] -= cookbooks[i][j]
			dfs(i + 1, temp_x, temp_y)  # 如果放在选这之后要注意temp_x, temp_y也被修改了需要回溯
		dfs(0, 0, 0)
		return ans
#################### 划分型回溯 ###################
# 99.分割回文串
## 灵神题解——逗号选或不选
class Solution:
	def partition(self, s):
		n = len(s)
		ans = []
		path = []
		def dfs(i, start):  # start表示子串开始的位置
			if i == n:
				ans.append(path.copy())
				return
			# 不选，当i = n - 1时只能分割
			if i < n - 1:
				dfs(i + 1, start)
			# 分割，选i和i + 1之间的逗号
			t = s[start:i + 1]
			if t == t[::-1]:
				path.append(t)
				dfs(i + 1, i + 1)
				path.pop()
		dfs(0, 0)
		return ans

# 100.统计按位或能得到最大值的子集数目
class Solution:
	def countMaxOrSubsets(self, nums):
		ans = 0
		path = []
		ans_lis = []
		n = len(nums)
		def dfs(i, temp_s):
			nonlocal ans
			if i == n:
				ans = max(ans, temp_s)
				ans_lis.append(path.copy())
				return
			dfs(i + 1, temp_s)  # 不选
			path.append(nums[i])
			dfs(i + 1, temp_s | nums[i])  # 选
			path.pop()
		dfs(0, 0)
		result = 0
		for path in ans_lis:
			pre = 0
			for x in path:
				pre |= x
			result += int(pre == ans)
		return ans
## 优化
class Solution:
	def countMaxOrSubsets(self, nums):
		max_or = 0
		count = 0
		n = len(nums)
		def dfs(i, or_sum):
			nonlocal max_or, count
			if i == n:
				if or_sum > max_or:
					count = 1
					max_or = or_sum
				elif or_sum == max_or:
					count += 1
				return
			dfs(i + 1, or_sum)
			dfs(i + 1, or_sum | nums[i])
		dfs(0, 0)
		return count
## 灵神题解
class Solution:
	def countMaxOrSubsets(self, nums):
		total_or = reduce(or_, nums)  # 按位或越多元素越大
		n = len(nums)
		ans = 0
		def dfs(i, subset_or):
			nonlocal ans
			if i == n:
				ans += int(subset_or == total_or)
				return
			dfs(i + 1, subset_or)  # 不选
			dfs(i + 1, subset_or | nums[i])  # 选
		dfs(0, 0)
		return ans

# 101.求一个整数的惩罚数
## 灵神题解
pre_sum = [0] * 1001
for i in range(1, 1001):
	s = str(i * i)
	n = len(s)
	def dfs(p, sum):
		if p == n:
			return sum == i
		x = 0
		for j in range(p, n):  # 枚举分割出从s[p]到s[j]的子串
			x = x * 10 + int(s[j])
			if dfs(j + 1, sum + x):
				return True
		return False
	pre_sum[i] = pre_sum[i - 1] + (i * i if dfs(0, 0) else 0)
class Solution:
	def punishmentNumber(self, n):
		return pre_sum[n]

# 102.按位或最大的最小子数组长度
class Solution:
	def smallestSubarrays(self, nums):
		n = len(nums)
		sub_or = [0] * (n + 1)
		for i in range(n - 1, -1, -1):
			sub_or[i] = sub_or[i + 1] | nums[i]

		ans = []
		for i, x in enumerate(nums):
			for j in range(i, n):
				x |= nums[j]
				if x == sub_or[i]:
					ans.append(j - i + 1)
					break
		return ans
# O(n*32)优化
class Solution:
	def smallestSubarrays(self, nums):
		n = len(nums)
		ans = [0] * n
		last = [0] * 32

		for i in range(n - 1, -1, -1):
			for bit in range(32):
				if (nums[i] >> bit) & 1:  #判断nums[i]的第bit位是不是1
					last[bit] = i
			furthest = i  # 以nums[i]为起始的要延伸的最远位置
			for bit in range(32):
				furthest = max(furthest, last[bit])
			ans[i] = furthest - i + 1
		return ans
## 灵神题解1
class Solution:
	def smallestSubarrays(self, nums):
		ans = [1] * len(nums)
		for i, x in enumerate(nums):
			for j in range(i - 1, -1, -1):
				if (nums[j] | x) == nums[j]:  # 
					break

# 103.组合
class Solution:  # O(n * 2^n)
	def combine(self, n, k):
		ans = []
		path = []
		def dfs(i):
			if i == n:
				if len(path) == k:
					ans.append(path.copy())
				return
			## 剪枝, O(k * 2^n)
			if len(path) + n - i < k:
				return
			dfs(i + 1)  # 不选
			if len(path) < k:
				path.append(i + 1)
				dfs(i + 1)  # 选
				path.pop()  # 恢复现场
		dfs(0)
		return ans
## 灵神题解——O(k * Cnk)，组合数Cnk，路径长度k
class Solution:
	def combine(self, n, k):
		ans = []
		path = []

		def dfs(i):
			d = k - len(path)  # 还需要选的数
			if d == 0:
				ans.append(path.copy())
				return

			if i > d:
				dfs(i - 1)  # 不选（当元素足够时才可以不选）
			path.append(i)
			dfs(i - 1)
			path.pop()
		dfs(n)  # 倒序枚举从n到1
		return ans

# 104.组合总和3
class Solution:
	def combinationSum3(self, k, n):
		ans = []
		path = []
		def dfs(i):
			diff = n - sum(path)
			if diff == 0 and len(path) == k:
				ans.append(path.copy())
				return
			if i == 10 or sum(path) > n or len(path) > k:
				return

			dfs(i + 1)  # 不选
			path.append(i)
			dfs(i + 1)  # 选
			path.pop()
		dfs(1)
		return ans

# 105.子集2
class Solution:
	def subsetsWithDup(self, nums):
		nums.sort()
		n = len(nums)
		ans = []
		path = []
		def dfs(i):
			if i == n:
				ans.append(path.copy())
				return
			## 选x,之后的x可选可不选
			x = nums[i]
			path.append(x)
			dfs(i + 1)
			path.pop()

			## 不选x，那么之后的x都不能选
			i += 1
			while i < n and nums[i] == x:
				i += 1
			dfs(i)
		dfs(0)
		return ans

# 106.按位与最大的最长子数组
class Solution:
	def longestSubarray(self, nums):
		mx_num = max(nums)
		ans = 1
		i = 0
		n = len(nums)
		while i < n:
			if nums[i] == mx_num:
				start = i
				while i < n and nums[i] == mx_num:
					i += 1
				ans = max(ans, i - start)
			i += 1
		return ans
## 滑动窗口	
class Solution:
	def longestSubarray(self, nums):
		mx = max(nums)
		ans = left = 0
		for right, x in enumerate(nums):
			if x != mx:
				left = right + 1
			ans = max(ans, right - left + 1)
		return ans

# 107.组合总和2
class Solution:
	def combinationSum2(self, candidates, target):
		candidates.sort()
		ans = []
		path = []
		n = len(candidates)
		def dfs(i):
			if sum(path) == target:
				ans.append(path.copy())
				return
			if i == n or sum(path) > target:
				return
			## 选
			x = candidates[i]
			path.append(x)
			dfs(i + 1)
			path.pop()

			## 不选
			i += 1
			while i < n and candidates[i] == x:
				i += 1
			dfs(i)
		dfs(0)
		return ans
## 灵神题解
class Solution:
	def combinationSum2(self, candidates, target):
		candidates.sort()
		ans = []
		path = []
		n = len(candidates)
		def dfs(i, left):
			if left == 0:
				ans.append(path.copy())
				return
			if i == n:
				return
			x = candidates[i]
			if left < x:  # 后续无论选或不选都得>target
				return

			path.append(x)
			dfs(i + 1, left - x)
			path.pop()

			i += 1
			while i < n and candidates[i] == x:
				i += 1
			dfs(i, left)
		dfs(0, target)
		return ans

# 108.非递减子序列
class Solution:
	def findSubsequences(self, nums):
		ans = []
		path = []
		n = len(nums)
		def dfs(i):
			if i == n:
				if len(path) >= 2:
					ans.append(path.copy())
				return

			## 选
			x = nums[i]
			if not path or x >= path[-1]:
				path.append(x)
				dfs(i + 1)
				path.pop()

			## 不选——这种解法必须要排序
			i += 1
			while i < n and nums[i] == x:
				i += 1
			dfs(i)
		dfs(0)
		return ans
class Solution:  
	def findSubsequences(self, nums):
		ans = []
		n = len(nums)

		def dfs(i, path):
			if len(path) >= 2:
				if path[-1] >= path[-2]:
					ans.append(path)
				else:
					return

			for j in range(i, n):
				if nums[j] in nums[i:j]:
					continue
				dfs(i + 1, path + [nums[i]])
		dfs(0, [])
		return ans
class Solution:
    def findSubsequences(self, nums):
        result = []

        def backtracking(start_index, path):
            # 终止条件
            if len(path) >= 2:
                if path[-1] >= path[-2]:
                    result.append(path)
                else:
                    return 
            # 回溯
            for i in range(start_index, len(nums)):
                # 去重
                if nums[i] in nums[start_index:i]:
                    continue
                backtracking(i + 1, path + [nums[i]])
        
        backtracking(0, [])
        return result





