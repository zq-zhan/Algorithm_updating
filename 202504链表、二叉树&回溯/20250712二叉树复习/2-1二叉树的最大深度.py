class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	def maxDepth(self, root):
		ans = 0
		def dfs(root, length):
			if not root:
				return 
			length += 1
			nonlocal ans
			ans = max(ans, length)
			dfs(root.left, length)
			dfs(root.right, length)
		dfs(root, 0)
		return ans
	
## 自底向上遍历
class Solution:
	def maxDepth(self, root):
		if not root:
			return 0
		l_maxdepth = self.maxDepth(root.left)
		r_maxdepth = self.maxDepth(root.right)
		return max(l_maxdepth, r_maxdepth) + 1
	
	
if __name__ == '__main__':
	tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
	print(Solution().maxDepth(tree))