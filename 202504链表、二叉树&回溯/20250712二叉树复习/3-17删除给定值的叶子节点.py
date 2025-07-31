class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	def removeLeafNodes(self, root, target):
		def dfs(node):
			if not node:
				return None
			node.left = dfs(node.left)
			node.right = dfs(node.right)
			if not node.left and not node.right and node.val == target:
				return None
			return node
		return dfs(root)
	
if __name__ == '__main__':
	root = TreeNode(1, TreeNode(3, TreeNode(3), TreeNode(2)), TreeNode(3))
	target = 3
	print(Solution().removeLeafNodes(root, target))