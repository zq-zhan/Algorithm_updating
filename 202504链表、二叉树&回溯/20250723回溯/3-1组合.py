class Solution:
	def combine(self, n, k):
		ans = []
		path = []
		def dfs(i):
			if i == n:
				if len(path) == k:
					ans.append(path.copy())
				return
			dfs(i + 1)  # 不选
			if len(path) < k:
				path.append(i + 1)
				dfs(i + 1)  # 选
				path.pop()  # 恢复现场
		dfs(0)
		return ans
	
if __name__ == '__main__':
	n = 4
	k = 2
	s = Solution()
	print(s.combine(n, k))