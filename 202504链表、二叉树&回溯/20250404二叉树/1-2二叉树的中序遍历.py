class TreeNode:
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
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
	
## 迭代写法
class Solution2:
	def inorderTraversal(self, root):
		ans = []
		if not root:
			return ans
		stack = [root]
		while stack:
			node = stack.pop()
			if node.right:
				stack.append(node.right)
			
			if node.left:
				stack.append(node.left)
			ans.append(node.val)
		return ans
	

if __name__ == '__main__':
	root = TreeNode(1)
	root.right = TreeNode(2)
	root.right.left = TreeNode(3)
	print(Solution2().inorderTraversal(root)) # Output: [1,3,2]