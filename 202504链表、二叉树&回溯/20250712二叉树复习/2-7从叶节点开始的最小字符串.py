class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	def smallestFromLeaf(self, root):
		ans = 'z' * 8500
		ord_a = ord('a')
		def dfs(root, temp_str):
			nonlocal ans
			if not root:
				return 
			temp_str = chr(root.val + ord_a) + temp_str
			if not root.left and not root.right:
				if len(temp_str) < len(ans):
					ans = temp_str
				elif len(temp_str) == len(ans) and temp_str < ans:
					ans = temp_str
			dfs(root.left, temp_str)
			dfs(root.right, temp_str)
		dfs(root, '')
		return ans
	
if __name__ == '__main__':
	root = TreeNode(0, TreeNode(1, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(5), TreeNode(6)))
	print(Solution().smallestFromLeaf(root))