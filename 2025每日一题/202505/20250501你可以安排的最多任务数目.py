from functools import cache
from collections import deque

# 20250501你可以安排的最多任务数目
class Solution1:
	def maxTaskAssign(self, tasks, workers, pills, strength):
		tasks.sort()
		workers.sort(reverse = True)
		n, m = len(tasks), len(workers)
		@cache
		def dfs(i, j, c):
			if i >= n or j >= m:
				return 0
			if workers[j] >= tasks[i]:
				return dfs(i + 1, j + 1, c) + 1
			elif workers[j] < tasks[i] and c < pills and workers[j] + strength >= tasks[i]:
				return max(dfs(i + 1, j + 1, c + 1) + 1, dfs(i, j + 1, c))
			else:
				return dfs(i, j + 1, c)
		return dfs(0, 0, 0)
	
"""
本题核心在于想到对应的贪心策略
"""
## 灵神题解
class Solution2:
	def maxTaskAssign(self, tasks, workers, pills, strength):
		tasks.sort()
		workers.sort()

		def check(k):
			# 贪心思路：用最强的k名工人，完成最简单的k个任务，检查是否能完成
			i, p = 0, pills
			valid_task = deque()
			for w in workers[-k:]:
				while i < k and tasks[i] <= w + strength:
					valid_task.append(tasks[i])
					i += 1
				if not valid_task:
					return False
				if w >= valid_task[0]:
					valid_task.popleft()
					continue
				if p == 0:
					return False
				p -= 1
				valid_task.pop()
			return True

		left, right = 0, min(len(workers), len(tasks)) + 1
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				left = mid
			else:
				right = mid
		return left

	
if __name__ == '__main__':
	tasks = [5,9,8,5,9]
	workers = [1,6,4,2,6]
	pills = 1
	strength = 5
	print(Solution1().maxTaskAssign(tasks, workers, pills, strength)) # Output: 2
	