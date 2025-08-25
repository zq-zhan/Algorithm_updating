from functools import cache
from bisect import bisect_right
# class Solution:
# 	def kIncreasing(self, arr, k):
# 		n = len(arr)
# 		ans = 0
# 		# @cache
# 		def dfs(i, nums):
# 			res = 0
# 			for j in range(i):
# 				if nums[j] <= nums[i]:
# 					res = max(res, dfs(j))
# 			return res + 1
				
# 		for i in range(k):
# 			new_arr = [arr[j] for j in range(i, n, k)]
# 			m = len(new_arr)
# 			temp_mx = max(dfs(i, new_arr) for i in range(m))
# 			ans += m - temp_mx
# 		return ans

def find_mx(nums):
	g = []
	ans = 1
	for x in nums:
		j = bisect_right(g, x)
		if j == len(g):
			g.append(x)
		else:
			g[j] = x
		ans = max(ans, j + 1)
	return ans 

class Solution:
	def kIncreasing(self, arr, k):
		n = len(arr)
		ans = 0
		# @cache
		# def dfs(i, nums):
		# 	res = 0
		# 	for j in range(i):
		# 		if nums[j] <= nums[i]:
		# 			res = max(res, dfs(j))
		# 	return res + 1
				
		for i in range(k):
			new_arr = [arr[j] for j in range(i, n, k)]
			m = len(new_arr)
			# temp_mx = max(dfs(i, new_arr) for i in range(m))
			temp_mx = find_mx(new_arr)
			ans += m - temp_mx
		return ans

	
if __name__ == '__main__':
	arr = [5,4,3,2,1]
	k = 1
	print(Solution().kIncreasing(arr, k))