# 1.二叉树的前序遍历
class TreeNode:
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right
## 递归写法
class Solution1:
	def preorderTraversal(self, root):
		ans = []
		def dfs(root):
			if not root:
				return 
			ans.append(root.val)
			dfs(root.left)
			dfs(root.right)
		dfs(root)
		return ans
	
## 迭代写法
class Solution2:
	def preorderTraversal(self, root):
		ans = []
		if not root:
			return ans
		stack = [root]
		while stack:
			node = stack.pop()
			ans.append(node.val)
			if node.right:
				stack.append(node.right)  # 栈-先入后出
			if node.left:
				stack.append(node.left)
		return ans

	
if __name__ == '__main__':
	root = TreeNode(1)
	# root.left = None
	root.right = TreeNode(2)
	root.right.left = TreeNode(3)
	print(Solution2().preorderTraversal(root)) # [1, None, 2, 3]