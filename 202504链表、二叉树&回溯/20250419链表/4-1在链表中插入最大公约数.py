class ListNode:
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next


# 6.在链表中插入最大公约数
class Solution1:
	def insertGreatestCommonDivisors(self, head):
		def find_mx(a, b):
			mn = min(a, b)
			for x in range(mn, 0, -1):
				if a % x == 0 and b % x == 0:
					return x
			return 1

		cur = head
		while cur.next:
			node_val = find_mx(cur.val, cur.next.val)
			insert = ListNode(node_val)
			nxt = cur.next  # 10
			cur.next = insert  # 6
			cur.next.next = nxt  # 10
			cur = nxt
		return head

if __name__ == '__main__':
	head = ListNode(18, ListNode(6, ListNode(10, ListNode(3))))
	print(Solution1().insertGreatestCommonDivisors(head))