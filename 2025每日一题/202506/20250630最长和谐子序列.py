class Solution:
	def findLHS(self, nums):
		nums.sort()
		left = ans = 0 
		for right, x in enumerate(nums):
			while left <= right and x - nums[left] > 1:
				left += 1
			if x - nums[left] == 1:
				ans = max(ans, right - left + 1)
		return ans
	
if __name__ == '__main__':
	nums = [1,3,2,2,5,2,3,7]
	print(Solution().findLHS(nums))