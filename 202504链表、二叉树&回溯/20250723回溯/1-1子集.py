class Solution:  # O(n2^n)
	def subsets(self, nums):
		n = len(nums)

		ans = []
		path = []
		def dfs(i):
			if i == n:
				ans.append(path.copy())  # 列表复制的复杂度是O(n)
				return

			dfs(i + 1)  # 不选的情况

			path.append(nums[i])
			dfs(i + 1)  # 选的情况
			path.pop()
		dfs(0)
		return ans

if __name__ == '__main__':
	nums = [1, 2, 3]
	print(Solution().subsets(nums))