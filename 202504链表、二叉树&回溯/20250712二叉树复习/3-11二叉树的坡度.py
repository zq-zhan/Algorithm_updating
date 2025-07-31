class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	def findTilt(self, root):
		ans = 0
		def dfs(node):
			nonlocal ans
			if not node:
				return 0
			if not node.left and not node.right:
				return node.val
			left = dfs(node.left)
			right = dfs(node.right)
			ans += abs(left - right)
			return abs(left - right)
		dfs(root)
		return ans


if __name__ == '__main__':
	root = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(5)), TreeNode(9, None, TreeNode(7)))
	print(Solution().findTilt(root))