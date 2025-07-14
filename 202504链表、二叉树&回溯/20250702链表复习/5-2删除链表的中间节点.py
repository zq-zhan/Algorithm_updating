class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def deleteMiddle(self, head):
		dummy = ListNode(next = head)
		slow = dummy
		fast = dummy.next
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
		slow.next = slow.next.next
		return dummy.next
	
if __name__ == '__main__':
	head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
	print(Solution().deleteMiddle(head))