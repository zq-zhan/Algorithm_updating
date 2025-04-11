class TreeNode:
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

class Solution1:
	def findSecondMinimumValue(self, root):
		ans = set()
		# heapq.heapify(ans)

		def dfs(root):
			nonlocal ans
			if not root:
				return
			ans.add(root.val)
			dfs(root.left)
			dfs(root.right)
		dfs(root)
		ans = sorted(list(ans))
		return ans[1] if len(ans) >= 2 else -1

if __name__ == '__main__':
	root = TreeNode(2, TreeNode(2), TreeNode(5, TreeNode(5), TreeNode(7)))
	print(Solution1().findSecondMinimumValue(root)) # Output: 5