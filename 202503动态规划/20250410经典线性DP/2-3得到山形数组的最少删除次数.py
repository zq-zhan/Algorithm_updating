from bisect import bisect_left

class Solution1:  # 错解
	def minimumMountainRemovals(self, nums):
		n = len(nums)
		def dfs(i):
			left = 0
			for j in range(i):
				if nums[j] < nums[i]:
					left = max(left, dfs(j))
			right = 0
			for k in range(i + 1, n):
				if nums[k] < nums[i]:
					right = max(right, dfs(k))
			return right + left + 1
		return n - max(dfs(i) for i in range(n))
## 灵神题解
class Solution2:
	def minimumMountainRemovals(self, nums):
		n = len(nums)
		suf = [0] * n
		g = []
		for i in range(n - 1, 0, -1):
			x = nums[i]
			j = bisect_left(g, x)
			if j == len(g):
				g.append(x)
			else:
				g[j] = x
			suf[i] = len(g)  # 从nums[i]开始的最长严格递减子序列的长度

		mx = 0  # 最长山形子序列的长度
		g = []
		for i, x in enumerate(nums):
			j = bisect_left(g, x)
			if j == len(g):
				g.append(x)
			else:
				g[j] = x
			pre = j + 1  # 以nums[i]结尾的最长严格递增子序列的长度
			if pre >= 2 and suf[i] >= 2:  # 不一定要等长
				mx = max(mx, pre + suf[i] - 1)
		return n - mx
	
if __name__ == '__main__':
	nums = [2,1,1,5,6,2,3,1]
	print(Solution2().minimumMountainRemovals(nums))