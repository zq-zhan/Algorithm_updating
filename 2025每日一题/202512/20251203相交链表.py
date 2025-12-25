class ListNode:
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next

## 灵神题解
class Solution:
	def getIntersectionNode(self, headA, headB):
		p, q = headA, headB
		while p is not q:  # 检查的是地址是否相同，而不是值是否相同
			p = p.next if p else headB
			q = q.next if q else headA
		return p
	
if __name__ == '__main__':
	common = ListNode(8, ListNode(4, ListNode(5)))
	headA = ListNode(4, ListNode(1, common))
	headB = ListNode(5, ListNode(6, ListNode(1, common)))
	print(Solution().getIntersectionNode(headA, headB).val) # 8
