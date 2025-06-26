from collections import defaultdict

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def pathSum(self, root, targetSum):
		ans = 0
		dic_win = defaultdict(int)
		dic_win[0] = 1
		def dfs(root, s):
			if not root:
				return 
			nonlocal ans
			s += root.val
			ans += dic_win[s - targetSum]
			dic_win[s] += 1
			dfs(root.left, s)
			dfs(root.right, s)
			dic_win[s] -= 1  # 恢复原状
		dfs(root, 0)
		return ans
	
if __name__ == '__main__':
	root = TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, None, TreeNode(1))), TreeNode(-3, None, TreeNode(11)))
	targetSum = 8
	print(Solution().pathSum(root, targetSum)) # Output: 3
