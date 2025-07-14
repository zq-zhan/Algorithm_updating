class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	def sumNumbers(self, root):
		ans = 0
		def dfs(root, temp_s):
			if not root:
				return 
			temp_s += str(root.val)
			if not root.right and not root.left:
				nonlocal ans
				ans += int(temp_s)
			dfs(root.left, temp_s)
			dfs(root.right, temp_s)
		dfs(root, '')
		return ans
## 自底向上遍历
class Solution:
	def sumNumbers(self, root, x = 0):
		if not root:
			return 0
		x = x * 10 + root.val
		if not root.left and not root.right:
			return x
		return self.sumNumbers(root.left, x) + self.sumNumbers(root.right, x)


if __name__ == '__main__':
	root = TreeNode(1, TreeNode(2), TreeNode(3))
	print(Solution().sumNumbers(root))