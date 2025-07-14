class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:  # 左-根-右
	def inorderTraversal(self, root):
		ans = []
		def dfs(root):
			if not root:
				return 
			dfs(root.left)
			ans.append(root.val)
			dfs(root.right)
		dfs(root)
		return ans

if __name__ == '__main__':
	root = TreeNode(1, None, TreeNode(2, TreeNode(3), TreeNode(4)))
	print(Solution().inorderTraversal(root)) # [3, 2, 4, 1]