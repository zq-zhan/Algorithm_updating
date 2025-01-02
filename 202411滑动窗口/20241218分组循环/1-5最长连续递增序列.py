# 5.最长连续递增序列
class Solution1:
	def findLengthOfLCIS(self,nums):
		ans = 0
		left, right = 0, 1
		while right < len(nums):
			if nums[right] <= nums[right - 1]:
				ans = max(ans, right - left)
				left = right
			right += 1
		return max(ans,right - left)
	
if __name__ == '__main__':
	nums = [1,3,5,4,7]
	cls = Solution1()
	print(cls.findLengthOfLCIS(nums))