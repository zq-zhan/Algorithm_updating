from math import inf

class TreeNode:
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def isValidBST(self, root):
		ans = True
		def dfs(node, min_x, max_x):
			if node is None:
				return

			nonlocal ans
			if not min_x < node.val < max_x:
				ans = False
				return

			dfs(node.left, min_x, node.val)
			dfs(node.right, node.val, max_x)
		dfs(root, -inf, inf)
		return ans

## 灵神题解
# class Solution:
# 	def isValidBST(self, root, left, right):
# 		if root is None:
# 			return True
# 		x = root.val
# 		return left < x < right and self.isValidBST(root.left, left, x) and self.isValidBST(root.right, x, right)



if __name__ == '__main__':
	root = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))
	print(Solution().isValidBST(root))