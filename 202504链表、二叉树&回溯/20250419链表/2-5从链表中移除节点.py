class ListNode:
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next


# class Solution1:  贪心思路是错解
# 	def removeNodes(self, head):
# 		max_node = 1
# 		cur = head
# 		while cur:
# 			max_node = max(max_node, cur.val)
# 			cur = cur.next
# 		cur = dummy = ListNode(next = head)
# 		while cur.next.next:
# 			if cur.next.val < max_node:
# 				cur.next = cur.next.next
# 			else:
# 				cur = cur.next
# 		return dummy.next
class Solution2:
	def removeNodes(self, head):
		head_node = []
		cur = head
		while cur:
			head_node.append(cur.val)
			cur = cur.next

		n = len(head_node)
		for i in range(n - 2, -1, -1):
			head_node[i] = max(head_node[i], head_node[i + 1])

		cnt = 0
		cur = dummy = ListNode(next = head)
		while cur.next.next:
			if cur.next.val < head_node[cnt]:
				cur.next = cur.next.next
			else:
				cur = cur.next
			cnt += 1
		return dummy.next
	


if __name__ == '__main__':
	head = ListNode(5, ListNode(2, ListNode(13, ListNode(3, ListNode(8)))))
	print(Solution2().removeNodes(head))