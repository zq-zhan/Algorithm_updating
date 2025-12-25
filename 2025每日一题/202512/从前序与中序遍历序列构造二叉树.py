class TreeNode:
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

## 灵神题解——递归
class Solution:
	def buildTree(self, preorder, inorder):
		if not preorder:
			return None
		left_size = inorder.index(preorder[0]) # 左子树大小
		left = self.buildTree(preorder[1:1+left_size], inorder[:left_size])
		right = self.buildTree(preorder[1+left_size:], inorder[1+left_size:])
		return TreeNode(preorder[0], left, right)
	
if __name__ == '__main__':
	preorder = [3,9,20,15,7]
	inorder = [9,3,15,20,7]
	root = Solution().buildTree(preorder, inorder)