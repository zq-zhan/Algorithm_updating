class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	def flipEquiv(self, root1, root2):
		if not root1 or not root2:
			return root1 is root2
		if root1.val == root2.val:
			return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) \
			or (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))
		else:
			return False
		return self.flipEquiv(root1, root2)

	
if __name__ == '__main__':
	root1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(7), TreeNode(8))), TreeNode(3, TreeNode(6)))
	root2 = TreeNode(1, TreeNode(3, None, TreeNode(6)), TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(8), TreeNode(7))))
	print(Solution().flipEquiv(root1, root2))