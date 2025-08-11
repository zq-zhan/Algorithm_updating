from functools import cache

class Solution:
	def kConcatenationMaxSum(self, arr, k):
		mod = 10 ** 9 + 7
		if all(x > 0 for x in arr):
			return sum(arr) * k % mod
		elif all(x < 0 for x in arr):
			return 0
		while k > 1:
			arr += arr
			k -= 1
		n = len(arr)
		@cache
		def dfs(i):
			if i < 0:
				return 0
			return max(arr[i], dfs(i - 1) + arr[i]) % mod
		return max(dfs(i) for i in range(n)) % mod
	
if __name__ == '__main__':
	arr = [1, -2, 1]
	k = 5
	print(Solution().kConcatenationMaxSum(arr, k))