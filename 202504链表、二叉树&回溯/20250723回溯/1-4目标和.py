class Solution:
	def findTargetSumWays(self, nums, target):
		ans = path = 0
		n = len(nums)
		def dfs(i):
			nonlocal ans, path
			if i == n:
				if path == target:
					ans += 1
				return

			path += nums[i]  # + 的情况
			dfs(i + 1)
			path -= nums[i]

			path -= nums[i]  # - 的情况
			dfs(i + 1)
			path += nums[i]
		dfs(0)
		return ans
	
if __name__ == '__main__':
	nums = [1, 1, 1, 1, 1]
	target = 3
	print(Solution().findTargetSumWays(nums, target))