from math import isqrt, log2

ori_2 = [2 ** i for i in range(31)]
MOD = 10 ** 9 + 7
class Solution:
	def productQueries(self, n, queries):
		power = []
		for x in ori_2[::-1]:
			if sum(power) + x <= n:
				power.append(x)

		power.sort()
		plus_pre = [1]
		for x in power:
			plus_pre.append(plus_pre[-1] * x)
		ans = []
		for left, right in queries:
			ans.append(plus_pre[right + 1]//plus_pre[left]%MOD)
		return ans
	
## 
class Solution:
	def productQueries(self, n, queries):
		target = int(log2(n + 1))
		ori_arr = [2 ** x for x in range(target + 1)]
		temp_diff = n
		min_arr = []
		while temp_diff > 0:
			min_arr.append(max([x for x in ori_arr if x <= temp_diff]))
			temp_diff -= min_arr[-1]

		p1, p2 = 0, len(min_arr) - 1
		while p1 < p2:
			temp = min_arr[p1]
			min_arr[p1] = min_arr[p2]
			min_arr[p2] = temp
			p1 += 1
			p2 -= 1
		# temp_sum = 0
		# # new_arr = []
		# min_arr = [0] * len(ori_arr)
		# left = 0
		# for right, c in enumerate(ori_arr):
		# 	temp_sum += c
		# 	while sum(new_arr) >= n:
		# 		if temp_sum == n and right - left + 1 < len(min_arr):
		# 			min_arr = ori_arr[left: right + 1]
		# 		temp_sum -= ori_arr[left]
		# 		left += 1
        
		sub_plus = [1]
		for p1 in range(len(min_arr)):
			sub_plus.append(sub_plus[-1] * min_arr[p1])

		ans = []
		for left, right in queries:
			ans.append((sub_plus[right + 1] // sub_plus[left]) % (10**9 + 7))
		return ans


if __name__ == '__main__':
	n = 15
	queries = [[0, 1], [2, 2], [0, 3]]
	print(Solution().productQueries(n, queries))