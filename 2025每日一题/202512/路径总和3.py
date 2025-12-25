from collections import defaultdict

class TreeNode:
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def pathSum(self, root, targetSum):
		ans = 0
		cnt = defaultdict(int)
		cnt[0] = 1

		def dfs(node, temp_s):
			if not node:
				return
			temp_s += node.val
			nonlocal ans
			ans += cnt[temp_s - targetSum]
			cnt[temp_s] += 1
			dfs(node.left, temp_s)
			dfs(node.right, temp_s)
			cnt[temp_s] -= 1
		dfs(root, 0)
		return ans


if __name__ == '__main__':
	root = TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, None, TreeNode(1))), TreeNode(-3, None, TreeNode(11)))
	targetSum = 8
	print(Solution().pathSum(root, targetSum)) # Output: 3