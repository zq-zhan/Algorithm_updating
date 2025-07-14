class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def reverseEvenLengthGroups(self, head):
		n = 0
		cur = head
		while cur:
			cur = cur.next
			n += 1

		k = 1
		p0 = dummy = ListNode(next = head)
		pre = p0
		cur = p0.next
		while n > 0:
			target = min(n, k)
			n -= k
			k += 1
			if target % 2:
				for _ in range(target):
					cur = cur.next
					p0 = p0.next
			else:
				for _ in range(target):
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
	head = ListNode(5, ListNode(2, ListNode(6, ListNode(3, ListNode(9, ListNode(1, ListNode(7, ListNode(3, ListNode(8, ListNode(4))))))))))
	print(Solution().reverseEvenLengthGroups(head))