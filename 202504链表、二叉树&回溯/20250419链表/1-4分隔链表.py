class ListNode:
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next


class Solution1:
	def splitListToParts(self, head, k):
		ans = []
		while head:
			ans.append(head.val)
			head = head.next
		result = []
		ori = 0
		n = len(ans)
		if n <= k:
			for x in ans:
				result.append([x])
			for _ in range(k - n):
				result.append([])
			return result

		mod = n % k
		cnt = n // k
		while ori <= n - 1:
			length = ori + cnt + int(mod >= 1)
			result.append(ans[ori:length])
			ori = length 
			mod -= 1
		return result
	
class Solution2:
	def splitListToParts(self, head, k):
		ans = []
		while head:
			ans.append(head.val)
			head = head.next
		result = ListNode(None)
		current = result
		ori = 0
		n = len(ans)
		if n <= k:
			for x in ans:
				current.next = ListNode(x)
				current = current.next
			for _ in range(k - n):
				current.next = ListNode(None)
				current = current.next
			return result
		mod = n % k
		cnt = n // k
		while ori <= n - 1:
			length = ori + cnt + int(mod >= 1)	
			current.next = ListNode(ans[ori:length])
			current = current.next()
			ori = length
			mod -= 1
		return result.next
	
class Solution:
    def splitListToParts(self, head, k):
        #计算链表长度
        cnt, length = head, 0
        while cnt:
            cnt = cnt.next
            length+=1

        #每部分长度
        part_length =  length // k

        #前 remainder 部分需要额外加一个节点
        remainder = length % k         
        res = []
        cur = head   # 可变对象，传递的是引用
        for i in range(k):
            part_head= cur 

            cur_part_length =  part_length 

            #前 remainder 部分需要额外加一个节点
            if remainder:
                cur_part_length+=1
                remainder-=1
            #不为空时, 遍历添加当前部分的节点
            for j in range(cur_part_length - 1):
                if cur:
                    cur = cur.next

            #如果后续还有节点则断开链接
            if cur:
                next_part = cur.next
                cur.next = None  # 原地修改，所以会修改原链表
                cur = next_part  # 重新赋值，所以不会影响原链表
            res.append(part_head)
        return res
	
class Solution3:
    def splitListToParts(self, root: ListNode, k: int):
        total_len = 0
        cur = root
        while cur:
            total_len += 1
            cur = cur.next
        length = total_len // k   # 每段的基础长度
        m = total_len % k         # 前 l 段需要在基础长度上+1

        res = []
        cur = root
        for i in range(k):
            res.append(cur)
            size = length + (1 if m > 0 else 0)   # 算出每段的长度
            if cur:   # 这里判断cur是否存在，防止cur.next不存在报错
                for j in range(size-1):
                    cur = cur.next
                m -= 1
                tmp = cur.next   # 把后面一段截掉，后面一段需在后面继续划分
                cur.next = None
                cur = tmp
        return res



if __name__ == '__main__':
	head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9, ListNode(10))))))))))
	# head = ListNode(1, ListNode(2, ListNode(3)))
	k = 3
	print(Solution3().splitListToParts(head, k))