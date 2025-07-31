class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	def kthLargestPerfectSubtree(self, root, k):
		ans = []
		def dfs(node):
			if not node:
				return 0, 0
			if node.left and node.right:
				tag = True
			else:
				tag = False
			l_depth, l_cnt = dfs(node.left)
			r_depth, r_cnt = dfs(node.right)
			if tag and l_depth == r_depth:
				ans.append(l_cnt + r_cnt + 1)
			return max(l_depth, r_depth) + 1, l_cnt + r_cnt + 1
		dfs(root)
		ans.sort()
		return ans[-k]
	

if __name__ == '__main__':
	root = TreeNode(5, TreeNode(3, TreeNode(5, TreeNode(1), TreeNode(8)), TreeNode(2)), TreeNode(6, TreeNode(5, TreeNode(6), TreeNode(8)), TreeNode(7)))
	k = 2
	print(Solution().kthLargestPerfectSubtree(root, k))