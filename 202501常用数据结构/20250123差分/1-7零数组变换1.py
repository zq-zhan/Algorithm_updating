# 7.零数组变换1
from itertools import accumulate

class Solution1:
	def isZeroArray(self, nums, queries):
		d = [0] * (len(nums) + 1)
		for left, right in queries:
			d[left] -= 1
			d[right + 1] += 1

		diff_sum = list(accumulate(d))[:-1]
		return all(x + y <= 0 for x, y in zip(nums, diff_sum))
	
if __name__ == '__main__':
	nums = [4,3,2,1]
	queries = [[1,3],[0,2]]
	cls = Solution1()
	print(cls.isZeroArray(nums, queries))