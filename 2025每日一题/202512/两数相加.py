class ListNode:
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next

class Solution:
	def addTwoNumbers(self, l1, l2):
		p = dummy = ListNode()
		x = 0
		while l1 or l2:
			if l1 is None:
				l1 = ListNode(0)
			if l2 is None:
				l2 = ListNode(0)
			x = x // 10 + l1.val + l2.val
			p.next = ListNode(x % 10)
			l1 = l1.next
			l2 = l2.next
			p = p.next
		if x // 10:
			p.next = ListNode(x // 10)
		return dummy.next
## 迭代写法2
class Solution:
	def addTwoNumbers(self, l1, l2):
		p = dummy = ListNode()
		carry = 0
		while l1 or l2 or carry:
			if l1:
				carry += l1.val
				l1 = l1.next
			if l2:
				carry += l2.val
				l2 = l2.next
			p.next = ListNode(carry % 10)
			carry //= 10
			p = p.next
		return dummy.next
## 灵神题解——递归
class Solution:
	def addTwoNumbers(self, l1, l2, carry = 0):
		if l1 is None and l2 is None and carry == 0:
			return None

		s = carry
		if l1:
			s += l1.val
			l1 = l1.next
		if l2:
			s += l2.val
			l2 = l2.next
		return ListNode(s % 10, self.addTwoNumbers(l1, l2, s // 10))




if __name__ == '__main__':
	l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))))
	l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
	print(Solution().addTwoNumbers(l1, l2))