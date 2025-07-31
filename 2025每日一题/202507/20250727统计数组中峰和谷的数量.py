class Solution:
	def countHillValley(self, nums):
		ans = 0
		pre_num = nums[0]
		for i, x in enumerate(nums):
			if i == 0 or i == len(nums)-1 or nums[i] == nums[i + 1]:
				continue
			if (pre_num > x and nums[i + 1] > x) or \
				(pre_num < x and nums[i + 1] < x):
				ans += 1
			pre_num = nums[i]
		return ans
	
if __name__ == '__main__':
	nums = [2,4,1,1,6,5]
	print(Solution().countHillValley(nums))