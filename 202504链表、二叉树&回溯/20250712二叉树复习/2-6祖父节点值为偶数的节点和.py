class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	def sumEvenGrandparent(self, root):
		ans = 0
		def dfs(root, temp_lis):
			nonlocal ans
			if not root:
				return
			if not root.left and not root.right:
				return 
			temp_lis.append(root.val)
			if len(temp_lis) == 3 and temp_lis[-3] % 2 == 0:
				ans += root.val

			dfs(root.left, temp_lis)
			dfs(root.right, temp_lis)
			temp_lis.pop(-1)
		dfs(root, [])
		return ans


	
if __name__ == '__main__':
	root = TreeNode(6, TreeNode(7, TreeNode(2, TreeNode(9), None), TreeNode(7, TreeNode(1, TreeNode(4)))), TreeNode(8, TreeNode(1), TreeNode(3, None, TreeNode(5))))
	print(Solution().sumEvenGrandparent(root))