class ListNode:
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next

# 1.移除链表元素
class Solution1:
	def removeElements(self, head, val):
		p = ListNode(val)
		p.next = head
		while p.next:
			if p.next.val == val:
				p.next = p.next.next
			else:
				p = p.next
		return p.next
	
class Solution2:
	def removeElements(self, head, val):
		dummy = ListNode(next = head)
		cur = dummy
		while cur.next:
			if cur.next.val == val:
				cur.next = cur.next.next
			else:
				cur = cur.next
		return dummy.next


if __name__ == '__main__':
	# head = ListNode(1, ListNode(2, ListNode(6, ListNode(6, ListNode(4, ListNode(5, ListNode(6)))))))
	# val = 6
	head = ListNode(7, ListNode(7, ListNode(7, ListNode(7))))
	val = 7
	print(Solution1().removeElements(head, val))