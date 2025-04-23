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