class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	def diameterOfBinaryTree(self, root):
		ans = 0
		def dfs(node):
			if not node:
				return -1
			left = dfs(node.left)
			right = dfs(node.right)
			nonlocal ans
			ans = max(ans, left + right + 2)  # 以当前节点为中间节点(拐弯)的最长直径
			return max(left, right) + 1  # 以当前节点为根的子树的最长链
		dfs(root)
		return ans
	
if __name__ == '__main__':
	root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
	print(Solution().diameterOfBinaryTree(root))  # Output: 3