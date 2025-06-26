class ListNode:
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next


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
	
if __name__ == '__main__':
	head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
	k = 2
	print(Solution1().reverseKGroup(head, k))