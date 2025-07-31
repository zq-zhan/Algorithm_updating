class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	def delNodes(self, root, to_delete):
		ans = []
		def dfs(node):
			if not node:
				return None
			node.left = dfs(node.left)
			node.right = dfs(node.right)
			if node.val in to_delete:
				if node.left:
					ans.append(node.left)
				if node.right:
					ans.append(node.right)
				return None
			return node
		root = dfs(root)
		if root:
			ans.append(root)
		return ans
	
if __name__ == '__main__':
	root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
	print(Solution().delNodes(root, [3, 5]))