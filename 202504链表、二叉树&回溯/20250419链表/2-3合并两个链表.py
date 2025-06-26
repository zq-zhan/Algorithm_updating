class ListNode:
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next

# 7.合并两个链表
class Solution1:  # 快慢指针思路
	def mergeInBetween(self, list1, a, b, list2):
		dummy = ListNode(next = list1)
		right = dummy
		for _ in range(b - a + 1):
			right = right.next
		left = dummy
		for _ in range(a):
			left = left.next
			right = right.next
		left.next = list2
		cur = list2
		while cur.next:
			cur = cur.next
		cur.next = right.next
		return dummy.next

## 简洁写
class Solution1:
	def mergeInBetween(self, list1, a, b, list2):
		dummy = ListNode(next = list1)
		right = dummy
		for _ in range(b + 1):
			right = right.next
		left = dummy
		for _ in range(a):
			left = left.next
		left.next = list2
		cur = list2
		while cur.next:
			cur = cur.next
		cur.next = right.next
		return dummy.next


if __name__ == '__main__':
	list1 = ListNode(10, ListNode(1, ListNode(13, ListNode(6, ListNode(9, ListNode(5))))))
	a = 3
	b = 4
	list2 = ListNode(1000000, ListNode(1000001, ListNode(1000002)))
	print(Solution1().mergeInBetween(list1, a, b, list2))