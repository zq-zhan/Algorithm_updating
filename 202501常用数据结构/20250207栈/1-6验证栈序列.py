# 6.验证栈序列
class Solution1:
	def validateStackSequences(self, pushed, poped):
		ans = []
		p1 = p2 = 0
		n, m = len(pushed), len(poped)
		while p2 < m:
			while p1 < n and (not ans or ans[-1] != poped[p2]):
				ans.append(pushed[p1])
				p1 += 1
			if ans[-1] == poped[p2]:
				ans.pop()
			# p1 += 1
			p2 += 1
		return len(ans) == 0
	
if __name__ == '__main__':
	pushed = [1,2,3,4,5]
	poped = [4,3,5,1,2]
	cls = Solution1()
	print(cls.validateStackSequences(pushed, poped))