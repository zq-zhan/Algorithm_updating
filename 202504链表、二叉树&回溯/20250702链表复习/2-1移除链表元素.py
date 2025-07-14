class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def removeElements(self, head, val):
		temp_node = ListNode(None)
		temp_node.next = head
		cur = temp_node
		while cur.next:
			if cur.next.val == val:
				cur.next = cur.next.next
				continue
			cur = cur.next
		return temp_node.next
	
if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
    # head = ListNode(7, ListNode(7, ListNode(7, ListNode(7))))
    val = 6
    print(Solution().removeElements(head, val))