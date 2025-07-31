from math import inf

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

## 自底向上——归
class Solution:
	def maxAncestorDiff(self, root):
		ans = 0
		def dfs(node):
			if not node:
				return inf, -inf
			l_mn, l_mx = dfs(node.left)
			r_mn, r_mx = dfs(node.right)
			mn = min(node.val, l_mn, r_mn)
			mx = max(node.val, l_mx, r_mx)
			nonlocal ans
			ans = max(ans, node.val - mn, mx - node.val)
			return mn, mx
		dfs(root)
		return ans
	
if __name__ == '__main__':
	root = TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6, TreeNode(4), TreeNode(7))), TreeNode(10, None, TreeNode(14, TreeNode(13))))
	print(Solution().maxAncestorDiff(root)) # 7