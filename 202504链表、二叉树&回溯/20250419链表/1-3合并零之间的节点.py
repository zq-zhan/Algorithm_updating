class ListNode:
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next

# 3.合并零之间的节点
class Solution1:
	def mergeNodes(self, head):
		ans = ListNode(None)
		current = ans
		head = head.next
		temp_sum = 0
		while head:
			temp_sum += head.val
			if head.val == 0:
				# if ans is not None:
				# 	ans = ListNode(temp_sum)
				# else:
				# 	ans.next = ListNode(temp_sum)
				current.next = ListNode(temp_sum)
				current = current.next
				temp_sum = 0
			head = head.next
		return ans.next
	
## 在原节点基础上修改—— 明确思考指针的用法
class Solution2:
	def mergeNodes(self, head):
		q = head.next
		while q:
			if q.next.val == 0:
				q.next = q.next.next
				q = q.next
			else:
				q.val += q.next.val
				q.next = q.next.next
		return head.next

if __name__ == '__main__':
	head = ListNode(0, ListNode(3, ListNode(1, ListNode(0, ListNode(4, ListNode(5, ListNode(2, ListNode(0))))))))
	print(Solution2().mergeNodes(head))