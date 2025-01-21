# 4.半径为k的子数组平均值
class Solution1:
	def getAverages(self, nums, k):
		ans = [-1] * len(nums)
		temp_sum = 0
		for i, c in enumerate(nums):
			temp_sum += c
			if i < 2 * k:
				continue
			ans[i - k] = temp_sum // (2 * k + 1)
			temp_sum -= nums[i - 2 * k]
		return ans
	
if __name__ == '__main__':
	nums = [7,4,3,9,1,8,5,2,6]
	k = 3
	cls = Solution1()
	print(cls.getAverages(nums, k))