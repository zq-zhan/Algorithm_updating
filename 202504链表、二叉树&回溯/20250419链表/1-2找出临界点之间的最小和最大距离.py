from math import inf

class ListNode:
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next

class Solution1:
	def nodesBetweenCriticalPoints(self, head):
		distance_lis = []
		mindistance = inf
		# maxdistance = 0
		cnt = 0
		while head:
			if cnt >= 1 and head.next:
				if (head.val > pre and head.val > head.next.val) or \
					(head.val < pre and head.val < head.next.val):
					distance_lis.append(cnt)
					if len(distance_lis) >= 2:
						mindistance = min(mindistance, distance_lis[-1] - distance_lis[-2])
						# maxdistance = max(maxdistance, distance_lis[-1] - distance_lis[0])
			cnt += 1
			pre = head.val
			head = head.next
		# return [mindistance, maxdistance] if maxdistance > 0 else [-1, -1]
		return [mindistance, distance_lis[-1] - distance_lis[0]] if mindistance < inf else [-1, -1]



if __name__ == '__main__':
	# head = ListNode(5, ListNode(3, ListNode(1, ListNode(2, ListNode(5, ListNode(1, ListNode(2)))))))
	head = ListNode(3, ListNode(1))
	print(Solution1().nodesBetweenCriticalPoints(head))
