class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	def maxAncestorDiff(self, root):
		ans = 0
		def dfs(root, mx_pre, mn_pre):
			nonlocal ans
			if not root:
				return 
			ans = max(ans, abs(root.val - mx_pre), abs(root.val - mn_pre))
			mx_pre = max(mx_pre, root.val)
			mn_pre = min(mn_pre, root.val)
			dfs(root.left, mx_pre, mn_pre)
			dfs(root.right, mx_pre, mn_pre)
		dfs(root, root.val, root.val)
		return ans
## 自底向上写法 错解
class Solution:
	def maxAncestorDiff(self, root, ans=0, mx_pre=root.val, mn_pre=root.val):
		if not root:
			return ans
		ans = max(ans, abs(ans - mx_pre), abs(ans - mn_pre))
		mx_pre = max(mx_pre, root.val)
		mn_pre = min(mn_pre, root.val)
		left = self.maxAncestorDiff(root.left, ans, mx_pre, mn_pre)
		right = self.maxAncestorDiff(root.right, ans, mx_pre, mn_pre)
		return max(left, right)

if __name__ == '__main__':
	root = TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6, TreeNode(4), TreeNode(7))), TreeNode(10, None, TreeNode(14, TreeNode(13))))
	print(Solution().maxAncestorDiff(root))