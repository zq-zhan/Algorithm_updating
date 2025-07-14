class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	def sumOfLeftLeaves(self, root):
		ans = 0
		def dfs(root, tag):
			if not root:
				return 
			if root.left is None and root.right is None and tag == 'left':
				nonlocal ans
				ans += root.val
			dfs(root.left, 'left')
			dfs(root.right, 'right')
		dfs(root, 'right')
		return ans
	
if __name__ == '__main__':
	root = TreeNode(3)
	print(Solution().sumOfLeftLeaves(root)) # Output: 24