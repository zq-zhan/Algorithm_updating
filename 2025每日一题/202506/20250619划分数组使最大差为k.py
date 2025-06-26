class Solution:
	def partitionArray(self, nums, k):
		nums.sort()
		ans = 0
		pre_mn = nums[0]
		for i in range(1, len(nums)):
			if nums[i] - pre_mn <= k:
				continue
			else:
				pre_mn = nums[i]
				ans += 1
		return ans + 1
	
if __name__ == '__main__':
	nums = [3,6,1,2,5]
	k = 2
	print(Solution().partitionArray(nums, k))