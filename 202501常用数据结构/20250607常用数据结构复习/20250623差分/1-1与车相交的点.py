from itertools import accumulate

class Solution:
	def numberOfPoints(self, nums):
		mx = max((max(a, b) for a, b in nums))
		new_arr = [0] * (mx + 1)
		for start, end in nums:
			new_arr[start - 1] += 1
			new_arr[end] -= 1
		pre_s = list(accumulate(new_arr))
		return sum(1 if x > 0 else 0 for x in pre_s)
	
if __name__ == '__main__':
	nums = [[3,6],[1,5],[4,7]]
	print(Solution().numberOfPoints(nums))