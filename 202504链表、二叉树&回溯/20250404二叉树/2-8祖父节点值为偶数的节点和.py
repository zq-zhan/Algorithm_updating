class TreeNode:
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

# 8.祖父节点值为偶数的节点和
class Solution1:
	def sumEvenGrandparent(self, root):
		ans = 0
		def dfs(root, temp_lis):
			if not root:
				return
			if len(temp_lis) == 2:
				val = temp_lis.pop(0)
				if val % 2 == 0:
					nonlocal ans
					ans += root.val
			temp_lis.append(root.val)
			dfs(root.left, temp_lis)  # 错解，temp_lis是可变对象，每次调用dfs都会改变temp_lis，导致结果错误
			dfs(root.right, temp_lis)
		dfs(root, [])
		return ans
	
class Solution2:
	def sumEvenGrandparent(self, root):
		ans = 0
		def dfs(root, grandParentVal):
			if not root:
				return
			nonlocal ans
			flag = 1 if grandParentVal % 2 == 0 else 0
			if root.left:
				ans += root.left.val * flag
				dfs(root.left, root.val)
			if root.right:
				ans += root.right.val * flag
				dfs(root.right, root.val)
		dfs(root.left, root.val)
		dfs(root.right, root.val)
		return ans
	
## 
class Solution3:
	def sumEvenGrandparent(self, root):
		ans = 0
		def dfs(root, parent_val, grandparent_val):
			if not root:
				return 
			nonlocal ans
			if grandparent_val % 2 == 0:
				ans += root.val
			dfs(root.left, root.val, parent_val)
			dfs(root.right, root.val, parent_val)
		dfs(root, -1, -1)
		return ans


if __name__ == '__main__':
	root = TreeNode(6, TreeNode(7, TreeNode(2, TreeNode(9)), TreeNode(7, TreeNode(1), TreeNode(4))), TreeNode(8, TreeNode(1), TreeNode(3,None,TreeNode(5))))
	print(Solution3().sumEvenGrandparent(root))