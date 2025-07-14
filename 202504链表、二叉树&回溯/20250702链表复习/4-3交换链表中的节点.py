class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def swapNodes(self, head, k):
		dummy = ListNode(next = head)
		right = dummy
		for _ in range(k):
			right = right.next
		temp_node = right
		left = dummy
		while right.next:
			right = right.next
			left = left.next
		temp_node.val, left.next.val = left.next.val, temp_node.val
		return dummy.next
	
if __name__ == '__main__':
	head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
	k = 2
	print(Solution().swapNodes(head, k))