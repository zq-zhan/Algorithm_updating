class ListNode:
	def __init__(self,val=0,next=None):
		self.val=val
		self.next=next

class Solution:
	def addTwoNumbers(self,l1,l2):
		dummy_listnode=ListNode(0)
		curren_listnode=dummy_listnode
		carry=0
		while l1 or l2 or carry:
			if l1 is None:
				l1=ListNode(0)
			if l2 is None:
				l2=ListNode(0)
			s=carry+l1.val+l2.val
			carry=s//10
			curren_listnode.next=ListNode(s%10)
			curren_listnode=curren_listnode.next
			l1=l1.next
			l2=l2.next
		return dummy_listnode.next

l1_lis=[5,4,9]
l2_lis=[8,3,2,4,4,2]
def create_linked_list_from_list(lst):
	head=ListNode(0)
	current=head  # 指针指向头结点
	for value in lst[::-1]:
		current.next=ListNode(value)
		current=current.next
	return head.next
l1=create_linked_list_from_list(l1_lis)
# while l1:
# 	print(l1.val,end=' ')
# 	l1=l1.next
# print()
l2=create_linked_list_from_list(l2_lis)
# while l2:
# 	print(l2.val,end=' ')
# 	l2=l2.next
# print()

s=Solution()
result=s.addTwoNumbers(l1,l2)
while result:
	print(result.val,end=' ')
	result=result.next

class ListNode:
	def __init__(self,val=0,next=None):
		self.val=val
		self.next=next

class Solution:
	def addTwoNumbers(self,l1,l2):
		dummy_listnode=ListNode()
		carry=0
		while l1 or l2:
			if l1 is None:
				l1=ListNode(0)
			if l2 is None:
				l2=ListNode(0)
			s=carry+l1.val+l2.val
			carry=s//10
			dummy_listnode.next=ListNode(s%10)
		return dummy_listnode.next

l1_lis=[5,4,9]
l2_lis=[8,3,2,4,4,2]
l1=ListNode()
l2=ListNode()
for i in l1_lis[::-1]:
	l1.next=ListNode(i)
for j in l2_lis[::-1]:
	l2.next=ListNode(j)