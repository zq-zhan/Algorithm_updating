class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

## 灵神题解——快慢指针+反转链表
class Solution:
	def isPalindrome(self, head):
		dummy = ListNode(next = head)
		slow = dummy
		fast = dummy.next
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
		pre = None
		cur = slow.next
		while cur:
			nxt = cur.next
			cur.next = pre
			pre = cur
			cur = nxt
		slow.next = None
		cur = dummy.next
		while cur and pre:
			if cur.val != pre.val:
				return False
			cur = cur.next
			pre = pre.next
		return True
	
if __name__ == '__main__':
	head = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
	s = Solution()
	print(s.isPalindrome(head))