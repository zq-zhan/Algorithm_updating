class Solution:
	def combinationSum3(self, k, n):
		ans = []
		path = []
		def dfs(i):
			diff = n - sum(path)
			if diff == 0 and len(path) == k:
				ans.append(path.copy())
				return
			if i == 10 or sum(path) > n or len(path) > k:
				return

			dfs(i + 1)  # 不选
			path.append(i)
			dfs(i + 1)  # 选
			path.pop()
		dfs(1)
		return ans

if __name__ == '__main__':
	k = 3
	n = 7
	print(Solution().combinationSum3(k, n))