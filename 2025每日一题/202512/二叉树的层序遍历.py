from collections import defaultdict

class TreeNode:
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right
		

class Solution:
	def levelOrder(self, root):
		ans = defaultdict(list)
		def dfs(root, depth):
			if not root:
				return 
			ans[depth].append(root.val)
			dfs(root.left, depth + 1)
			dfs(root.right, depth + 1)
		dfs(root, 0)
		new_ans = []
		for depth, lis in ans.items():
			new_ans.append(lis)
		return new_ans

class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        ans = []
        cur = [root]
        while cur:
            nxt = []
            vals = []
            for node in cur:
                vals.append(node.val)
                if node.left:  nxt.append(node.left)
                if node.right: nxt.append(node.right)
            cur = nxt
            ans.append(vals)
        return ans

if __name__ == '__main__':
	root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
	print(Solution().levelOrder(root))