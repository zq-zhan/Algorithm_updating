class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

# class Solution:
# 	def rotateRight(self, head, k):
# 		n = 0
# 		cur = head
# 		while cur:
# 			n += 1
# 			cur = cur.next

# 		p0 = dummy = ListNode(next = head)
# 		right = dummy
# 		for _ in range(n - k):
# 			right = right.next

# 		nxt = p0.next
# 		p0.next = right.next
# 		right.next = None
# 		for _ in range(k):
# 			p0 = p0.next
# 		p0.next = nxt
# 		return dummy.next
	
## 题解：题意等价于将链表后k % n个节点一道链表最前面
class Solution:
	def rotateRight(self, head, k):
		n = 0
		cur = head
		while cur:
			n += 1
			cur = cur.next

		k = k % n
		p0 = dummy = ListNode(next = head)
		right = dummy
		for _ in range(n - k):
			right = right.next

		nxt = p0.next
		p0.next = right.next
		while p0.next:
			p0 = p0.next
		p0.next = nxt
		right.next = None
		return dummy.next

## 快慢指针解法
class Solution:
	def rotateRight(self, head, k):
		if not head or not head.next:
			return head
		n = 0
		cur = head
		while cur:
			n += 1
			cur = cur.next

		k = k % n
		if k == 0:
			return head
			
		p0 = dummy = ListNode(next = head)
		right = dummy
		for _ in range(k):
			right = right.next
		left = dummy
		while right.next:
			left = left.next
			right = right.next

		nxt = p0.next
		p0.next = left.next
		right.next = nxt
		left.next = None
		return dummy.next


if __name__ == '__main__':
	head = ListNode(1, ListNode(2))
	k = 2
	print(Solution().rotateRight(head, k))