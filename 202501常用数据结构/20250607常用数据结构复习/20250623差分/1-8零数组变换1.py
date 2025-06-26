from itertools import accumulate

class Solution:
	def isZeroArray(self, nums, queries):
		new_arr = [0] * (len(nums) + 1)
		for left, right in queries:
			new_arr[left] -= 1
			new_arr[right + 1] += 1
		pre_s = list(accumulate(new_arr))[:-1]
		return all(x + y <= 0 for x, y in zip(nums, pre_s))
	
if __name__ == '__main__':
	nums = [1,0,1]
	queries = [[0,2]]
	s = Solution()
	print(s.isZeroArray(nums, queries))