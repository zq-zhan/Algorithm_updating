

class Solution1:
	def lcaDeepestLeaves(self, root):
		n = len(root)
		root_lis = []
		i = 0
		k = 1
		while i < n:
			root_lis.append(root[i:i + k])
			i += k
			k *= 2
		ans = []
		m = len(root_lis[-1])
		for i in range(0, m, 2):
			if root_lis[-1][i] != 'null':
				ans.extend([root_lis[-2][i // 2], root_lis[-1][i], root_lis[-1][i + 1]])
		return ans

if __name__ == '__main__':
	root = [3,5,1,6,2,0,8,'null','null',7,4]
	print(Solution1().lcaDeepestLeaves(root))