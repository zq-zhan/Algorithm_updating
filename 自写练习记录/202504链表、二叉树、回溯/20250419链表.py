# 1.二进制链表转整数
class Solution1:
	def getDecimalValue(self, head):
		ans = ''
		while head.val:
			ans += head.val
			head = head.next
		return int(ans, 2)

# 2.找出临界点之间的最小和最大距离
class Solution1:
	def nodesBetweenCriticalPoints(self, head):
		distance_lis = []
		mindistance = inf
		# maxdistance = 0
		cnt = 0
		while head:
			if cnt >= 1 and head.next:
				if (head.val > pre and head.val > head.next.val) or \
					(head.val < pre and head.val < head.next.val):
					distance_lis.append(cnt)
					if len(distance_lis) >= 2:
						mindistance = min(mindistance, distance_lis[-1] - distance_lis[-2])
						# maxdistance = max(maxdistance, distance_lis[-1] - distance_lis[0])
			cnt += 1
			pre = head.val
			head = head.next
		# return [mindistance, maxdistance] if maxdistance > 0 else [-1, -1]
		return [mindistance, distance_lis[-1] - distance_lis[0]] if mindistance < inf else [-1, -1]

# 3.合并零之间的节点
class Solution1:
	def mergeNodes(self, head):
		ans = ListNode(None)
		current = ans
		head = head.next
		temp_sum = 0
		while head:
			temp_sum += head.val
			if head.val == 0:
				# if ans is not None:
				# 	ans = ListNode(temp_sum)
				# else:
				# 	ans.next = ListNode(temp_sum)
				current.next = ListNode(temp_sum)
				current = current.next
				temp_sum = 0
			head = head.next
		return ans.next
## 在原节点基础上修改
class Solution2:
	def mergeNodes(self, head):
		q = head.next
		while q:
			if q.next.val == 0:
				q.next = q.next.next
				q = q.next
			else:
				q.val += q.next.val
				q.next = q.next.next
		return head.next

# 4.分隔链表
class Solution1:
	def splitListToParts(self, head, k):
		ans = []
		while head:
			ans.append(head.val)
			head = head.next
		result = []
		ori = 0
		n = len(ans)
		if n <= k:
			for x in ans:
				result.append([x])
			for _ in range(k - n):
				result.append([])
			return result

		mod = n % k
		cnt = n // k
		while ori <= n - 1:
			length = ori + cnt + int(mod >= 1)
			result.append(ans[ori:length])
			ori = length 
			mod -= 1
		return result
class Solution2:
	def splitListToParts(self, head, k):
		ans = []
		while head:
			ans.append(head.val)
			head = head.next
		result = ListNode(None)
		current = result
		ori = 0
		n = len(ans)
		if n <= k:
			for x in ans:
				current.next = ListNode(x)
				current = current.next
			for _ in range(k - n):
				current.next = ListNode(None)
				current = current.next
			return result
		mod = n % k
		cnt = n // k
		while ori <= n - 1:
			length = ori + cnt + int(mod >= 1)	
			current.next = ListNode(ans[ori:length])
			current = current.next()
			ori = length
			mod -= 1
		return result.next

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
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head, k):
        #计算链表长度
        cnt, length = head, 0
        while cnt:
            cnt = cnt.next
            length+=1

        #每部分长度
        part_length =  length // k

        #前 remainder 部分需要额外加一个节点
        remainder = length % k         
        res = []
        cur = head 
        for i in range(k):
            part_head= cur 

            cur_part_length =  part_length 

            #前 remainder 部分需要额外加一个节点
            if remainder:
                cur_part_length+=1
                remainder-=1
            #不为空时, 遍历添加当前部分的节点
            for j in range(cur_part_length - 1):
                if cur:
                    cur = cur.next

            #如果后续还有节点则断开链接
            if cur:
                next_part = cur.next
                cur.next = None
                cur = next_part
            res.append(part_head)
        return res

# 5.链表组件
# class Solution1:
# 	def numComponents(self, head, nums):
# 		ans = temp_ans = result = 0
# 		while head:
# 			if head.val in nums:
# 				temp_ans += 1
# 			else:
# 				temp_ans = 0
# 			if temp_ans > ans:
# 				result = 1
# 			elif temp_ans == ans:
# 				result += 1
# 			ans = max(ans, temp_ans)
# 			head = head.next
# 		return reslut

class Solution1:
	def numComponents(self, head, nums):
		nums = set(nums)
		ans = cnt = 0
		while head:
			if head.val in nums:
				cnt += 1
			else:
				ans += 1 if cnt > 0 else 0
				cnt = 0
			head = head.next
		return ans + 1 if cnt > 0 else ans
## 优化
class Solution1:
	def numComponents(self, head, nums):
		nums = set(nums)
		p = head
		inSet = False
		ans = 0
		while p:
			if p.val in nums:
				if not inSet:
					inSet = True
					ans += 1
			else:
				inSet = False
			p = p.next
		return ans

####################### 删除节点 ######################
# 1.移除链表元素
class Solution1:
	def removeElements(self, head, val):
		dummy = ListNode(next = head)
		cur = dummy
		while cur.next:
			if cur.next.val == val:
				cur.next = cur.next.next
			else:
				cur = cur.next
		return dummy.next

# 2.删除链表中的节点
class Solution1:
	def deleteNode(self, node):
		node.val = node.next.val
		node.next = node.next.next

# 3.删除链表的倒数第N个节点
class Solution1:
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

# 4.删除排序链表中的重复元素
class Solution1:
	def deleteDuplicates(self, head):
		if not head:
			return head
		cur = head
		while cur.next:
			if cur.val == cur.next.val:
				cur.next = cur.next.next
			else:
				cur = cur.next
		return head
# 5.删除排序链表中的重复元素2
class Solution1:
	def deleteDuplicates(self, head):
		cur = dummy = ListNode(next = head)
		while cur.next and cur.next.next:
			val = cur.next.val
			if val == cur.next.next.val:
				while cur.next and cur.next.val == val:
					cur.next = cur.next.next
			else:
				cur = cur.next
		return dummy.next

# 6.从链表中移除在数组中存在的节点
class Solution1:
	def modifiedList(self, nums, head):
		nums = set(nums)
		cur = dummy = ListNode(next = head)
		while cur.next:
			if cur.next.val in nums:  # 判断的复杂度是O(1)
				cur.next = cur.next.next
			else:
				cur = cur.next
		return dummy.next

# 7.合并两个链表
class Solution1:
	def mergeInBetween(self, list1, a, b, list2):
		dummy = ListNode(next = list1)
		right = dummy
		for _ in range(b - a + 1):
			right = right.next
		left = dummy
		for _ in range(a):
			left = left.next
			right = right.next
		left.next = list2
		cur = list2
		while cur.next:
			cur = cur.next
		cur.next = right.next
		return dummy.next
## 简洁写
class Solution1:
	def mergeInBetween(self, list1, a, b, list2):
		dummy = ListNode(next = list1)
		right = dummy
		for _ in range(b + 1):
			right = right.next
		left = dummy
		for _ in range(a):
			left = left.next
		left.next = list2
		cur = list2
		while cur.next:
			cur = cur.next
		cur.next = right.next
		return dummy.next

# 8.从链表中移除节点
# class Solution1:  贪心思路是错解
# 	def removeNodes(self, head):
# 		max_node = 1
# 		cur = head
# 		while cur:
# 			max_node = max(max_node, cur.val)
# 			cur = cur.next
# 		cur = dummy = ListNode(next = head)
# 		while cur.next.next:
# 			if cur.next.val < max_node:
# 				cur.next = cur.next.next
# 			else:
# 				cur = cur.next
# 		return dummy.next
class Solution2:
	def removeNodes(self, head):
		head_node = []
		cur = head
		while cur:
			head_node.append(cur.val)
			cur = cur.next

		n = len(head_node)
		for i in range(n - 2, -1, -1):
			head_node[i] = max(head_node[i], head_node[i + 1])

		cnt = 0
		cur = dummy = ListNode(next = head)
		while cur.next.next:
			if cur.next.val < head_node[cnt]:
				cur.next = cur.next.next
			else:
				cur = cur.next
			cnt += 1
		return dummy.next


############## 反转链表 #########
# 1.反转链表
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

class Solution2:
	def reverseList(self, head):
		p0 = dummy = ListNode(next = head)
		pre = None
		cur = p0.next
		while cur:
			nxt = cur.next
			cur.next = pre
			pre = cur
			cur = nxt
		p0.next = pre
		return dummy.next



# 2.反转链表2
class Solution2:
	def reverseBetween(self, head, left, right):
		p0 = dummy = ListNode(next = head)
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

# 3.两两交换链表中的节点
class Solution1:
	def swapPairs(self, head):
		n = 0
		cur = head
		while cur:
			n += 1
			cur = cur.next

		dummy = ListNode(next = head)
		p0 = dummy
		pre = None
		cur = p0.next
		while n >= 2:
			n -= 2
			# pre = None
			# cur = p0.next
			for _ in range(2):
				nxt = cur.next
				cur.next = pre
				pre = cur
				cur = nxt

			nxt = p0.next  # 1
			p0.next.next = cur # 3
			p0.next = pre  # 2
			p0 = nxt  # 1 此时为3的上一个节点
		return dummy.next

# 4.K个一组翻转链表
class Solution1:
	def reverseKGroup(self, head, k):
		n = 0
		cur = head
		while cur:
			n += 1
			cur = cur.next

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

# 5.反转偶数长度组的节点
class Solution1:
	def reverseEvenLengthGroups(self, head):
		n = 0
		cur = head
		while cur:
			cur = cur.next
			n += 1

		p0 = dummy = ListNode(next = head)
		pre = None
		cur = p0.next
		cnt = 1
		while n >= cnt:
			n -= cnt
			if cnt % 2 != 0:
				for _ in range(cnt):
					p0 = p0.next
					cur = p0.next
			else:
				for _ in range(cnt):
					nxt = cur.next
					cur.next = pre
					pre = cur
					cur = nxt

				nxt = p0.next
				p0.next.next = cur
				p0.next = pre
				p0 = nxt
			cnt += 1
		if n >= 2 and n % 2 == 0:
			for _ in range(n):
				nxt = cur.next
				cur.next = pre
				pre = cur
				cur = nxt
			p0.next.next = cur
			p0.next = pre
		return dummy.next

################## 插入节点 ################
# 1.在链表中插入最大公约数
class Solution1:
	def insertGreatestCommonDivisors(self, head):
		def find_mx(a, b):
			mn = min(a, b)
			for x in range(mn, 0, -1):
				if a % x == 0 and b % x == 0:
					return x
			return 1

		cur = head
		while cur.next:
			node_val = find_mx(cur.val, cur.next.val)
			# insert = ListNode(node_val)
			# nxt = cur.next  # 10
			# cur.next = insert  # 6
			# cur.next.next = nxt  # 10
			# cur = nxt
			nxt = cur.next
			cur.next = ListNode(node_val, next = cur.next)
			cur = nxt
		return head
## 灵神写法
class Solution1:
	def insertGreatestCommonDivisors(self, head):
		cur = head
		while cur.next:
			cur.next = ListNode(gcd(cur.val, cur.next.val), next = cur.next)
			cur = cur.next.next
		return head

# 2.对链表进行插入排序
class Solution1:  # 错解
	def insertionSortList(self, head):
		p0 = dummy = ListNode(next = head)
		cur = p0.next
		pre = None
		while cur:
			while cur.next.val < cur.val:
				nxt = cur.next
				cur.next = pre
				pre = cur
				cur = nxt
			p0.next.next = cur
			cur = cur.next
		return dummy.next
##
class Solution1:
	def insertionSortList(self, head):
		dummy = ListNode(-inf)
		pre = dummy
		tail = dummy
		cur = head:
		while cur:
			if tail.val < cur.val:
				tail.next = cur
				tail = cur
				cur = cur.next
			else:
				tmp = cur.next
				tail.next = tmp
				while pre.next and pre.next.val < cur.val:
					pre = pre.next
				cur.next = pre.next
				pre.next = cur
				pre = dummy
				cur = tmp
		return dummy.next

class Solution2:
    def insertionSortList(self, head):
     	# 找个排头
        dummy = ListNode(-1)
        pre = dummy
        # 依次拿head节点
        cur = head
        while cur:
        	# 把下一次节点保持下来
            tmp = cur.next
            # 找到插入的位置（最后一个小于当前节点的节点）
            while pre.next and pre.next.val < cur.val:
                pre = pre.next
            # 进行插入操作
            cur.next = pre.next  # 此时pre.next的值是第一个大于cur的值的节点，这就是cur要插入的位置
            pre.next = cur  # pre的值小于cur的值，所以pre.next指向cur
            pre = dummy  # 重新初始化pre，因为后续要重新查找插入的位置
            cur = tmp  #依次遍历head的所有节点
        return dummy.next
## 写法三
class Solution3:
	def insertionSortList(self, head):
		if not head or not head.next:
			return head
		cur, nxt = head, head.next
		dummy = ListNode(-inf)
		dummy.next = head
		while nxt:
			if nxt.val >= cur.val:
				cur = nxt
				nxt = nxt.next
			else:
				cur.next = nxt.next
				pre1, pre2 = dummy, dummy.next
				while nxt.val > pre2.val:
					pre1 = pre2
					pre2 = pre2.next
				pre1.next = nxt
				nxt.next = pre2
				nxt = cur.next
		return dummy.next
