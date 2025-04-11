class TreeNode:
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right


class Solution1:
	def sumNumbers(self, root):
		ans = 0
		def dfs(root, cnt):
			if not root:
				return 
			cnt += str(root.val)
			nonlocal ans
			if root.left is None and root.right is None:
				ans += int(cnt)
			dfs(root.left, cnt)
			dfs(root.right, cnt)
		dfs(root, '')
		return ans
	
class Solution2:
	def sumNumbers(self, root, x = ''):
		if not root:
			return 0
		x += str(root.val)
		if root.left is None and root.right is None:
			return int(x)
		return self.sumNumbers(root.left, x) + self.sumNumbers(root.right, x)


if __name__ == '__main__':
	# root = TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))
	root = TreeNode(0, TreeNode(1))
	print(Solution2().sumNumbers(root))