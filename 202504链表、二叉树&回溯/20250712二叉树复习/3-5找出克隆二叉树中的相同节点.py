class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	def getTargetCopy(self, original, cloned, target):
		ans = ''
		def dfs(cloned):
			if not cloned:
				return
			elif cloned.val == target.val:
				nonlocal ans
				ans = cloned
				return
			dfs(cloned.left)
			dfs(cloned.right)
		dfs(cloned)
		return ans


## 灵神题解
class Solution:
	def getTargetCopy(self, original, cloned, target):
		if original is None or original is target:
			return cloned
		return self.getTargetCopy(original.left, cloned.left, target) or \
			self.getTargetCopy(original.right, cloned.right, target)

if __name__ == '__main__':
	original = TreeNode(7, TreeNode(4), TreeNode(3, TreeNode(6, TreeNode(19))))
	cloned = TreeNode(7, TreeNode(4), TreeNode(3, TreeNode(6, TreeNode(19))))
	target = TreeNode(3)
	print(Solution().getTargetCopy(original, cloned, target))