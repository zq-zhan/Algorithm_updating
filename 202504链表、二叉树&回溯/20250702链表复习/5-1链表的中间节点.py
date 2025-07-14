class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def middleNode(self, head):
		slow = head
		fast = head
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
		return slow

if __name__ == '__main__':
	head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
	print(Solution().middleNode(head).val)

