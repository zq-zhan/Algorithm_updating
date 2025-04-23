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

