class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


## 灵神题解
class Solution:
	def invertTree(self, root):
		if not root:
			return None
		left = self.invertTree(root.left)
		right = self.invertTree(root.right)
		root.left = right
		root.right = left
		return root

### 自上向下
class Solution:
	def invertTree(self, root):
		if not root:
			return None
		root.left, root.right = root.right, root.left
		self.invertTree(root.left)
		self.invertTree(root.right)
		return root


if __name__ == '__main__':
	root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
	print(Solution().invertTree(root))