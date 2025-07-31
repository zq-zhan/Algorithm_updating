class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	def isSameTree(self, p, q):
		if not p and not q:
			return True
		elif (not p and q) or (p and not q) or (p.val != q.val):
			return False
		left = self.isSameTree(p.left, q.left)
		right = self.isSameTree(p.right, q.right)
		return left and right
	
if __name__ == '__main__':
	p = TreeNode(1, TreeNode(2), TreeNode(3))
	q = TreeNode(1, TreeNode(2), TreeNode(3))
	print(Solution().isSameTree(p, q))