# 14.三角形的最大周长
class Solution1:
	def largestPerimeter(self, nums):
		nums.sort(reverse = True)
		n = len(nums)
		for i in range(n - 2):
			if nums[i] >= nums[i + 1] + nums[i + 2]:
				continue
			else:
				return nums[i] + nums[i + 1] + nums[i + 2]
		return 0
	
if __name__ == '__main__':
	nums = [1,2,1,10]
	s = Solution1()
	print(s.largestPerimeter(nums))