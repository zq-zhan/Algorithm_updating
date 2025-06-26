class ListNode:
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next

class Solution1:
	def modifiedList(self, nums, head):
		nums = set(nums)
		cur = dummy = ListNode(next = head)
		while cur.next:
			if cur.next.val in nums:
				cur.next = cur.next.next
			else:
				cur = cur.next
		return dummy.next
	
if __name__ == '__main__':
	nums = [1,2,3]
	head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
	print(Solution1().modifiedList(nums, head))