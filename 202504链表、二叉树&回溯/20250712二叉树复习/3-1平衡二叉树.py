class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	def isBalanced(self, root):
		def get_height(node):
			if not node:
				return 0
			left_height = get_height(node.left)
			if left_height == -1:
				return -1
			right_height = get_height(node.right)
			if right_height == -1 or abs(left_height - right_height) > 1:
				return -1
			return max(left_height, right_height) + 1
		return get_height(root) != -1
	
if __name__ == '__main__':
	root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
	print(Solution().isBalanced(root)) # True