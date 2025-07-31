class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	def pathSum(self, root, targetSum):
		ans = []
		path = []
		def dfs(node):
			if not node:
				return 
			path.append(node.val)
			if not node.left and not node.right and sum(path) == targetSum:
				ans.append(path.copy())
			else:
				dfs(node.left)
				dfs(node.right)
			path.pop()
		dfs(root)
		return ans
	
if __name__ == '__main__':
	root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))
	targetSum = 22
	print(Solution().pathSum(root, targetSum))