class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
	def leafSimilar(self, root1, root2):
		ans1 = []
		ans2 = []
		def pass_read(root):
			nonlocal ans
			ans = []
			def dfs(root):
				if not root:
					return 
				if root.left is None and root.right is None:
					ans.append(root.val)
				dfs(root.left)
				dfs(root.right)
			return ans
		ans1 = pass_read(root1)
		ans2 = pass_read(root2)
		return ans1 == ans2
		# return pass_read(root1) == pass_read(root2)
		
class Solution2:
	def leafSimilar(self, root1, root2):
		ans1 = []
		ans2 = []

		def dfs(root, result):
			if not root:
				return
			if root.left is None and root.right is None:
				result.append(root.val)
			dfs(root.left, result)
			dfs(root.right, result)
			
		dfs(root1, ans1)
		dfs(root2, ans2)
		return ans1 == ans2

if __name__ == '__main__':
	# Example usage:
	root1 = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(9), TreeNode(8)))
	root2 = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(7)), TreeNode(1, TreeNode(4), TreeNode(2, 9, TreeNode(8))))
	print(Solution1().leafSimilar(root1, root2)) # Output: True