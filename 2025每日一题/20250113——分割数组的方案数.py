# 20250113——分割数组的方案数
class Solution1:
	def waysToSplitArray(self, nums):
		# cum_sum_1 = []
		ans = 0
		temp_sum = 0
		nums_sum = sum(nums)
		for i in range(len(nums) - 1):
			temp_sum += nums[i]
			if temp_sum >= nums_sum - temp_sum:
				ans += 1
		return ans
	
if __name__ == '__main__':
	nums = [10, 4, -8, 7]
	cls = Solution1()
	print(cls.waysToSplitArray(nums))