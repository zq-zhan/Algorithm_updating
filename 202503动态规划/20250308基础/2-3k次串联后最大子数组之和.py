from functools import cache

# 13.k次串联后最大子数组之和
class Solution1:  # ——超出内存限制
	def kConcatenationMaxSum(self, arr, k):
		# new_arr = []
		# for _ in range(k):
		# 	new_arr.extend(arr)
		n = len(arr)
		mod = (10 ** 9) + 7
		@cache
		def dfs(i):
			if i < 0:
				return 0
			return max(dfs(i - 1), 0) + arr[i % n]
		return max(dfs(x) for x in range(-1, n * k)) % mod

## 前缀和写法——超出内存限制
class Solution2:
	def kConcatenationMaxSum(self, arr, k):
		mod = 10 ** 9 + 7
		n = len(arr)
		min_pre_sum = 0
		ans = 0
		temp_s = 0
		for i in range(n * k):
			temp_s += arr[i % n]
			ans = max(temp_s - min_pre_sum, ans)
			min_pre_sum = min(min_pre_sum, temp_s)
		return ans % mod
## 前缀和写法优化
class Solution3:
	def kConcatenationMaxSum(self, arr, k):
		mod = 10 ** 9 + 7
		s, max_s = 0, 0
		for x in arr * min(2, k):
			s = x if s < 0 else s + x  # 前缀和
			max_s = max(max_s, s)
		if k <= 2:
			return max_s % mod
		return (max(sum(arr), 0) * (k - 2) + max_s) % mod
## 前缀和写法优化2
class Solution3:
	def kConcatenationMaxSum(self, arr, k):
		mod = 10 ** 9 + 7
		min_pre_sum = 0
		ans = 0
		temp_s = 0
		for x in arr * min(k, 2):
			temp_s += x
			ans = max(ans, temp_s - min_pre_sum)
			min_pre_sum = min(min_pre_sum, temp_s)
		if k <= 2:
			return ans % mod
		return (max(sum(arr), 0) * (k - 2) + ans) % mod


## 递归写法
class Solution4:
	def kConcatenationMaxSum(self, arr, k):
		mod = 10 ** 9 + 7
		s = sum(arr)

		def maxSub(arr):
			n = len(arr)
			@cache
			def dfs(i):
				if i < 0:
					return 0
				return max(dfs(i - 1), 0) + arr[i]
			return max(dfs(x) for x in range(n))

		if k == 1:
			return max(0, maxSub(arr)) % mod
		else:
			return max(maxSub(arr + arr) + max(0, (k - 2) * s), 0) % mod

## 递推
class Solution4:
	def kConcatenationMaxSum(self, arr, k):
		mod = 10 ** 9 + 7
		s = sum(arr)

		def max_ditui(arr):
			f0 = 0
			ans = 0
			for x in arr:
				f0 = max(f0, 0) + x
				ans = max(f0, ans)
			return ans

		if k <= 2:
			return max(0, max_ditui(arr * k)) % mod
		else:
			return max(max_ditui(arr * 2) + max(0, (k - 2) * s), 0) % mod
	
if __name__ == '__main__':
	arr = [1,-2,1]
	k = 5
	s = Solution2()
	print(s.kConcatenationMaxSum(arr, k))