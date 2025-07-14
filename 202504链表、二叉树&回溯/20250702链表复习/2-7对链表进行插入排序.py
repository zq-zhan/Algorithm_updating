class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def insertionSortList(self, head):
		dummy = ListNode(next = head)
		left = dummy
		right = left.next
		while right.next:
			if right.next.val < right.val:
				temp = right.next.next
				cur = left.next
				left.next = right.next
				left.next.next = cur
				right.next = temp
		return dummy.next
## 灵神题解
class Solution:
	def insertionSortList(self, head):
		dummy = ListNode(0)
		cur = head
		while cur:
			next_node = cur.next
			pre = dummy
			while pre.next and pre.next.val < cur.val:
				pre = pre.next
			cur.next = pre.next
			pre.next = cur
			cur = next_node
		return dummy.next

	

if __name__ == '__main__':
	head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
	print(Solution().insertionSortList(head))