# 3.二叉树的后序遍历
class TreeNode:
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right


class Solution: # 左-右-根
	def postorderTraversal(self, root):
		ans = []
		def dfs(root):
			if not root:
				return 
			dfs(root.left)
			dfs(root.right)
			ans.append(root.val)
		dfs(root)
		return ans
	
if __name__ == '__main__':
	root = TreeNode(1)
	root.right = TreeNode(2)
	root.right.left = TreeNode(3)
	s = Solution()
	print(s.postorderTraversal(root))