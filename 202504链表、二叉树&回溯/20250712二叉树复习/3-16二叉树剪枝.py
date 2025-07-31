class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	def pruneTree(self, root):
		def dfs(node):
			if not node:
				return None
			node.left = dfs(node.left)
			node.right = dfs(node.right)
			if node.val == 0 and not node.left and not node.right:
				return None
			return node
		dfs(root)
		return root
	
if __name__ == '__main__':
	root = TreeNode(1, None, TreeNode(0, TreeNode(0), TreeNode(1)))
	print(Solution().pruneTree(root))