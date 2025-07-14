class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
	def rightSideView(self, root):
		ans = []
		def dfs(root, depth):
			if not root:
				return 
			if depth == len(ans):
				ans.append(root.val)
			dfs(root.right, depth + 1)
			dfs(root.left, depth + 1)
		dfs(root, 0)
		return ans
	
if __name__ == '__main__':
	root = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(5))), TreeNode(3))
	print(Solution().rightSideView(root)) # Output: [1, 3, 4]