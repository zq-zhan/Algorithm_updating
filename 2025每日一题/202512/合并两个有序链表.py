class ListNode:
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next

class Solution:
	def mergeTwoLists(self, listA, listB):
		p = dummy = ListNode(0)
		while listA and listB:
			if listA.val <= listB.val:
				p.next = listA
				listA = listA.next
			else:
				p.next = listB
				listB = listB.next
			p = p.next
		# if listA:
		# 	p.next = listA
		# else:
		# 	p.next = listB
		p.next = listA or listB
		return dummy.next
### 递归写法
class Solution:
	def mergeTwoLists(self, listA, listB):
		if listA is None:
			return listB
		if listB is None:
			return listA
		if listA.val < listB.val:
			listA.next = self.mergeTwoLists(listA.next, listB)
			return listA
		listB.next = self.mergeTwoLists(listA, listB.next)
		return listB
	
if __name__ == '__main__':
	listA = ListNode(1, ListNode(2, ListNode(4)))
	listB = ListNode(1, ListNode(3, ListNode(4)))
	s = Solution()
	merged = s.mergeTwoLists(listA, listB)