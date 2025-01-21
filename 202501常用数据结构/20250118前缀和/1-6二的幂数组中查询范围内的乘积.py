# 6.二的幂数组中查询范围内的乘积
from math import log2

class Solution1:
	def productQueries(self, n, queries):
		target = int(log2(n + 1))
		ori_arr = [2 ** x for x in range(target + 1)]
		temp_sum = 0
		# new_arr = []
		min_arr = [0] * len(ori_arr)
		left = 0
		for right, c in enumerate(ori_arr):
			temp_sum += c
			while temp_sum >= n:
				if temp_sum == n and right - left + 1 < len(min_arr):
					min_arr = ori_arr[left: right + 1]
				temp_sum -= ori_arr[left]
				left += 1

		sub_plus = [1]
		for p1 in range(len(min_arr)):
			sub_plus.append(sub_plus[-1] * min_arr[p1])

		ans = []
		for left, right in queries:
			ans.append(sub_plus[right + 1] // sub_plus[left])
		return ans

## 
class Solution2:
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

MOD = 10 ** 9 + 7

class Solution:
    def productQueries(self, n: int, queries):
        a = []
        while n:
            lb = n & -n
            a.append(lb)
            n ^= lb
        na = len(a)
        res = [[0] * na for _ in range(na)]
        for i, x in enumerate(a):
            res[i][i] = x
            for j in range(i + 1, na):
                res[i][j] = res[i][j - 1] * a[j] % MOD
        return [res[l][r] for l, r in queries]



if __name__ == '__main__':
	n = 919
	queries = [[0,6]]
	cls = Solution()
	print(cls.productQueries(n, queries))