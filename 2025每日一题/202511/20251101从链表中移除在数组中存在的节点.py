class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
	def modifiedList(self, nums, head):
		num_node = ListNode(0, next = head)
		cur = num_node
		nums = set(nums)
		while cur:
			if cur.next and cur.next.val in nums:
				cur.next = cur.next.next
			cur = cur.next
		return num_node.next
	
if __name__ == '__main__':
	nums = [1,2,3]
	head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
	print(Solution().modifiedList(nums, head))