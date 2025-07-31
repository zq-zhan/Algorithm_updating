class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

## 后序遍历+剪枝
# class Solution:
# 	def isBalanced(self, root):
# 		def get_height(node):
# 			if not node:
# 				return 0
# 			left_height = get_height(node.left)
# 			if left_height == -1:
# 				return -1
# 			right_height = get_height(node.right)
# 			if right_height == -1 or abs(left_height - right_height) > 1:
# 				return -1
# 			return max(left_height, right_height) + 1
# 		return get_height(root) != 1
	
## 先序遍历+判断深度
class Solution:
	def isBalanced(self, root):
		if not root:
			return True
		return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and \
			self.isBalanced(root.left) and self.isBalanced(root.right)

	def depth(self, root):
		if not root:
			return 0
		return max(self.depth(root.left), self.depth(root.right)) + 1



if __name__ == '__main__':
	root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
	print(Solution().isBalanced(root))