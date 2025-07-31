class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	def maxProduct(self, root):
		total_s = 0
		def dfs(node):
			if not node:
				return
			nonlocal total_s
			total_s += node.val
			dfs(node.left)
			dfs(node.right)
		dfs(root)

		ans = 0
		def sub_dfs(node):
			if not node:
				return 0
			left = sub_dfs(node.left)
			right = sub_dfs(node.right)
			nonlocal ans
			temp_s = left + right + node.val
			ans = max(ans, (total_s-temp_s) * temp_s)
			return left + right + node.val
		sub_dfs(root)
		return ans
	
if __name__ == '__main__':
	root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
	print(Solution().maxProduct(root))