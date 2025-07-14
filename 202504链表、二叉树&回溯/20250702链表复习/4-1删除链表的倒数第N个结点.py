class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def removeNthFromEnd(self, head, n):
		dummy = ListNode(next = head)
		right = dummy.next
		for _ in range(n):
			right = right.next

		left = dummy
		while right:
			left = left.next
			right = right.next
		left.next = left.next.next
		return dummy.next
	
if __name__ == '__main__':
	head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
	n = 2
	print(Solution().removeNthFromEnd(head, n))