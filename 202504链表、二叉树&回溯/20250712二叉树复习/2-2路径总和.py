class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	def hasPathSum(self, root, target):
		ans = False
		def dfs(root, temp_s):
			if not root:
				return
			temp_s += root.val
			if not root.left and not root.right:
				nonlocal ans
				ans |= (temp_s == target)
			dfs(root.left, temp_s)
			dfs(root.right, temp_s)
		dfs(root, 0)
		return ans

## 自底向上遍历
class Solution:
	def hasPathSum(self, root, target):
		if not root:
			return False
		if not root.left and not root.right:
			return target == root.val
		l_sum = self.hasPathSum(root.left, target - root.val)
		r_sum = self.hasPathSum(root.right, target - root.val)
		return l_sum | r_sum
	
if __name__ == '__main__':
	root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
	target = 22
	print(Solution().hasPathSum(root, target))