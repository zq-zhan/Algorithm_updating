class Solution:
	def validateStackSequences(self, pushed, poped):
		ans = []
		p1 = 0
		for x in pushed:
			if x != poped[p1]:
				ans.append(x)
			else:
				p1 += 1
			while ans and ans[-1] == poped[p1]:
				ans.pop()
				p1 += 1

		return len(ans) == 0



if __name__ == '__main__':
	pushed = [1,2,3,4,5]
	poped = [4,5,3,2,1]
	print(Solution().validateStackSequences(pushed, poped))