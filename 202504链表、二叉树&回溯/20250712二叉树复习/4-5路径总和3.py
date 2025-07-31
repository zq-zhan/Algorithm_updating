from collections import Counter, defaultdict
from itertools import accumulate

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	def pathSum(self, root, targetSum):
		ans = 0
		path = [0]
		def dfs(node):
			nonlocal ans 
			if not node:
				pre_s_dic = Counter(pre_s)
				for x in pre_s:
					pre_s_dic[x] -= 1
					ans += pre_s_dic[x + targetSum]
					# pre_s_dic[x] += 1
				return
			path.append(node.val + path[-1])
			dfs(node.left)
			dfs(node.right)
			path.pop()
		dfs(root)
		return ans
## 上面错解的修改
class Solution:
    def pathSum(self, root, targetSum):
        self.ans = 0
        path = [0]  # 初始前缀和为0（模拟从根之前的空路径）

        def dfs(node):
            if not node:
                return

            # 当前路径和 = 父路径和 + 当前值
            curr_sum = path[-1] + node.val
            path.append(curr_sum)

            # 枚举前缀，判断是否有 curr_sum - old_sum == targetSum
            for pre_sum in path[:-1]:  # 排除当前的自己
                if curr_sum - pre_sum == targetSum:
                    self.ans += 1

            # 递归左右子树
            dfs(node.left)
            dfs(node.right)

            path.pop()  # 回溯

        dfs(root)
        return self.ans

## 灵神题解
class Solution:
	def pathSum(self, root, targetSum):
		ans = 0
		cnt = defaultdict(int)
		cnt[0] = 1
		def dfs(node, s):
			if not node:
				return
			nonlocal ans
			s += node.val  # 把node当作路径的重点，统计有多少个起点
			ans += cnt[s - targetSum]
			cnt[s] += 1
			dfs(node.left, s)
			dfs(node.right, s)
			cnt[s] -= 1
		dfs(root, 0)
		return ans

	
if __name__ == '__main__':
	root = TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, None, TreeNode(1))), TreeNode(-3, None, TreeNode(11)))
	targetSum = 8
	print(Solution().pathSum(root, targetSum))