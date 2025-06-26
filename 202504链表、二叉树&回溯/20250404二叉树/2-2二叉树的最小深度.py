from math import inf

class TreeNode:
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

# 2.二叉树的最小深度
class Solution1:  # 错解-无法处理root为None的情况
	def minDepth(self, root):
		if not root:
			return inf
		elif root.left is None and root.right is None:
			return 1

		l_depth = self.minDepth(root.left)
		r_depth = self.minDepth(root.right)
		ans = min(l_depth, r_depth) + 1
		return ans if root else 0
## 灵神题解
class Solution2:  
	def minDepth(self, root):
		if not root:
			return 0
		elif root.left is None and root.right is None:
			return 1

		l_depth = self.minDepth(root.left) if root.left else inf
		r_depth = self.minDepth(root.right) if root.right else inf
		return min(l_depth, r_depth) + 1
## 灵神题解-自顶向下
class Solution3:
	def minDepth(self, root):
		ans = inf
		def dfs(root, cnt):
			if not root:
				return
			cnt += 1
			nonlocal ans
			# 优化：最优性剪枝
			if cnt >= ans:
				return 

			if root.left is None and root.right is None:
				ans = min(ans, cnt)
				return  # 再递归只会增大 
			dfs(root.left, cnt)
			dfs(root.right, cnt)
		dfs(root, 0)
		return ans if root else 0



if __name__ == '__main__':
	root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
	# root = TreeNode()
	print(Solution2().minDepth(root)) # Output: 2
	
