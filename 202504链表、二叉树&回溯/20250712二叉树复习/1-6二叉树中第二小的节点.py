class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	def findSecondMinimumValue(self, root):
		ans = []
		def dfs(root):
			if not root:
				return 
			if len(ans) < 2 and (not ans or root.val != ans[-1]):
				ans.append(root.val)
			elif ans[-1] > root.val and ans[0] != root.val:
				ans[-1] = root.val
			dfs(root.left)
			dfs(root.right)
		dfs(root)
		return ans[-1] if len(ans) == 2 else -1

if __name__ == '__main__':
	root = TreeNode(2, TreeNode(2), TreeNode(5, TreeNode(5), TreeNode(7)))
	print(Solution().findSecondMinimumValue(root))