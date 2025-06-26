from math import inf

class Solution:
	def findIndices(self, nums, indexDifference, valueDifference):
		i = 0
		mn = 0
		mx = 0
		for j, y in enumerate(nums):
			if j - i < indexDifference:
				continue
			if nums[i] < nums[mn]:
				mn = i
			if nums[i] > nums[mx]:
				mx = i
			if abs(nums[mn] - y) >= valueDifference:
				return [mn, j]
			if abs(nums[mx] - y) >= valueDifference:
				return [mx, j]
			i += 1
		return [-1, -1]
	
if __name__ == '__main__':
	nums = [4,4,3,0,6,1,7,8]
	indexDifference = 3
	valueDifference = 6
	print(Solution().findIndices(nums, indexDifference, valueDifference))