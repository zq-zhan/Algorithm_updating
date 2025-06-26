
class TreeNode:
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

# 10.节点与其祖先的最大差值
class Solution1:
	def maxAncestorDiff(self, root):
		ans = 0
		def dfs(root, min_val, max_val):
			if not root:
				return 
			nonlocal ans
			ans = max(ans, abs(min_val - root.val), abs(max_val - root.val))
			min_val = min(min_val, root.val)
			max_val = max(max_val, root.val)
			dfs(root.left, min_val, max_val)
			dfs(root.right, min_val, max_val)
		dfs(root, root.val, root.val)
		return ans
	
if __name__ == '__main__':
	root = TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6, TreeNode(4), TreeNode(7))), TreeNode(10, None, TreeNode(14, TreeNode(13))))
	print(Solution1().maxAncestorDiff(root)) # Output: 7