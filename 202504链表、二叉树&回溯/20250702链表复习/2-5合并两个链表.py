class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def mergeInBetween(self, list1, a, b, list2):
		dummy = ListNode(next = list1)
		cur = dummy
		cnt = 0
		while cnt <= b:
			if cnt == a:
				temp = cur.next
				while cnt <= b:
					temp = temp.next
					cnt += 1
				cur.next = list2
				while cur.next:
					cur = cur.next
				cur.next = temp
				break
			else:
				cur = cur.next
				cnt += 1
		return dummy.next
	
if __name__ == '__main__':
	list1 = ListNode(10, ListNode(1, ListNode(13, ListNode(6, ListNode(9, ListNode(5))))))
	a = 3
	b = 4
	list2 = ListNode(1000000, ListNode(1000001, ListNode(1000002)))
	print(Solution().mergeInBetween(list1, a, b, list2))