class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	def mergeTrees(self, root1, root2):
		if not root1 and not root2:
			return None
		if not root1:
			root1 = root2
		elif root1 and root2:
			root1.val += root2.val
		left = self.mergeTrees(root1.left, root2.left)
		right = self.mergeTrees(root1.right, root2.right)
		root1.left = left
		root2.right = right
		return root1
	
if __name__ == '__main__':
	root1 = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
	root2 = TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3, None, TreeNode(7)))
	print(Solution().mergeTrees(root1, root2))
	