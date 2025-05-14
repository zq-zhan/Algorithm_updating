class ListNode:
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next


class Solution1:
	def swapPairs(self, head):
		n = 0
		cur = head
		while cur:
			n += 1
			cur = cur.next

		dummy = ListNode(next = head)
		p0 = dummy
		pre = None
		cur = p0.next
		while n >= 2:
			n -= 2
			# pre = None
			# cur = p0.next
			for _ in range(2):
				nxt = cur.next
				cur.next = pre
				pre = cur
				cur = nxt

			nxt = p0.next  # 1
			p0.next.next = cur # 3
			p0.next = pre  # 2
			p0 = nxt  # 1 此时为3的上一个节点
		return dummy.next
	
if __name__ == '__main__':
	head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
	print(Solution1().swapPairs(head))