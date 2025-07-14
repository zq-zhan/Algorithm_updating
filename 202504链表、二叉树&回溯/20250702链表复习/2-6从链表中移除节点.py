class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def removeNodes(self, head):
		head_lis = []
		cur = head
		while cur:
			head_lis.append(cur.val)
			cur = cur.next
		dummy = ListNode(None)
		mx = head_lis[-1]
		n = len(head_lis)
		ans = []
		for i in range(n - 1, -1, -1):
			if head_lis[i] >= mx:
				ans.append(head_lis[i])
				mx = max(head_lis[i], mx)
		cur = dummy
		for x in ans[::-1]:
			cur.next = ListNode(x)
			cur = cur.next
		return dummy.next
	
if __name__ == '__main__':
	head = ListNode(5, ListNode(2, ListNode(13, ListNode(3, ListNode(8)))))
	print(Solution().removeNodes(head))