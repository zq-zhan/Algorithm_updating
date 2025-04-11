from collections import defaultdict,Counter

class TreeNode:
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

class Solution1:
	def pseudoPalindromicPaths(self, root):
		temp_ans = defaultdict(int)
		ans = 0
		def dfs(root, temp_dic):
			if not root:
				return 
			nonlocal ans		
			temp_dic[root.val] += 1
			if root.left is None and root.right is None:
				cnt = 0
				for val in temp_dic:
					cnt += 1 if temp_dic[val] % 2 == 1 else 0
				ans += 1 if cnt <= 1 else 0
			dfs(root.left, temp_dic)
			dfs(root.right, temp_dic)
			temp_dic[root.val] -= 1
		dfs(root, temp_ans)
		return ans
##
##
class Solution2:
	def pseudoPalindromicPaths(self, root, temp_dic = defaultdict(int)):
		if not root:
			return 0
		temp_dic[root.val] += 1
		if root.left is None and root.right is None:
			cnt = 0
			for val in temp_dic:
				cnt += 1 if temp_dic[val] % 2 == 1 else 0
			temp_dic[root.val] -= 1
			return cnt <= 1
		return self.pseudoPalindromicPaths(root.left, temp_dic) + self.pseudoPalindromicPaths(root.right, temp_dic)


if __name__ == '__main__':
	root = TreeNode(2, TreeNode(3, TreeNode(3), TreeNode(1)), TreeNode(1, None, TreeNode(1)))
	print(Solution2().pseudoPalindromicPaths(root))