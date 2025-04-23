class ListNode:
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next

# 1.反转链表
class Solution1:
	def reverseList(self, head):
		pre = None
		cur = head
		while cur:
			nxt = cur.next
			cur.next = pre
			pre = cur
			cur = nxt
		return pre
	
if __name__ == '__main__':
	head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
	print(Solution1().reverseList(head))