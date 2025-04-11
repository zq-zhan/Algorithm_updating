# 5.开幕式的焰火
class TreeNode:
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

class Solution1:
	def numColor(self, root):
		ans = set()

		def dfs(root):
			if not root:
				return 
			ans.add(root.val)
			dfs(root.left)
			dfs(root.right)
		dfs(root)
		return len(ans)
	
if __name__ == '__main__':
	root = TreeNode(1, TreeNode(3, TreeNode(1), None), TreeNode(2, TreeNode(2), None))
	print(Solution1().numColor(root)) # Output: 3