class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	def binaryTreePaths(self, root):
		ans = []
		def dfs(node, temp_s):
			if not node:
				return
			temp_s += str(node.val) + '->'
			if not node.left and not node.right:
				temp_s = temp_s[:-2]
				ans.append(temp_s)
				return
			dfs(node.left, temp_s)
			dfs(node.right, temp_s)
		dfs(root, '')
		return ans
	
class Solution:
	def binaryTreePaths(self, root):
		ans = []
		path = []
		def dfs(node):
			if not node:
				return 
			path.append(str(node.val))
			if not node.left and not node.right:
				ans.append('->'.join(path))
			dfs(node.left)
			dfs(node.right)
			path.pop()  # 恢复现场
		dfs(root)
		return ans

if __name__ == '__main__':
	root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
	print(Solution().binaryTreePaths(root))