class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	def leafSimilar(self, root1, root2):
		ans1 = []
		ans2 = []
		def dfs(root, ans):
			if not root:
				return 
			if root.left is None and root.right is None:
				ans.append(root.val)
			dfs(root.left, ans)
			dfs(root.right, ans)
		dfs(root1, ans1)
		dfs(root2, ans2)
		return ans1 == ans2

	
if __name__ == '__main__':
	root1 = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, None, TreeNode(9, TreeNode(8))))
	root2 = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(7)), TreeNode(1, TreeNode(4), TreeNode(2, TreeNode(9), TreeNode(8))))
	print(Solution().leafSimilar(root1, root2))