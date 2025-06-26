class TreeNode:
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right


class Solution1:
	def sumOfLeftLeaves(self, root):
		ans = 0
		
		def dfs(root, tag):
			nonlocal ans
			if not root:
				return 
			if root.left is None and root.right is None and tag == 'left':
				ans += root.val
			dfs(root.left, 'left')
			dfs(root.right, 'right')
		dfs(root, 'right')
		return ans
	
if __name__ == '__main__':
	root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
	print(Solution1().sumOfLeftLeaves(root))