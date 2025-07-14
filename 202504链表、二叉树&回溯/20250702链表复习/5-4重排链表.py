class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
		

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

	
if __name__ == '__main__':
	head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
	print(Solution().reorderList(head))