from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
# 	def findFrequentTreeSum(self, root):
# 		if not root.left and not root.right:
# 			return [root.val]
# 		dic_win = defaultdict(int)
# 		def get_sum(root):
# 			if not root:
# 				return 0
# 			# if not root.left and not root.right:
# 			# 	return root.val
# 			left = get_sum(root.left)
# 			if left != 0:
# 				dic_win[left] += 1
# 			right = get_sum(root.right)
# 			if right != 0:
# 				dic_win[right] += 1
# 			dic_win[left + right + root.val] += 1
# 		get_sum(root)
# 		mx_cnt = max(cnt for _, cnt in dic_win.items())
# 		ans = []
# 		for key, val in dic_win.items():
# 			if val == mx_cnt:
# 				ans.append(key)
# 		return ans


class Solution:
	def findFrequentTreeSum(self, root):
		if not root:
			return []

		dic_win = defaultdict(int)
		def get_sum(node):
			if not node:
				return 0
			left = get_sum(node.left)
			right = get_sum(node.right)
			curr_sum = left + right + node.val
			dic_win[curr_sum] += 1
			return curr_sum
		get_sum(root)
		mx_cnt = max(dic_win.values())
		return [s for s, cnt in dic_win.items() if cnt == mx_cnt]
	
if __name__ == '__main__':
	root = TreeNode(5, TreeNode(2))
	s = Solution()
	print(s.findFrequentTreeSum(root))