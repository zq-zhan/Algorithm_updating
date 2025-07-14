from math import inf
# from itertools import pairwise

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def nodesBetweenCriticalPoints(self, head):
		ans = []
		pre_val = head.val
		head = head.next
		index = 1
		while head.next:
			x = head.val
			nxt_val = head.next.val
			if (x > pre_val and x > nxt_val) or (x < pre_val and x < nxt_val):
				ans.append(index)
			index += 1
			head = head.next
			pre_val = x
		if len(ans) < 2:
			return [-1, -1]
		else:
			temp_ans = inf
			for x, y in zip(ans, ans[1:]):
				temp_ans = min(y - x, temp_ans)
			return [temp_ans, ans[-1] - ans[0]]

class Solution:
	def nodesBetweenCriticalPoints(self, head):
		ans = []
		pre_val = head.val
		head = head.next
		index = 1
		temp_ans = inf
		while head.next:
			x = head.val
			nxt_val = head.next.val
			if (x > pre_val and x > nxt_val) or (x < pre_val and x < nxt_val):
				ans.append(index)
				if len(ans) >= 2:
					temp_ans = min(ans[-1] - ans[-2], temp_ans)
			index += 1
			head = head.next
			pre_val = x

		return [temp_ans, ans[-1] - ans[0]] if temp_ans < inf else [-1, -1]

if __name__ == '__main__':
	# head = ListNode(5, ListNode(3, ListNode(1, ListNode(2, ListNode(5, ListNode(1, ListNode(2)))))))
	head = ListNode(4, ListNode(2, ListNode(4, ListNode(1))))
	print(Solution().nodesBetweenCriticalPoints(head))