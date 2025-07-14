class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def getDecimalValue(self, head):
		ans = ''
		while head:
			ans += str(head.val)
			head = head.next
		return int(ans, 2)
	
if __name__ == '__main__':
	head = ListNode(1, ListNode(0, ListNode(1)))
	print(Solution().getDecimalValue(head)) # 5
	