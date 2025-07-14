class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def swapPairs(self, head):
		dummy = ListNode(next = head)
		p0 = dummy
		pre = None
		cur = p0.next
		while cur and cur.next:
			for _ in range(2):
				nxt = cur.next
				cur.next = pre
				pre = cur
				cur = nxt
			nxt = p0.next
			p0.next.next = cur
			p0.next = pre
			p0 = nxt
		return dummy.next
	
if __name__ == '__main__':
	head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
	s = Solution()
	print(s.swapPairs(head))