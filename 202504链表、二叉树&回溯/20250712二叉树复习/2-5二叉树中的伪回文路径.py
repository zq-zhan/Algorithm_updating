from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	def pseudoPalindromicPaths(self, root):
		ans = 0
		def dfs(root, temp_dic):
			nonlocal ans
			if not root:
				return
			temp_dic[root.val] += 1
			if not root.left and not root.right:
				cnt = 0
				for key, val in temp_dic.items():
					if val % 2:
						cnt += 1
					if cnt > 1:
						break
				ans += (cnt <= 1)
			dfs(root.left, temp_dic)
			dfs(root.right, temp_dic)
			temp_dic[root.val] -= 1
		dfs(root, defaultdict(int))
		return ans

	
if __name__ == '__main__':
	root = TreeNode(2, TreeNode(3, TreeNode(3), TreeNode(1)), TreeNode(1, None, TreeNode(1)))
	print(Solution().pseudoPalindromicPaths(root))