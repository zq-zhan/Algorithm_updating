class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	def evaluateTree(self, root):
		if not root.left and not root.right:
			return True if root.val else False
		left = self.evaluateTree(root.left)
		right = self.evaluateTree(root.right)
		if root.val == 2:
			return left or right
		else:
			return left and right
		
if __name__ == '__main__':
	root = TreeNode(2, TreeNode(1), TreeNode(3, TreeNode(0), TreeNode(1)))
	print(Solution().evaluateTree(root))