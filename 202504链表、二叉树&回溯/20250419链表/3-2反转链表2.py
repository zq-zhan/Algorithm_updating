class ListNode:
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next


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
	
if __name__ == '__main__':
	head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
	left = 2
	right = 4
	print(Solution2().reverseBetween(head, left, right))
	