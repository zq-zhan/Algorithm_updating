class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

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

if __name__ == '__main__':
	head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8))))))))
	print(Solution().oddEvenList(head))