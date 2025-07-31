from math import inf

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	def maxPathSum(self, root):
		ans = -inf
		def dfs(node):
			if not node:
				return 0
			left = max(dfs(node.left), 0)  # 左子树和为负数时就剪枝
			right = max(dfs(node.right), 0)
			nonlocal ans
			ans = max(ans, left + right + node.val)
			return max(left, right) + node.val
		dfs(root)
		return ans

if __name__ == '__main__':
	root = TreeNode(2, TreeNode(-1))
	print(Solution().maxPathSum(root)) # Output: 2