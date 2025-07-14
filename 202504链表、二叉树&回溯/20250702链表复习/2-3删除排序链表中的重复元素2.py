class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def deleteDuplicates(self, head):
		dummy = ListNode(next = head)
		cur = dummy
		while cur.next and cur.next.next:
			val = cur.next.val
			if cur.next.next.val == val:
				while cur.next and cur.next.val == val:
					cur.next = cur.next.next
			else:
				cur = cur.next
		return dummy.next


	
if __name__ == '__main__':
	head = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(4)))))))
	print(Solution().deleteDuplicates(head))