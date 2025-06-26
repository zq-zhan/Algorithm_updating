# 2.路径总和
class TreeNode:
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

class Solution1:
	def hasPathSum(self, root, targetSum):
		result = False
		def dfs(root, ans):
			nonlocal result
			if not root:
				return
			ans += root.val
			if root.left is None and root.right is None and ans == targetSum:
				result = True
				return
			dfs(root.left, ans)
			dfs(root.right, ans)
		dfs(root, 0)
		return result
	
if __name__ == '__main__':
	root = TreeNode(1, TreeNode(2), TreeNode(3))
	targetSum = 5 
	print(Solution1().hasPathSum(root, targetSum))