class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def deleteNode(self, head, node):
		cur = head
		while cur.next:
			if cur.next.val == node:
				cur.next = cur.next.next
				break
			else:
				cur = cur.next
		return head
	
if __name__ == '__main__':
	head = ListNode(4, ListNode(5, ListNode(1, ListNode(9))))
	node = 5
	print(Solution().deleteNode(head, node))