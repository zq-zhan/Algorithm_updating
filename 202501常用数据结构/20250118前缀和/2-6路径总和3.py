# 6.路径总和3
from collections import defaultdict

class TreeNode:
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right
	def fromList(arr):
		if not arr:
			return None
		root = TreeNode(arr[0])
		queue = [root]
		i = 1
		while i < len(arr):
			node = queue[0]
			del queue[0]
			if arr[i] is not None:
				node.left = TreeNode(arr[i])
				queue.append(node.left)
			i += 1
			if i < len(arr) and arr[i] is not None:
				node.right = TreeNode(arr[i])
				queue.append(node.right)
			i += 1
		return root

class Soliution1:
	def pathSum(self, root, targetSum):
		pre_sum = [0] * (len(root) + 1)
		for i, c in enumerate(root):
			pre_sum[i + 1] = pre_sum[i] + c

		ans = 0
		cnt = defaultdict(int)
		for sj in pre_sum:
			ans += cnt[sj - targetSum]
			cnt[sj] += 1
		return ans
	
## 灵神题解：递归二叉树的左子树和右子树
class Solution2:
	def pathSum(self, root, targetSum):
		ans = 0
		cnt = defaultdict(int)
		cnt[0] = 1

		def dfs(node, s):
			if node is None:
				return 
			nonlocal ans
			s += node.val
			ans += cnt[s - targetSum]
			cnt[s] += 1
			dfs(node.left, s)
			dfs(node.right, s)
			cnt[s] -= 1
		dfs(root, 0)
		return ans
	
if __name__ == '__main__':
	arr = [10,5,-3,3,2,None,11,3,-2,None,1]
	root = TreeNode.fromList(arr)
		
	# root = TreeNode(10)
	targetSum = 8
	cls = Solution2()
	print(cls.pathSum(root, targetSum))