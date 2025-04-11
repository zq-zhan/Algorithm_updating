from collections import deque

# 5.二叉树的右视图
class TreeNode:
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

class Solution1:
	def rightSideView(self, root):
		ans = []
		def dfs(root, tag):
			if not root:
				return 
			if tag == 'right':
				nonlocal ans
				ans.append(root.val)
			dfs(root.left, 'left')
			dfs(root.right, 'right')
		dfs(root, 'right')
		return ans

## 灵神题解-DFS
class Solution2:
	def rightSideView(self, root):
		ans = []
		def dfs(root, depth):
			if not root:
				return 
			if depth == len(ans):  #该深度第一次遇到
				ans.append(root.val)
			dfs(root.right, depth + 1)  # 先递归右子树，保证首次遇到的一定是最右边的节点
			dfs(root.left, depth + 1)
		dfs(root, 0)
		return ans
	

## 层序遍历
class LeverOrder():
	def levelOrder(self, root):
		if not root:
			return []
		ans = []
		queue = deque([root])
		while queue:
			level_size = len(queue)
			current_level = []
			for _ in range(level_size):
				node = queue.popleft()
				if node.val:
					current_level.append(node.val)
				if node.left:
					queue.append(node.left)
				if node.right:
					queue.append(node.right)
			ans.append(current_level)
		return ans
	
## 层序遍历解法
class Solution3():
	def rightSideView(self, root):
		if not root:
			return []
		ans = []
		queue = deque([root])
		while queue:
			level_size = len(queue)
			for i in range(level_size):
				node = queue.popleft()
				if i == level_size - 1:
					ans.append(node.val)
				if node.left:
					queue.append(node.left)
				if node.right:
					queue.append(node.right)
		return ans



if __name__ == '__main__':
	root = TreeNode(1, TreeNode(2, TreeNode(None), TreeNode(5)), TreeNode(3, TreeNode(None), TreeNode(4)))
	print(Solution3().rightSideView(root))
	# print(LeverOrder().levelOrder(root))