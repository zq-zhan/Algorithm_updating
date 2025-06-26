from itertools import accumulate

class Solution:
	def maxSumRangeQuery(self, nums, requests):
		mod = 10 ** 9 + 7
		n = len(nums)
		new_arr = [0] * (n + 1)
		for start, end in requests:
			new_arr[start] += 1
			new_arr[end + 1] -= 1
		pre_s = list(accumulate(new_arr))[:-1]
		pre_s.sort(reverse = True)
		nums.sort(reverse = True)
		return sum(x * y for x, y in zip(nums, pre_s)) % mod
	
if __name__ == '__main__':
	nums = [1, 2, 3, 4, 5]
	requests = [[1, 3], [0, 1]]
	print(Solution().maxSumRangeQuery(nums, requests))