class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def partition(self, head, x):
		p1 = cur1 = ListNode(0)
		p2 = cur2 = ListNode(1)
		while head:
			if head.val < x:
				cur1.next = head
				cur1 = cur1.next
			else:
				cur2.next = head
				cur2 = cur2.next
			head = head.next
		cur2.next = None
		cur1.next = p2.next
		return p1.next
	
if __name__ == '__main__':
	head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
	x = 3
	print(Solution().partition(head, x))