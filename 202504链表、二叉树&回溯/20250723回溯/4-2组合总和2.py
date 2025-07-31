class Solution:
	def combinationSum2(self, candidates, target):
		candidates.sort()
		ans = []
		path = []
		n = len(candidates)
		def dfs(i):
			if sum(path) == target:
				ans.append(path.copy())
				return  # 这里如果不retur会导致后面不选但实际上相同的路径也被重复添加（取决于排序后最后选的那个数后面还有几个）
			if i == n or sum(path) > target:
				return
			## 选
			x = candidates[i]
			path.append(x)
			dfs(i + 1)
			path.pop()

			## 不选
			i += 1
			while i < n and candidates[i] == x:
				i += 1
			dfs(i)
		dfs(0)
		return ans
	
if __name__ == '__main__':
	candidates = [10,1,2,7,6,1,5]
	target = 8
	print(Solution().combinationSum2(candidates, target))