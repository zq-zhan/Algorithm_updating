class ListNode:
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next

## 灵神题解——归并排序（分治）
class Solution:
	## 链表的中间节点
	def middleNode(self, head):
		slow = fast = head
		while fast and fast.next:
			pre = slow # 记录slow的前一个节点，用于分段
			slow = slow.next
			fast = fast.next.next
		pre.next = None
		return slow

	## 合并两个有序链表
	def mergeTwoLists(self, list1, list2):
		cur = dummy = ListNode()
		while list1 and list2:
			if list1.val <= list2.val:
				cur.next = list1
				list1 = list1.next
			else:
				cur.next = list2
				list2 = list2.next
			cur = cur.next
		cur.next = list1 if list1 else list2
		return dummy.next

	def sortList(self, head):
		if head is None or head.next is None:
			return head

		head2 = self.middleNode(head)

		# 分治
		head = self.sortList(head)
		head2 = self.sortList(head2)

		return self.mergeTwoLists(head, head2)

if __name__ == '__main__':
	head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
	print(Solution().sortList(head))