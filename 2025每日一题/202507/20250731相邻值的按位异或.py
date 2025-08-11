class Solution:
	def doesValidArrayExist(self, derived):
		n = len(derived)
		path = [0] * n
		ans = False
		def dfs(i, path):
			nonlocal ans
			if i == 0:
				if path[0] ^ path[1] == derived[0]:
					ans = True
				return
			if path[i] ^ path[(i + 1)%n] != derived[i]:
				return 

			## 选1
			path[i] = 1
			dfs(i - 1, path)

			## 不选1
			dfs(i - 1, path)
		dfs(n - 1, path)
		return ans
			

if __name__ == '__main__':
	derived = [1,1,0]
	print(Solution().doesValidArrayExist(derived))