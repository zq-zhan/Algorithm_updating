# 1.二叉树的前序遍历
class TreeNode:
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right
## 递归写法  - 根-左-右
class Solution1:
	def preorderTraversal(self, root):
		res = []
		def dfs(root):
			if not root:
				return 
			ans.append(root.val)
			dfs(root.left)
			dfs(root.right)
		dfs(root)
		return res
## 迭代写法
class Solution2:
	def preorderTraversal(self, root):
		ans = []
		if not root:
			return ans
		stack = [root]
		while stack:
			node = stack.pop()
			ans.append(node.val)
			if node.right:
				stack.append(node.right)  # 栈-先入后出
			if node.left:
				stack.append(node.left)
		return ans

# 2.二叉树的中序遍历
class Solution:  # 左-根-右
	def inorderTraversal(self, root):
		ans = []
		def dfs(root):
			if not root:
				return 
			dfs(root.left)
			ans.append(root.val)
			dfs(root.right)
		dfs(root)
		return ans


# 3.二叉树的后序遍历
class Solution: # 左-右-根
	def postorderTraversal(self, root):
		ans = []
		def dfs(root):
			if not root:
				return 
			dfs(root.left)
			dfs(root.right)
			ans.append(root.val)
		dfs(root)
		return ans

# 4.叶子相似的树
class Solution1:
	def leafSimilar(self, root1, root2):
		def pass_read(root, ans):
			# ans = []
			def dfs(root):
				if not root:
					return 
				if root.left is None and root.right is None:
					ans.append(root.val)
				dfs(root.left)
				dfs(root.right)
			dfs(root)
			return ans

		return pass_read(root1,[]) == pass_read(root2,[])
## DFS-递归
class Solution1:
	def leafSimilar(self, root1, root2):
		ans1 = []
		ans2 = []

		def dfs(root, result):
			if not root:
				return
			if root.left is None and root.right is None:
				result.append(root.val)
			dfs(root.left, result)
			dfs(root.right, result)

		dfs(root1, ans1)
		dfs(root2, ans2)
		return ans1 == ans2

# 5.开幕式的焰火
class Solution1:
	def numColor(self, root):
		ans = set()

		def dfs(root):
			if not root:
				return 
			ans.append(root.val)
			dfs(root.left)
			dfs(root.right)
		dfs(root)
		return len(ans)

# 6.左叶子之和
class Solution1:
	def sumOfLeftLeaves(self, root):
		ans = 0
		def dfs(root, tag):
			if not root:
				return 
			if root.left is None and root.right is None and tag == 'left':
				ans += root.val
			dfs(root.left, 'left')
			dfs(root.right, 'right')
		dfs(root, 'right')
		return ans

# 7.二叉树中第二小的节点
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

########################### 自顶向下DFS #################
# 1.二叉树的最大深度
## 自顶向下遍历
class Solution1:
	def maxDepth(self, root):
		ans = 0

		def dfs(root, length):
			nonlocal ans
			if not root:
				return 
			length += 1
			ans = max(ans, length)
			dfs(root.left, length)
			dfs(root.right, length)
		dfs(root, 0)
		return ans
## 自底向上遍历
class Solution2:
	def maxDepth(self, root):
		if not root:
			return 0

		l_maxdepth = self.maxDepth(root.left)
		r_maxdepth = self.maxDepth(root.right)
		return max(l_maxdepth, r_maxdepth) + 1

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

		l_depth = self.minDepth(root.left) if root.left else inf  # 左儿子不是空节点则递归，否则为inf
		r_depth = self.minDepth(root.right) if root.right else inf
		return min(l_depth, r_depth) + 1
## 灵神题解-自顶向下
class Solution2:
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

# 3.路径总和
class Solution1:
	def hasPathSum(self, root, targetSum):
		result = False
		def dfs(root, ans):
			nonlocal result
			if not root:
				return
			ans += root.val
			if root.left is None and root.right is None and ans == targetSum:
				result = True
				return
			dfs(root.left, ans)
			dfs(root.right, ans)
		dfs(root, 0)
		return result
## 灵神题解
class Solution2:
	def hasPathSum(self, root, targetSum):
		if not root:
			return False
		targetSum -= root.val
		if root.left is None and root.right is None:
			return targetSum == 0
		return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

# 4.求根节点到叶节点数字之和
class Solution1:
	def sumNumbers(self, root):
		ans = 0
		def dfs(root, cnt):
			if not root:
				return 
			cnt += str(root.val)
			nonlocal ans
			if root.left is None and root.right is None:
				ans += int(cnt)
			dfs(root.left, cnt)
			dfs(root.right, cnt)
		dfs(root, '')
		return ans
## 自底向下写法
class Solution2:
	def sumNumbers(self, root, x = 0):
		if not root:
			return 0
		x = x * 10 + root.val
		if root.left is None and root.right is None:
			return x
		return self.sumNumbers(root.left, x) + self.sumNumbers(root.right, x)
##
class Solution2:
	def sumNumbers(self, root, x = ''):
		if not root:
			return 0
		x += str(root.val)
		if root.left is None and root.right is None:
			return int(x)
		return self.sumNumbers(root.left, x) + self.sumNumbers(root.right, x)

# 5.二叉树的右视图
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

# 6.统计二叉树中好节点的数目
class Solution1:
	def goodNodes(self, root):
		ans = 0
		def dfs(root, num):
			if not root:
				return 
			# if root.left is None and root.right is None:
			nonlocal ans
			ans += 1 if root.val >= num else 0
			num = max(root.val, num)
			dfs(root.left, num)
			dfs(root.right, num)
		dfs(root, -inf)
		return ans

## 自底向上写法
class Solution2:
	def goodNodes(self, root, ans = 0, num = -inf):
		if not root:
			return ans
		ans += 1 if root.val >= num else 0
		# if root.left is None and root.right is None:
		# 	return 1 
		num = max(num, root.val)
		return self.goodNodes(root.left, num) + self.goodNodes(root.right, num)
## 自底向上-灵神题解
class Solution3:
	def goodNodes(self, root, num = -inf):
		if not root:
			return 0
		left = self.goodNodes(root.left, max(num, root.val))
		right = self.goodNodes(root.right, max(num, root.val))
		return left + right + (num <= root.val)

# 7.二叉树中的伪回文路径
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
			temp_dic[root.val] -= 1  # 可变对象、需要回溯
		dfs(root, temp_ans)
		return ans
##
class Solution2:
	def pseudoPalindromicPaths(self, root, temp_dic = defaultdict(int)):
		if not root:
			return 0
		temp_dic[root.val] += 1
		if root.left is None and root.right is None:
			cnt = 0
			for val in temp_ans:
				cnt += 1 if temp_ans[val] % 2 == 1 else 0
			temp_ans[root.val] -= 1
			return cnt <= 1
		return self.pseudoPalindromicPaths(root.left, temp_dic) + self.pseudoPalindromicPaths(root.right, temp_dic)

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
## 
class Solution2:
	def sumEvenGrandparent(self, root):
		ans = 0
		def dfs(root, parent_val, grandparent_val):
			if not root:
				return 
			nonlocal ans
			if grandparent_val % 2 == 0:
				ans += root.val
			new_parent_val = root.val
			dfs(root.left, root.val, parent_val)
			dfs(root.right, root.val, parent_val)
		dfs(root, -1, -1)
		return ans

# 9.从叶节点开始的最小字符串
class Solution2:
	def smallestFromLeaf(self, root):
		ans = 'z' * 8500
		ori = ord('a')
		def dfs(root, char):
			if not root:
				return
			char += chr(root.val + ori)
			if root.left is None and root.right is None:
				nonlocal ans
				# if len(ans) > len(char):
				# 	ans = char[::-1]
				# elif len(ans) == len(char) and ans > char[::-1]:
				# 	ans = char[::-1]
				if ans > char[::-1]:
					ans = char[::-1]
			dfs(root.left, char)
			dfs(root.right, char)
		dfs(root, '')
		return ans

# 10.节点与其祖先的最大差值
class Solution1:
	def maxAncestorDiff(self, root):
		ans = 0
		def dfs(root, min_val, max_val):
			if not root:
				return 
			nonlocal ans
			ans = max(ans, abs(min_val - root.val), abs(max_val - root.val))
			min_val = min(min_val, root.val)
			max_val = max(max_val, root.val)
			dfs(root.left, min_val, max_val)
			dfs(root.right, min_val, max_val)
		dfs(root, root.val, root.val)
		return ans
## 灵神优化思路
class Solution2:
	def maxAncestorDiff(self, root):
		ans = 0
		def dfs(root, mn, mx):
			if not root:
				nonlocal ans
				ans = max(ans, mx - mn)
				return
			mn = min(mn, root.val)
			mx = max(mx, root.val)
			dfs(root.left, mn, mx)
			dfs(root.right, mn, mx)
		dfs(root, root.val, root.val)
		return ans









