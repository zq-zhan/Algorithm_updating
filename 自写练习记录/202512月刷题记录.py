# 20251202统计梯形的数目1
class Solution:
	def countTrapezoids(self, points):
		MOD = 10 ** 9 + 7
		temp_dic = defaultdict(int)
		n = len(points)
		ans = 0
		for i in range(n):
			x1, y1 = points[i]
			for j in range(i, n):
				x2, y2 = points[j]
				if x1 != x2:
					k = (y2 - y1) / (x2 - x1)
					ans = (ans + temp_dic[k]) % MOD
					ans = (ans + temp_dic[-k]) % MOD
					temp_dic[k] += 1
		return ans
## 灵神题解
class Solution:
	def countTrapezoids(self, points):
		MOD = 10 ** 9 + 7
		cnt = Counter(p[1] for p in points)  # 统计每一行(y相同)有多少点
		ans = s = 0
		for c in cnt.values():
			k = c * (c - 1) // 2
			ans += s * k
			s += k
		return ans % MOD

# 20251203相交链表
## 灵神题解
class Solution:
	def getIntersectionNode(self, headA, headB):
		p, q = headA, headB
		while p is not q:
			p = p.next if p else headB
			q = q.next if q else headA
		return p
		
# 20251204统计道路上的碰撞次数
class Solution:
	def countCollisions(self, directions):
		directions = list(directions)
		ans = 0
		cnt = 1
		n = len(directions)
		for i in range(n - 1):
			if directions[i] == 'R':
				if directions[i + 1] == 'L':
					ans += cnt + 1
					directions[i + 1] = 'S'
					cnt = 1
				elif directions[i + 1] == 'S':
					ans += cnt
					cnt = 1
				else:
					cnt += 1
			elif directions[i] == 'L':
				if directions[i + 1] == 'L':
					cnt += 1
				elif directions[i + 1] == 'S':
					cnt = 1
				else:
					cnt = 1
			else:
				if directions[i + 1] == 'L':
					ans += cnt
					directions[i + 1] = 'S'
		return ans
## 灵神题解
class Solution:
	def countCollisions(self, s):
		s = s.lstrip('L')
		s = s.rstrip('R')
		return len(s) - s.count('S')  # 两辆相反算两次，一辆撞静止算1次计在移动车上

# 20251205统计元素和差值为偶数的分区方案
class Solution:
	def countPartitions(self, nums):
		s = sum(nums)
		ans = pre_s = 0
		for x in nums[:-1]:
			pre_s += x
			if pre_s % 2 == (s - pre_s) % 2:
				ans += 1
		return ans
## 灵神题解——只需判断s是否偶数
class Solution:
	def countPartitions(self, nums):
		return 0 if sum(nums) % 2 else len(nums) - 1

# 20251207在区间范围内统计奇数数目
class Solution:
	def countOdds(self, low, high):
		if low % 2 != high % 2:
			return (high - low) // 2 + 1
		elif low % 2 == high % 2 == 0:
			return (high - low) // 2
		else:
			return (high - low - 1) // 2 + 2
## 灵神解法：前缀和
class Solution:
	def countOdds(self, low, high):
		return (high + 1) // 2 - (low // 2) # [1, high]中正奇数的个数减去[1, low-1]中正奇数的个数

# 20251208统计平方和三元组的数目
class Solution:
	def countTriples(self, n):
		ans = 0
		for i in range(1, n):
			for j in range(i + 1, n):
				x = i ** 2 + j ** 2
				if x <= n ** 2 and isqrt(x) ** 2 == x:
					ans += 2
				elif x > n ** 2:
					break
		return ans

# 反转链表
class Solution:
	def reverseList(self, head):
		val_lis = []
		p = head
		while p:
			val_lis.append(p.val)
			p = p.next

		p = nummy_node = ListNode(0)
		for x in val_lis[::-1]:
			p.next = ListNode(x)
			p = p.next
		return nummy_node.next
## 头插法
class Solution1:
	def reverseList(self, head):
		pre = None
		cur = head
		while cur:
			nxt = cur.next
			cur.next = pre
			pre = cur
			cur = nxt
		return pre
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

# 反转链表2
class Solution:
	def reverseBetween(self, head, left, right):
		dummy = ListNode(next = head)
		p0 = dummy
		for _ in range(left - 1):
			p0 = p0.next

		pre = None
		cur = p0.next
		for _ in range(right - left + 1):
			nxt = cur.next
			cur.next = pre
			pre = cur
			cur = nxt

		p0.next.next = cur
		p0.next = pre
		return dummy.next

# k个一组翻转链表
class Solution:
	def reverseKGroup(self, head, k):
		n = 0
		p = head
		while p:
			p = p.next
			n += 1

		p0 = dummy = ListNode(next = head)
		pre = None
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
		return dummy.next


# 回文链表
class Solution:
	## 链表的中间节点
	def middleNode(self, head):
		slow = fast = head
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
		return slow

	## 反转链表
	def reverseList(self, head):
		pre = None
		cur = head
		while cur:
			nxt = cur.next
			cur.next = pre
			pre = cur
			cur = nxt
		return pre

	def isPalindrome(self, head):
		mid = self.middleNode(head)
		heads2 = self.reverseList(mid)
		while head2:
			if head2.val != head.val:
				return False
			head = head.next
			head2 = head2.next
		return True

## 环形链表
class Solution:
	def hasCycle(self, head, pos):
		slow = fast = head
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
			if slow is fast:
				return True
		return False

## 环形链表2
class Solution:
	def detectCycle(self, head):
		slow = fast = head
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
			if fast is slow:
				while slow is not head: # 头节点和慢节点同时走，再走a步一定在入环口相遇
					slow = slow.next
					head = head.next
				return slow
		return None

## 合并两个有序链表
class Solution:
	def mergeTwoLists(self, listA, listB):
		p = dummy = ListNode(0)
		while listA and listB:
			if listA.val <= listB.val:
				p.next = listA
				listA = listA.next
			else:
				p.next = listB
				listB = listB.next
			p = p.next
		# if listA:
		# 	p.next = listA
		# else:
		# 	p.next = listB
		p.next = listA or listB
		return dummy.next
### 递归写法
class Solution:
	def mergeTwoLists(self, listA, listB):
		if listA is None:
			return listB
		if listB is None:
			return listA
		if listA.val < listB.val:
			listA.next = self.mergeTwoLists(listA.next, listB)
			return listA
		listB.next = self.mergeTwoLists(listA, listB.next)
		return listB

# 两数相加
class Solution:
	def addTwoNumbers(self, l1, l2):
		p = dummy = ListNode()
		x = 0
		while l1 or l2:
			if l1 is None:
				l1 = ListNode(0)
			if l2 is None:
				l2 = ListNode(0)
			x = x // 10 + l1.val + l2.val
			p.next = ListNode(x % 10)
			l1 = l1.next
			l2 = l2.next
			p = p.next
		if x // 10:
			p.next = ListNode(x // 10)
		return dummy.next
## 迭代写法2
class Solution:
	def addTwoNumbers(self, l1, l2):
		p = dummy = ListNode()
		carry = 0
		while l1 or l2 or carry:
			if l1:
				carry += l1.val
				l1 = l1.next
			if l2:
				carry += l2.val
				l2 = l2.next
			p.next = ListNode(carry % 10)
			carry //= 10
			p = p.next
		return dummy.next
## 灵神题解——递归
class Solution:
	def addTwoNumbers(self, l1, l2, carry = 0):
		if l1 is None and l2 is None and carry == 0:
			return None

		s = carry
		if l1:
			s += l1.val
			l1 = l1.next
		if l2:
			s += l2.val
			l2 = l2.next
		return ListNode(s % 10, self.addTwoNumbers(l1, l2, s // 10))
## 原地修改
class Solution:
    # l1 和 l2 为当前遍历的节点，carry 为进位
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry=0) -> Optional[ListNode]:
        if l1 is None and l2 is None:  # 递归边界
            return ListNode(carry) if carry else None  # 如果进位了，就额外创建一个节点
        if l1 is None:  # 如果 l1 是空的，那么此时 l2 一定不是空节点
            l1, l2 = l2, l1  # 交换 l1 与 l2，保证 l1 非空，从而简化代码
        s = carry + l1.val + (l2.val if l2 else 0)  # 节点值和进位加在一起
        l1.val = s % 10  # 每个节点保存一个数位（直接修改原链表）
        l1.next = self.addTwoNumbers(l1.next, l2.next if l2 else None, s // 10)  # 进位
        return l1

# 删除链表的倒数第N个节点
class Solution:
	def removeNthFromEnd(self, head, n):
		slow = fast = dummy = ListNode(next = head)
		for _ in range(n):
			fast = fast.next

		while fast.next:
			slow = slow.next
			fast = fast.next
		slow.next = slow.next.next
		return dummy.next

# 两两交换链表中的节点
class Solution:
	def swapPairs(self, head):
		node0 = dummy = ListNode(head)
		node1 = head
		while node1 and node1.next:
			node2 = node1.next
			node3 = node2.next

			node0.next = node2
			node2.next = node1
			node1.next = node3

			node0 = node1
			node1 = node3
		return dummy.next

# 20251209统计特殊三元组
class Solution:
	def specialTriplets(self, nums):
		MOD = 10 ** 9 + 7
		sub_dic = Counter(nums)
		pre_dic = defaultdict(int)
		ans = 0
		for i, x in enumerate(nums): # 枚举中间
			sub_dic[x] -= 1
			ans = (pre_dic[x * 2] * sub_dic[x * 2] + ans) % MOD
			pre_dic[x] += 1
		return ans

# 随机链表的复制
## 灵神题解
class Solution:
	def copyRandomList(self, head):
		if head is None:
			return None

		cur = head
		while cur:
			cur.next = Node(cur.val, cur.next)
			cur = cur.next

		cur = head
		while cur:
			if cur.random:
				cur.next = cur.ran

# 排序链表
## 灵神题解——归并排序（分治）
class Solution:
	## 链表的中间节点
	def middleNode(self, head):
		slow = fast = head
		while fast and fast.next:
			pre = slow # 记录slow的前一个节点，用于分段
			slow = slow.next
			fast = fast.next.next
		pre.next = None
		return slow

	## 合并两个有序链表
	def mergeTwoLists(self, list1, list2):
		cur = dummy = ListNode()
		while list1 and list2:
			if list1.val <= list2.val:
				cur.next = list1
				list1 = list1.next
			else:
				cur.next = list2
				list2 = list2.next
			cur = cur.next
		cur.next = list1 if list1 else list2
		return dummy.next

	def sortList(self, head):
		if head is None or head.next is None:
			return head

		head2 = self.middleNode(head)

		# 分治
		head = self.sortList(head)
		head2 = self.sortList(head2)

		return self.mergeTwoLists(head, head2)

# 20251210统计计算机解锁顺序排列数
class Solution:
	def countPermutations(self, complexity):
		MOD = 10 ** 9 + 7

		ans = 1
		for i in range(1, len(complexity)):
			if complexity[i] <= complexity[0]:
				return 0
			ans = ans * i % MOD
		return ans

# 合并K个升序链表
class Solution:
	## 合并两个有序链表
	def mergeTowLists(self, l1, l2):
		p0 = dummy = ListNode()
		while l1 and l2:
			if l1.val <= l2.val:
				p0.next = l1
				l1 = l1.next
			else:
				p0.next = l2
				l2 = l2.next
			p0 = p0.next
		p0.next = l1 if l1 else l2
		return dummy.next

	# def mergeKLists(self, lists):
	# 	if not lists:
	# 		return None
	# 	l1 = lists[0]
	# 	for l2 in lists[1:]: # O(mL),O(1)
	# 		l1 = self.mergeTowLists(l1, l2)
	# 	return l1

	## 优化,O(Llogm),O(1)
	def mergeKLists(self, lists):
		m = len(lists)
		if m == 0:
			return None
		step = 1
		while step < m:
			for i in range(0, m - step, step * 2):
				lists[i] = self.mergeTowLists(lists[i], lists[i + step])
			step *= 2
		return lists[0]

# LRU缓存
## 灵神题解——双向链表
class Node:
	__slots__ = 'prev', 'next', 'key', 'value'

	def __init__(self, key = 0, value = 0):
		self.key = key
		self.value = value

class LRUCache:

	def __init__(self, capacity: int):
		self.capacity = capacity
		self.dummy = Node() # 哨兵节点
		self.dummy.prev = self.dummy
		self.dummy.next = self.dummy
		self.key_to_node = {}

	def get_node(self, key):
		if key not in self.key_to_node:
			return None
		node = self.key_to_node[key]
		self.remove(node)
		self.push_front(node)
		return node

	def get(self, key: int) -> int:
		node = self.get_node(key)
		return node.value if node else -1

	def put(self, key: int, value: int) -> None:
		node = self.get_node(key)
		if node:
			node.value = value
			return
		self.key_to_node[key] = node = Node(key, value)
		self.push_front(node) # 放到最上面
		if len(self.key_to_node) > self.capacity:
			back_node = self.dummy.prev
			del self.key_to_node[back_node.key]
			self.remove(back_node)

	def remove(self, x):
		x.prev.next = x.next
		x.next.prev = x.prev

	def push_front(self, x): # 在链表头添加一个节点
		x.prev = self.dummy
		x.next = self.dummy.next
		x.prev.next = x
		x.next.prev = x

# 二叉树的中序遍历
class Solution:
	def inorderTraversal(self, root):
		ans = []
		def dfs(root):
			if not root:
				return
			nonlocal ans
			dfs(root.left)
			ans.append(root.val)
			dfs(root.right)
		dfs(root)
		return ans

# 20251211统计被覆盖的建筑
class Solution: # 超时
	def countCoveredBuildings(self, n, buildings):
		same_y_dic = defaultdict(list)
		buildings.sort()
		for x, y in buildings:
			same_y_dic[y].append((x, y))

		same_x_dic = defaultdict(list)
		buildings.sort(key = lambda x:x[1])
		for x, y in buildings:
			same_x_dic[x].append((x, y))

		ans = 0
		for y, lis in same_y_dic.items():
			if len(lis) >= 3:
				for x1, y1 in lis[1:-1]:
					same_x = set(same_x_dic[x1][1:-1])
					if (x1, y1) in same_x:
						ans += 1
		return ans
## 灵神题解
class Solution:
	def countCoveredBuildings(self, n, buildings):
		row_min = [n + 1] * (n + 1) # 同一行最小x
		row_max = [0] * (n + 1) # 同一行最大x
		col_min = [n + 1] * (n + 1) # 同一列最小y
		col_max = [0] * (n + 1) # 同一列最大y

		for x, y in buildings:
			if x < row_min[y]:
				row_min[y] = x
			if x > row_max[y]:
				row_max[y] = x
			if y < col_min[x]:
				col_min[x] = y
			if y > col_max[x]:
				col_max[x] = y

		ans = 0
		for x, y in buildings:
			if row_min[y] < x < row_max[y] and col_min[x] < y < col_max[x]:
				ans += 1
		rteurn ans
## 写法二
class Solution:
	def countCoveredBuildings(self, n, buildings):
		row = defaultdict(lambda: [inf,-inf])
		col = defaultdict(lambda: [inf,-inf])

		for x, y in buildings:
			row[x][0] = min(row[x][0], y) # 同一列最小y
			row[x][1] = max(row[x][1], y)
			col[y][0] = min(col[y][0], x) # 同一行最小x
			col[y][1] = max(col[y][1], x)

		ans = 0
		for x, y in buildings:
			if row[x][0] < y < row[x][1] and col[y][0] < x < col[y][1]:
				ans += 1
		return ans

# 二叉树的最大深度
class Solution:
	def maxDepth(self, root):
		ans = 0
		def dfs(root, mx_depth):
			if not root:
				nonlocal ans
				ans = max(ans, mx_depth)
				return
			mx_depth += 1
			dfs(root.left, mx_depth)
			dfs(root.right, mx_depth)
		dfs(root, 0)
		return ans
class Solution:
	def maxDepth(self, root):
		if not root:
			return 0
		l_depth = self.maxDepth(root.left)
		r_depth = self.maxDepth(root.right)
		return max(l_depth, r_depth) + 1

# 20251212统计用户被提及情况
class Solution:
	def countMentions(self, numberOfUsers, events):
		events.sort(key = lambda x:int(x[1]))
		ans = [0] * numberOfUsers
		offline_time = [-60] * numberOfUsers
		events_message = []
		events_offline = []
		for info, time, detail in events:
			if info == 'MESSAGE':
				events_message.append([info, int(time), detail])
			else:
				events_offline.append([info, int(time), int(detail)])
		idx_off = 0
		m = len(events_offline)
		for info, time, detail in events_message:
			while idx_off < m and events_offline[idx_off][1] <= time:
				offline_time[events_offline[idx_off][2]] = events_offline[idx_off][1]
				idx_off += 1
			if detail == "ALL":
				ans = [x + 1 for x in ans]
			elif detail == "HERE":
				for i in range(numberOfUsers):
					if offline_time[i] + 60 <= time:
						ans[i] += 1
			else:
				for idx in detail.split(' '):
					ans[int(idx[2])] += 1
			
		return ans
class Solution:
	def countMentions(self, numberOfUsers, events):
		events.sort(key = lambda x:(int(x[1]), x[0][2]))
		ans = [0] * numberOfUsers
		offline_time = [-60] * numberOfUsers
		for info, time, detail in events:
			time = int(time)
			if info == 'MESSAGE':
				if detail == "ALL":
					ans = [x + 1 for x in ans]
				elif detail == "HERE":
					for i in range(numberOfUsers):
						if offline_time[i] + 60 <= time:
							ans[i] += 1
				else:
					for idx in detail.split(' '):
						ans[int(idx[2:])] += 1 	
			else:
				offline_time[int(detail)] = time
		return ans

# 20251212优惠券校验器
class Solution:
	def validateCoupons(self, code, businessLine, isActive):
		n = len(code)
		temp_lis = []
		for i in range(n):
			if isActive[i] and businessLine[i] in ('electronics', 'grocery', 'pharmacy', 'restaurant')\
				and code[i] != '' and all(x.isalnum() or x == '_' for x in code[i]):
				temp_lis.append((businessLine[i], code[i]))
		temp_lis.sort()
		return [y for _, y in temp_lis]

# 20251213翻转二叉树
class Solution:
	def invertTree(self, root):
		if not root:
			return None
		root.left, root.right = root.right, root.left
		self.invertTree(root.left)
		self.invertTree(root.right)
		return root

# 对称二叉树
class Solution:
	def isSameTree(self, p, q):
		if p is None or q is None:
			return p is q
		return p.val == q.val and self.isSameTree(p.left, q.right) and self.isSameTree(p.right, q.left)

	def isSymmetric(self, root):
		return self.isSameTree(root.left, root.right)

# 二叉树的直径
class Solution:
	def diameterOfBinaryTree(self, root):
		ans = 0 
		def dfs(node):
			if node is None:
				return -1
			l_len = dfs(node.left) + 1
			r_len = dfs(node.right) + 1
			nonlocal ans
			ans = max(ans, l_len + r_len)
			return max(l_len, r_len)
		dfs(root)
		return ans

# 20251214分隔长廊的方案数
class Solution:
	def numberOfWays(self, corridor):
		MOD = 10 ** 9 + 7
		n = len(corridor)
		i = n - 1
		while i >= 0:
			if corridor[i] == 'P':
				i -= 1
				continue
			else:
				break
		corridor = corridor[:i + 1] + 'S'
		m = len(corridor)

		ans = 1
		i = cnt_s = 0
		while i < m:
			if i == m - 1 and cnt_s < 2:
				return 0
			cnt_s += int(corridor[i] == 'S')
			if cnt_s < 2:
				i += 1
				continue
			else:
				pre = i
				i += 1
				while corridor[i] == 'P':
					i += 1
				ans = ans * (i - pre) % MOD
				cnt_s = 1
				i += 1
		return ans
## 灵神思路
class Solution:
	def numberOfWays(self, corridor):
		MOD = 10 ** 9 + 7
		ans = 1
		cnt_s = last_s = 0
		for i, x in enumerate(corridor):
			if x == 'S':
				cnt_s += 1
				if cnt_s >= 3 and cnt_s % 2:
					ans = ans * (i - last_s) % MOD
				last_s = i
		if cnt_s == 0 or cnt_s % 2: # 座位数总计为0或奇数则return 0
			return 0
		return ans

# 二叉树的层序遍历
class Solution:
	def levelOrder(self, root):
		ans = defaultdict(list)
		depth = 0
		def dfs(root, depth):
			if not root:
				return 
			ans[depth].append(root.val)
			dfs(root.left, depth + 1)
			dfs(root.right, depth + 1)
		dfs(root, 0)
		new_ans = []
		for depth, lis in ans.items():
			new_ans.append(lis)
		return new_ans

# 将有序数组转换为二叉搜索树
## 递归
class Solution:
	def sortedArrayToBST(self, nums):
		if not nums:
			return None
		m = len(nums) // 2
		left = self.sortedArrayToBST(nums[:m])
		right = self.sortedArrayToBST(nums[m + 1:])
		return TreeNode(nums[m], left, right)
## 写法二
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(left, right):
            if left > right:
                return None
            m = (left + right) // 2
            return TreeNode(nums[m], dfs(left, m - 1), dfs(m + 1, right))
        return dfs(0, len(nums) - 1)

# 验证二叉搜索树
class Solution:
	def isValidBST(self, root):
		ans = True
		def dfs(node, min_x, max_x):
			if node is None:
				return

			nonlocal ans
			if not min_x < node.val < max_x:
				ans = False
				return

			dfs(node.left, min_x, node.val)
			dfs(node.right, node.val, max_x)
		dfs(root, -inf, inf)
		return ans
## 灵神题解
class Solution:
	def isValidBST(self, root, left, right):
		if root is None:
			return True
		x = root.val
		return left < x < right and self.isValidBST(root.left, left, x) and self.isValidBST(root.right, x, right)

# 二叉搜索树中第K小的元素
class Solution:
	def kthSmallest(self, root, k):
		ans = []
		def dfs(node):
			if not node:
				return
			nonlocal ans
			ans.append(node.val)
			dfs(node.left)
			dfs(node.right)
		dfs(root)
		ans.sort()
		return ans[k - 1]
## 灵神题解——中序遍历，每次递归完左子树就k-=1
class Solution:
	def kthSmallest(self, root, k):
		ans = 0
		def dfs(node):
			nonlocal k, ans
			if node is None or k == 0:
				return
			dfs(node.left)
			k -= 1
			if k == 0:
				ans = node.val
				return
			dfs(node.right)
		dfs(root)
		return ans

# 二叉树的右视图
class Solution:
	def rightSideView(self, root):
		ans = []
		mx_depth = -1
		def dfs(node, depth):
			if not node:
				return
			nonlocal mx_depth
			if depth > mx_depth:
				ans.append(node.val)
			mx_depth = max(mx_depth, depth)
			dfs(node.right, depth + 1)
			dfs(node.left, depth + 1)
		dfs(root, 0)
		return ans

# 股票平滑下跌阶段的数目
class Solution:
	def getDescentPeriods(self, prices):
		ans = 0
		temp_cnt = 1
		for i, x in enumerate(prices):
			if i > 0:
				if x == prices[i - 1] - 1:
					temp_cnt += 1
				else:
					temp_cnt = 1
			ans += temp_cnt
		return ans

# 二叉树展开为链表
class Solution:
	def flatten(self, root):
		ans = []
		def dfs(node):
			if not node:
				return
			ans.append(node)
			dfs(node.left)
			dfs(node.right)
		dfs(root)
		n = len(ans)
		for i in range(n - 1):
			ans[i].left = None
			ans[i].right = ans[i + 1]
		ans[-1].left = None
		ans[-1].right = None
		return root
## 灵神题解——分治
class Solution:
	def flatten(self, root):
		if root is None:
			return None
		left_tail = self.flatten(root.left)
		right_tail = self.flatten(root.right)
		if left_tail:
			left_tail.right = root.right
			root.right = root.left
			root.left = None
		return right_tail or left_tail or root
## 灵神题解——头插法(按右-左-根的顺序访问树，并记录当前节点作为head)
class Solution:
	head = None
	def flatten(self, root):
		if root is None:
			return
		self.flatten(root.right)
		self.flatten(root.left)
		root.left = None
		root.right = self.head
		self.head = root

# 20251216折扣价交易股票的最大利润
class Solution:
	def maxProfit(self, n, present, future, hierarchy, budget):
		hierarchy_dic = defaultdict(int)
		for key, value in hierarchy: # 直属上司
			hierarchy_dic[value - 1] = key - 1
		
		def dfs(i, money, tag):
			if i == n:
				return 0
			if 
## 灵神题解
# 注意！这个写法很慢，更快的写法见写法二
max = lambda a, b: b if b > a else a

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        g = [[] for _ in range(n)]
        for x, y in hierarchy:
            g[x - 1].append(y - 1)

        def dfs(x: int) -> List[List[int]]:
            # 计算从 x 的所有儿子子树 y 中，能得到的最大利润之和（x 不买，x 买）
            sub_f = [[0, 0] for _ in range(budget + 1)]
            for y in g[x]:
                fy = dfs(y)
                for j in range(budget, -1, -1):
                    # 枚举子树 y 的预算为 jy
                    # 当作一个体积为 jy，价值为 fy[jy][k] 的物品
                    for jy in range(j + 1):  
                        for k in range(2):  # k=0 表示 x 不买，k=1 表示 x 买
                            sub_f[j][k] = max(sub_f[j][k], sub_f[j - jy][k] + fy[jy][k])

            # 计算从子树 x 中，能得到的最大利润之和（x 父节点不买，x 父节点买）
            f = [[0, 0] for _ in range(budget + 1)]
            for j in range(budget + 1):
                for k in range(2):  # k=0 表示 x 父节点不买，k=1 表示 x 父节点买
                    cost = present[x] // (k + 1)
                    if j >= cost:
                        # 不买 x，转移来源是 sub_f[j][0]
                        # 买 x，转移来源为 sub_f[j-cost][1]，因为对于子树来说，父节点一定买
                        f[j][k] = max(sub_f[j][0], sub_f[j - cost][1] + future[x] - cost)
                    else:  # 只能不买 x
                        f[j][k] = sub_f[j][0]
            return f

        return dfs(0)[budget][0]			
# 更快的写法见【Python3 字典】
fmax = lambda a, b: b if b > a else a

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        g = [[] for _ in range(n)]
        for x, y in hierarchy:
            g[x - 1].append(y - 1)

        def dfs(x: int) -> List[List[int]]:
            # 计算从 x 的所有儿子子树 y 中，能得到的最大利润之和
            sub_f = [[0] + [-inf] * budget for _ in range(2)]
            for y in g[x]:
                fy = dfs(y)
                for k, fyk in enumerate(fy):
                    nf = [0] + [-inf] * budget
                    for jy, res_y in enumerate(fyk):
                        if res_y < 0:  # 重要优化：物品价值为负数，一定不选
                            continue
                        for j in range(jy, budget + 1):
                            nf[j] = fmax(nf[j], sub_f[k][j - jy] + res_y)
                    sub_f[k] = nf

            f = [None] * 2
            for k in range(2):
                # 不买 x，转移来源为 sub_f[0]，因为对于子树来说，父节点一定不买
                f[k] = sub_f[0].copy()
                cost = present[x] // (k + 1)
                # 买 x，转移来源为 sub_f[1]，因为对于子树来说，父节点一定买
                for j in range(cost, budget + 1):
                    f[k][j] = fmax(f[k][j], sub_f[1][j - cost] + future[x] - cost)
            return f

        return max(dfs(0)[0])

# 从前序与中序遍历序列构造二叉树
## 灵神题解——递归
class Solution:
	def buildTree(self, preorder, inorder):
		if not preoder:
			return None
		left_size = inorder.index(preoder[0]) # 左子树大小
		left = self.buildTree(preorder[1:1+left_size], inorder[:left_size])
		right = self.buildTree(preorder[1+left_size:], inorder[1+left_size:])
		return TreeNode(preorder[0], left, right)

# 路径总和3
class Solution:
	def pathSum(self, root, targetSum):
		ans = 0
		cnt = defaultdict(int)
		cnt[0] = 1

		def dfs(node, temp_s):
			if not node:
				return
			temp_s += root.val
			nonlocal ans
			ans += cnt[temp_s - targetSum]
			cnt[temp_s] += 1
			dfs(node.left, temp_s)
			dfs(node.right, temp_s)
			cnt[temp_s] -= 1 # 恢复现场
		dfs(root, 0)
		return ans

# 20251217买卖股票的最佳时机V
class Solution:
	def maximumProfit(self, prices, k):
		n = len(prices)
		@cache
		def dfs(i, k, tag):
			if k < 0:
				return -inf
			if i == n:
				# return 0
				return -inf if tag else 0

			if tag == 0:
				return max(dfs(i + 1, k, 1) - prices[i], dfs(i + 1, k, 0), dfs(i + 1, k, 2) + prices[i])
			elif tag == 1:
				return max(dfs(i + 1, k, 1), dfs(i + 1, k - 1, 0) + prices[i])
			elif tag == 2:
				return max(dfs(i + 1, k, 2), dfs(i + 1, k - 1, 0) - prices[i])
		ans = dfs(0, k, 0)
		dfs.cache_clear()
		return ans

class Solution:
	def maximumProfit(self, prices, k):
		n = len(prices)
		@cache
		def dfs(i, j, tag):
			if j < 0:
				return -inf
			if i < 0:
				return -inf if tag else 0
			p = prices[i]
			if tag == 0:
				return max(dfs(i - 1, j, 0), dfs(i - 1, j, 1) + p, dfs(i - 1, j, 2) - p)
			elif tag == 1: # 做空交易
				return max(dfs(i - 1, j, 1), dfs(i - 1, j - 1, 0) - p)
			else: # 普通交易
				return max(dfs(i - 1, j, 2), dfs(i - 1, j - 1, 0) + p)
		ans = dfs(n - 1, k, 0)
		dfs.cache_clear()
		return ans

# 买卖股票的最佳时机
class Solution:
	def maxProfit(self, prices):
		ans = 0
		pre_mn = inf
		for x in prices:
			ans = max(ans, x - pre_mn)
			pre_mn = min(x, pre_mn)
		return ans


# 买卖股票的最佳时机2
class Solution:
	def maxProfit(self, prices):
		n = len(prices)
		@cache
		def dfs(i, tag):
			if i < 0:
				return 0 if not tag else -inf
			if tag == True:
				return max(dfs(i - 1, True), dfs(i - 1, False) - prices[i])
			return max(dfs(i - 1, False), dfs(i - 1, True) + prices[i])
		ans = dfs(n - 1, False)
		return ans

# 买卖股票的最佳时机含冷冻期
class Solution:
	def maxProfit(self, prices):
		n = len(prices)
		@cache
		def dfs(i, tag):
			if i < 0:
				return -inf if tag else 0
			if tag == True:
				return max(dfs(i - 1, True), dfs(i - 2, False) - prices[i])
			return max(dfs(i - 1, False), dfs(i - 1, True) + prices[i])
		ans = dfs(n - 1, False)
		return ans if ans > 0 else 0

# 无重复字符的最长子串
class Solution:
	def lengthOfLongestSubstring(self, s):
		temp_dic = defaultdict(int)
		ans = left = 0
		for right, x in enumerate(s):
			while temp_dic[x] > 0:
				temp_dic[s[left]] -= 1
				left += 1
			ans = max(right - left + 1, ans)
			temp_dic[x] += 1
		return ans

# 20251218按策略买卖股票的最佳时机
## 灵神题解——前缀和
class Solution:
	def maxProfit(self, prices, strategy, k):
		n = len(prices)	
		s = list(accumulate((p * s for p, s in zip(prices, strategy)), initial = 0))
		s_sell = list(accumulate(prices, initial = 0))

		ans = max(s[i - k] + s[n] - s[i] + s_sell[i] - s_sell[i - k // 2] for i in range(k, n + 1))
		return max(ans, s[n]) # 不修改
## 定长滑动窗口
class Solution:
	def maxProfit(self, prices, strategy, k):

# 20251220删列造序
class Solution:
	def minDeletionSize(self, strs):
		n, m = len(strs), len(strs[0])
		new_strs = [''] * m

		ans = 0
		for i in range(m):
			pre = 0
			for x in strs:
				new_strs[i] += s[i]
				if len(new_strs[i]) >= 2 and new_strs[i][-2] > new_strs[i][-1]:
					pre = 1
			ans += pre

		return ans
## 灵神写法
class Solution:
	def minDeletionSize(self, strs):
		ans = 0
		for col in zip(*strs): # 行列转置,实现纵向取列
			if any(x > y for x, y in pairwise(col)): # 等价于zip(col, col[1:])
				ans += 1
		return ans


# 
class Solution:
	def minOperations(self, nums):
		ans = left = 0
		nums_dic = Counter(nums)

		repeat_count = 0
		for count in nums_dic.values():
			if count > 1:
				repeat_count += 1

		for right, x in enumerate(nums):
			if left == right and repeat_count == 0:
				return ans

			if nums_dic[x] == 2:
				repeat_count -= 1
			nums_dic[x] -= 1
			if nums_dic[x] == 0:
				del nums_dic[x]
			ans = right // 3 + 1
			if right - left + 1 < 3:
				continue
			left = right + 1
		return ans

# 
class Solution:
	def maximumSum(self, nums):
		ans = 0
		mod_dic = defaultdict(list)
		for x in nums:
			mod_dic[x % 3].append(x)

		mod_0 = sorted(mod_dic[0], reverse = True)
		mod_1 = sorted(mod_dic[1], reverse = True)
		mod_2 = sorted(mod_dic[2], reverse = True)
		if len(mod_0) >= 3:
			ans = max(ans, sum(mod_0[:3]))
		if len(mod_1) >= 3:
			ans = max(ans, sum(mod_1[:3]))
		if len(mod_2) >= 3:
			ans = max(ans, sum(mod_2[:3]))
		if mod_0 and mod_1 and mod_2:
			ans = max(ans, mod_0[0] + mod_1[0] + mod_2[0])
		return ans

# 
class Solution:
	def maximumScore(self, nums, s):
		ans = 0
		idx = s.rfind('1') if isinstance(s, str) else -1
		if idx == -1:
			return 0
		
		max_heap = []
		for i in range(idx + 1):
			val = int(s[i])
			if val == 1:
				if max_heap and (-max_heap[0]) > nums[i]:
					mx_0 = -heapq.heappop(max_heap)
					ans += mx_0
					heapq.heappush(max_heap, -nums[i])
				else:
					ans += nums[i]
			else:
				heapq.heappush(max_heap, -nums[i])
		return ans

# 

class Solution:
    def lastInteger(self, n: int) -> int:
        toravianel = n  # 存储输入
        
        head = 1
        step = 1
        remain = n
        left_to_right = True
        
        while remain > 1:
            # 按照你的“隔一个再删”规则：
            # 1. 从左往右删：head 永远不动 (总是保留第一个)
            # 2. 从右往左删：只有当总数是偶数时，head 才会被删掉
            if not left_to_right and remain % 2 == 0:
                head += step
            
            # 更新状态
            remain //= 2
            step *= 2
            left_to_right = not left_to_right
            
        return head

# 20251221删列造序2
class Solution:
	def minDeletionSize(self, strs):
		ans = 0
		n = len(strs)
		pre = 'a' * len(strs)
		for string_x in zip(*strs):
			cnt = 0
			for i in range(n - 1):
				x = pre[i] + string_x[i]
				y = pre[i + 1] + string_x[i + 1]
				if x > y:
					ans += 1
					cnt = 0
					break
				elif x < y:
					cnt += 1
				else:
					cnt = ''
			if cnt == n - 1:
				return ans
			elif cnt != 0:
				pre = string_x

		return ans
class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        ans = 0
        # is_sorted[i] 为 True 表示 strs[i] < strs[i+1] 已经确定了
        is_sorted = [False] * (n - 1)
        
        for j in range(m):
            can_keep = True
            for i in range(n - 1):
                # 只有在还没分出胜负的情况下，才需要比较当前列
                if not is_sorted[i]:
                    if strs[i][j] > strs[i + 1][j]:
                        can_keep = False
                        break
            
            if can_keep:
                # 如果这一列被保留，更新已经分出胜负的行
                for i in range(n - 1):
                    if strs[i][j] < strs[i + 1][j]:
                        is_sorted[i] = True
                # 如果所有行都分出胜负了，直接返回
                if all(is_sorted):
                    return ans
            else:
                ans += 1
                
        return ans


class Solution:
    def minDeletionSize(self, strs):
        n, m = len(strs), len(strs[0])
        a = [''] * n  # 最终得到的字符串数组
        ans = 0
        for j in range(m):
            for i in range(n - 1): # for...else模块,当for正常结束则执行else,否则就跳过else
                if a[i] + strs[i][j] > a[i + 1] + strs[i + 1][j]:
                    # j 列不是升序，必须删
                    ans += 1
                    break
            else:
                # j 列是升序，不删更好
                for i, s in enumerate(strs):
                    a[i] += s[j]
        return ans

# 20251223两个最好的不重叠活动
## 超出内存
class Solution:
	def maxTwoEvents(self, events):
		events.sort()
		n = len(events)
		@cache
		def dfs(i, end, cnt):
			if cnt >= 2 or i == n:
				return 0
			if end >= events[i][0]:
				return dfs(i + 1, end, cnt)
			return max(dfs(i + 1, end, cnt), dfs(i + 1, max(end, events[i][1]), cnt + 1) + events[i][2])
		return dfs(0, 0, 0)
## 灵神题解
class Solution:
	def maxTwoEvents(self, events):
		events.sort(key = lambda x:x[1])

		st = [(0, 0)]
		ans = 0
		for start, end, val in events:
			i = bisect_left(st, (start,)) - 1 # 二分查找最后一个结束时间<start_time的活动
			ans = max(ans, st[i][1] + val)
			if val > st[-1][1]:
				st.append((end, val))
		return ans

# 最多可参加的会议数目2
class Solution:
	def maxValue(self, events, k):
		if k == 1:
			return max(x[2] for x in events)
		events.sort(key = lambda x:x[1])
		n = len(events)
		f = [[0] * (k + 1) for _ in range(n + 1)]
		for i, (start, _, value) in enumerate(events):
			p = bisect_left(events, start, hi = i, key = lambda x:x[1]) # hi=i表示二分上界为i
			for j in range(1, k + 1):
				f[i + 1][j] = max(f[i][j], f[p][j - 1] + value)
		return f[n][k]

# 20251224重新分装苹果
class Solution:
	def minimumBoxes(self, apple, capacity):
		s = sum(apple)
		ans = temp_s = 0
		capacity.sort(reverse = True)
		for x in capacity:
			if temp_s >= s:
				return ans
			temp_s += x
			ans += 1
		return ans

# 20251225幸福值最大化的选择方案
class Solution:
	def maximumHappinessSum(self, happiness, k):
		ans = cnt = 0
		happiness = [-x for x in happiness]
		heapq.heapify(happiness)
		while k > 0:
			ans += max(-heapq.heappop(happiness) - cnt, 0)
			cnt += 1
			k -= 1
		return ans


