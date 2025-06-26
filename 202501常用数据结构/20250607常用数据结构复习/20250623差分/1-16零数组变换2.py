from itertools import accumulate

class Solution:
	def minZeroArray(self, nums, queries):
		cnt = 0
		n = len(nums)
		for left, right, val in queries:
			if all(x <= 0 for x in nums):
				return cnt
			for i in range(n):
				if left<= i <= right and nums[i] > 0:
					nums[i] -= val
			cnt += 1
		return -1
	
## 差分 + 二分
class Solution:
	def minZeroArray(self, nums, queries):
		def check(target):
			new_arr = [0] * (n + 1)
			for left, right, val in queries[:target]:
				new_arr[left] -= val
				new_arr[right + 1] += val
			pre_s = list(accumulate(new_arr))[:-1]
			return all(x + y <= 0 for x, y in zip(pre_s, nums)) 

		q = len(queries)
		n = len(nums)
		left, right = -1, q + 1
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				right = mid
			else:
				left = mid
		return right if right < q + 1 else -1
	
## 双指针 + 差分
class Solution:
	def minZeroArray(self, nums, queries):
		diff = [0] * (len(nums) + 1)
		sum_d = k = 0
		for i, (x, d) in enumerate(zip(nums, diff)):
			sum_d += d
			while k < len(queries) and sum_d < x:
				left, right, val = queries[k]
				diff[left] += val
				diff[right + 1] -= val
				if left <= i <= right:
					sum_d += val
				k += 1
			if sum_d < x:
				return -1
		return k

if __name__ == '__main__':
	nums = [7,6,8]
	queries = [[0,0,2],[0,1,5],[2,2,5],[0,2,4]]
	print(Solution().minZeroArray(nums, queries))