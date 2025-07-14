class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def splitListToParts(self, head, k):
		cur = head
		n = 0
		while cur:
			n += 1
			cur = cur.next
		ori_cnt = (n - 1) // k + 1
		target_len = []
		if n <= k:
			target_len = [1] * n + [0] * (k - n)
		else:
			for _ in range(k):
				target_len.append(ori_cnt)
				ori_cnt -= 1
			target_len[-1] += n - sum(target_len)

		ans = []
		temp_lis = []
		index = 0
		while head:
			temp_lis.append(head.val)
			if len(temp_lis) == target_len[index]:
				ans.append(temp_lis)
				temp_lis = []
				index += 1
			head = head.next
		while len(ans) < k:
			ans.append([])
		return ans

class Solution2:  # 错解，不是数组形式返回
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
    print(Solution().splitListToParts(head, k))