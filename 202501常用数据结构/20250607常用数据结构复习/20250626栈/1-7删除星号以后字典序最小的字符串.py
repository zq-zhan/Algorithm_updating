class Solution:
	def clearStars(self, s):
		ord_a = ord('a')
		ans = []
		ori_lis = [[] for i in range(26)]
		for i, x in enumerate(s):
			if x == '*':
				for stk in ori_lis:
					if stk:
						stk.pop()
						break
			else:
				ori_lis[ord(x) - ord_a].append(i)
		for i, stk in enumerate(ori_lis):
			temp_chr = chr(i + ord_a)
			for j in stk:
				ans.append((j, temp_chr))
		ans.sort(key = lambda x:x[0])
		result = [x[1] for x in ans]
		return ''.join(result)
	
## 灵神题解优化：
class Solution:
	def clearStars(self, s):
		ord_a = ord('a')
		ans = list(s)
		ori_lis = [[] for i in range(26)]
		for i, x in enumerate(s):
			if x == '*':
				for stk in ori_lis:
					if stk:
						ans[stk.pop()] = '*'
						break
			else:
				ori_lis[ord(x) - ord_a].append(i)
		return ''.join(x for x in ans if x != '*')

if __name__ == '__main__':
	s = "aaba*"
	print(Solution().clearStars(s))