class Solution:
	def maxTotalFruits(self, fruits, startPos, k):
		mx = max(x[0] for x in fruits)
		fruits_lis = [0] * (mx + 1)
		for order, cnt in fruits:
			fruits_lis[order] += cnt	
		ans = path = 0
		def dfs(i, k):
			nonlocal ans, path
			if not (0 <= i <= mx) or k < 0:
				return
			x = fruits_lis[i]
			path += x
			fruits_lis[i] = 0
			ans = max(ans, path)

			dfs(i - 1, k - 1)
			dfs(i + 1, k - 1)

			# 回溯
			path -= x
			fruits_lis[i] = x
		dfs(startPos, k)
		return ans
	
if __name__ == '__main__':
	fruits = [[2,8],[6,3],[8,6]]
	startPos = 5
	k = 4
	print(Solution().maxTotalFruits(fruits, startPos, k))