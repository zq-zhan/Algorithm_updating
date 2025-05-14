class ListNode:
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next

# 2.对链表进行插入排序
class Solution1:
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
		cur = head
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


if __name__ == '__main__':
	head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
	s = Solution2()
	print(s.insertionSortList(head).toList())