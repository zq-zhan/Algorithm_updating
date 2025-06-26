from math import inf

class TreeNode:
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

class Solution1:
	def goodNodes(self, root):
		ans = 0
		def dfs(root, num):
			if not root:
				return 
			# if root.left is None and root.right is None:
			nonlocal ans
			ans += 1 if root.val >= num else 0
			num = max(root.val, num)
			dfs(root.left, num)
			dfs(root.right, num)
		dfs(root, -inf)
		return ans

## 自底向上-灵神题解
class Solution3:
	def goodNodes(self, root, num = -inf):
		if not root:
			return 0
		left = self.goodNodes(root.left, max(num, root.val))
		right = self.goodNodes(root.right, max(num, root.val))
		return left + right + (num <= root.val)


if __name__ == '__main__':
	root = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))
	print(Solution3().goodNodes(root))