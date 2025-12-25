# from itertools import pairwise

class Solution:
	def minDeletionSize(self, strs):
		n, m = len(strs), len(strs[0])
		new_strs = [''] * m

		ans = 0
		for i in range(m):
			pre = 0
			for x in strs:
				new_strs[i] += s[i]
				if len(new_strs[i]) >= 2 and new_strs[i][-2] > new_strs[i][-1]:
					pre = 1
			ans += pre

		return ans
## 灵神写法
class Solution:
	def minDeletionSize(self, strs):
		ans = 0
		for col in zip(*strs): # 行列转置,实现纵向取列
			# if any(x > y for x, y in pairwise(col)): # 等价于zip(col, col[1:])
			if any(x > y for x, y in zip(col, col[1:])):
				ans += 1
		return ans



if __name__ == '__main__':
	strs = ["zyx","wvu","tsr"]
	print(Solution().minDeletionSize(strs))