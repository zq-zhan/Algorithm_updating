class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def mergeNodes(self, head):
		ans = ListNode(0) # 哨兵节点
		cur = ans
		temp_s = 0
		head = head.next
		while head:
			if head.val != 0:
				temp_s += head.val
			else:
				cur.next = ListNode(temp_s)
				cur = cur.next
				temp_s = 0
			head = head.next
		return ans.next
	
## 灵神题解
class Solution:
	def mergeNodes(self, head):
		tail = head
		cur = head.next
		while cur.next:
			if cur.val:
				tail.val += cur.val
			else:
				tail = tail.next
				tail.val = 0
			cur = cur.next
		tail.next = None
		return head

if __name__ == '__main__':
	# head = ListNode(0, ListNode(3, ListNode(1, ListNode(0, ListNode(4, ListNode(5, ListNode(2, ListNode(0, None))))))))
	head = ListNode(0, ListNode(1, ListNode(0, ListNode(3, ListNode(0, ListNode(2, ListNode(2, ListNode(0))))))))
	print(Solution().mergeNodes(head))