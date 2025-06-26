class ListNode:
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next

# 1.二进制链表转整数
class Solution1:
	def getDecimalValue(self, head):
		ans = ''
		while head:
			ans += str(head.val)
			head = head.next
		return int(ans, 2)
	
if __name__ == '__main__':
	head = ListNode(1, ListNode(0, ListNode(1)))
	print(Solution1().getDecimalValue(head)) # 5