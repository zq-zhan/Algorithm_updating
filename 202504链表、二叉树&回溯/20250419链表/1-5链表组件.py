class ListNode:
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next


# 5.链表组件
# class Solution1:
# 	def numComponents(self, head, nums):
# 		ans = temp_ans = result = 0
# 		while head:
# 			if head.val in nums:
# 				temp_ans += 1
# 			else:
# 				temp_ans = 0
# 			if temp_ans > ans:
# 				result = 1
# 			elif temp_ans == ans:
# 				result += 1
# 			ans = max(ans, temp_ans)
# 			head = head.next
# 		return result
	
class Solution1:
	def numComponents(self, head, nums):
		ans = cnt = 0
		while head:
			if head.val in nums:
				cnt += 1
			else:
				ans += 1 if cnt > 0 else 0
				cnt = 0
			head = head.next
		return ans + 1 if cnt > 0 else ans

## 优化
class Solution2:
	def numComponents(self, head, nums):
		nums = set(nums)
		p = head
		inSet = False
		ans = 0
		while p:
			if p.val in nums:
				if not inSet:
					inSet = True
					ans += 1
			else:
				inSet = False
			p = p.next
		return ans


if __name__ == '__main__':
	head = ListNode(0, ListNode(1, ListNode(2, ListNode(3))))
	nums = [0, 1, 3]
	print(Solution2().numComponents(head, nums)) # Output: 2