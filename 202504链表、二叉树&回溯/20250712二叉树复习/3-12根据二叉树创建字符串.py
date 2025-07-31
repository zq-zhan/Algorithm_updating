class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	def tree2str(self, root):
		ans = ''
		def dfs(node):
			nonlocal ans
			if not node:
				return
			ans += str(node.val) + '('
			dfs(node.left)
			dfs(node.right)
			ans += ')'
		dfs(root)
		result = []
		for i in range(1, len(ans)):
			if ans[i] == ')' and result[i - 1] == '(':
				result.pop()
			else:
				result.append(ans[i])
		return ''.join(result)
	
if __name__ == '__main__':
	root = TreeNode(1, TreeNode(2, TreeNode(4), None), TreeNode(3))
	print(Solution().tree2str(root)) # Output: "1(2(4))(3)"