class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	def preorderTraversal(self, root):
		ans = []
		def dfs(root):
			if not root:
				return
			nonlocal ans
			ans.append(root.val)
			dfs(root.left)
			dfs(root.right)
		dfs(root)
		return ans

if __name__ == '__main__':
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    print(Solution().preorderTraversal(root))