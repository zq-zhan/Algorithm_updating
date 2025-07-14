class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def numComponents(self, head, nums):
		cur = head
		while cur.next:
			cur = cur.next
		cur.next = ListNode(-1)  # 尾插法，方便后续操作

		left = right = ans = 0
		nums = set(nums)
		while head:
			if head.val not in nums:
				ans += 1 if left != right else 0
				left = right
			else:
				right += 1
			head = head.next
		return ans
	
if __name__ == '__main__':
	head = ListNode(0, ListNode(1, ListNode(2)))
	nums = [0,2]
	print(Solution().numComponents(head, nums))