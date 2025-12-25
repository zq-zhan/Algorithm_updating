class TreeNode:
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def sortedArrayToBST(self, nums):
		if not nums:
			return None
		m = len(nums) // 2
		left = self.sortedArrayToBST(nums[:m])
		right = self.sortedArrayToBST(nums[m + 1:])
		return TreeNode(nums[m], left, right)

## 写法二
class Solution:
    def sortedArrayToBST(self, nums):
        def dfs(left, right):
            if left > right:
                return None
            m = (left + right) // 2
            return TreeNode(nums[m], dfs(left, m - 1), dfs(m + 1, right))
        return dfs(0, len(nums) - 1)

if __name__ == '__main__':
	nums = [-10,-3,0,5,9]
	print(Solution().sortedArrayToBST(nums))