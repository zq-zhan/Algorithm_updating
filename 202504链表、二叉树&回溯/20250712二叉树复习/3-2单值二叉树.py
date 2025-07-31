from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
		
# class Solution:
# 	def isUnivalTree(self, root, set_lis = set()):
# 		if not root:
# 			return len(set_lis) == 1
# 		if len(set_lis) > 1:
# 			return False
# 		set_lis.add(root.val)
# 		left = self.isUnivalTree(root.left, set_lis)
# 		right = self.isUnivalTree(root.right, set_lis)
# 		return left and right

class Solution:
	def isUnivalTree(self, root, dic_win = defaultdict(int)):
		if not root:
			return len(dic_win) == 1
		if len(dic_win) > 1:
			return False
		dic_win[root.val] += 1
		left = self.isUnivalTree(root.left, dic_win)
		right = self.isUnivalTree(root.right, dic_win)
		if dic_win[root.val] == 1:
			del dic_win[root.val]
		else:
			dic_win[root.val] -= 1
		return left and right
	
## 自顶向下
class Solution:
	def isUnivalTree(self, root):
		ans_set = set()
		def dfs(root):
			if not root:
				return
			ans_set.add(root.val)
			dfs(root.left)
			dfs(root.right)
		return len(ans_set) <= 1
	
class Solution:
	def isUnivalTree(self, root):
		v = root.val
		def dfs(node):
			return not node or (node.val == v and dfs(node.left) and dfs(node.right))
		return dfs(root)
	
if __name__ == '__main__':
    root = TreeNode(1, TreeNode(1, TreeNode(5), TreeNode(1)), TreeNode(1, None, TreeNode(1)))
    print(Solution().isUnivalTree(root))