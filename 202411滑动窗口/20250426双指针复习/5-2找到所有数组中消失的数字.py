class Solution1:
	def findDisappearedNumbers(self, nums):
		# ans = []
		for x in nums:
			x = abs(x)
			nums[x - 1] = -abs(nums[x - 1])
		return [i + 1 for i, x in enumerate(nums) if x > 0]

	
if __name__ == '__main__':
	nums = [4,3,2,7,8,2,3,1]
	print(Solution1().findDisappearedNumbers(nums))