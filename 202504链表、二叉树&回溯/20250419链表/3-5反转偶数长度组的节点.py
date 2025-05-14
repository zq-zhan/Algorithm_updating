class ListNode:
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next

class Solution1:
	def reverseEvenLengthGroups(self, head):
		n = 0
		cur = head
		while cur:
			cur = cur.next
			n += 1

		p0 = dummy = ListNode(next = head)
		pre = None
		cur = p0.next
		cnt = 1
		while n >= cnt:
			n -= cnt
			if cnt % 2 != 0:
				for _ in range(cnt):
					p0 = p0.next
					cur = p0.next
			else:
				for _ in range(cnt):
					nxt = cur.next
					cur.next = pre
					pre = cur
					cur = nxt

				nxt = p0.next
				p0.next.next = cur
				p0.next = pre
				p0 = nxt
			cnt += 1
		if n >= 2 and n % 2 == 0:
			for _ in range(n):
				nxt = cur.next
				cur.next = pre
				pre = cur
				cur = nxt
			p0.next.next = cur
			p0.next = pre
		return dummy.next
	
if __name__ == '__main__':
	head = ListNode(5, ListNode(2, ListNode(6, ListNode(3, ListNode(9, ListNode(1, ListNode(7, ListNode(3, ListNode(8, ListNode(4))))))))))
	print(Solution1().reverseEvenLengthGroups(head))