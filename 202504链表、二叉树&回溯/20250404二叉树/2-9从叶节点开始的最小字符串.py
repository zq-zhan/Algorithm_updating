# 9.从叶节点开始的最小字符串
from math import inf

class TreeNode:
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

class Solution1:
	def smallestFromLeaf(self, root):
		ans = inf
		def dfs(root, cnt, val):
			if not root:
				return
			val += root.val * 10 ** cnt
			cnt += 1
			if root.left is None and root.right is None:
				nonlocal ans
				ans = min(ans, val)
			dfs(root.left, cnt, val)
			dfs(root.right, cnt, val)
		dfs(root, 0, 0)
		return ans
	
class Solution2:
	def smallestFromLeaf(self, root):
		ans = 'z' * 8500
		ori = ord('a')
		def dfs(root, char):
			if not root:
				return
			char += chr(root.val + ori)
			if root.left is None and root.right is None:
				nonlocal ans
				# if len(ans) > len(char):
				# 	ans = char[::-1]
				# elif len(ans) == len(char) and ans > char[::-1]:
				# 	ans = char[::-1]
				if ans > char[::-1]:
					ans = char[::-1]
			dfs(root.left, char)
			dfs(root.right, char)
		dfs(root, '')
		return ans

if __name__ == '__main__':
	# root = TreeNode(0, TreeNode(1, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(3), TreeNode(4)))
	root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
	print(Solution2().smallestFromLeaf(root)) # Output: 1132