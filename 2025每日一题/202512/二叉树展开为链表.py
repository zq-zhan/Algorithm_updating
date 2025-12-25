class TreeNode:
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def flatten(self, root):
		ans = []
		def dfs(node):
			if not node:
				return
			ans.append(node)
			dfs(node.left)
			dfs(node.right)
		dfs(root)
		n = len(ans)
		for i in range(n - 1):
			ans[i].left = None
			ans[i].right = ans[i + 1]
		ans[-1].left = None
		ans[-1].right = None
		return root
## 灵神题解——分治
class Solution:
	def flatten(self, root):
		if root is None:
			return None
		left_tail = self.flatten(root.left)
		right_tail = self.flatten(root.right)
		if left_tail:
			left_tail.right = root.right
			root.right = root.left
			root.left = None
		return right_tail or left_tail or root

## 灵神题解——头插法
class Solution:
	head = None
	def flatten(self, root):
		if root is None:
			return
		self.flatten(root.right)
		self.flatten(root.left)
		root.left = None
		root.right = self.head
		self.head = root



if __name__ == '__main__':
	root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
	print(Solution().flatten(root))