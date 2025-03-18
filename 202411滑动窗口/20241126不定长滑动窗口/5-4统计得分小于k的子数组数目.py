# 14.统计得分小于k的子数组数目
class Solution1:
	def countSubarrays(self, nums, k):
		ans = left = 0
		temp_score = 0
		for right, c in enumerate(nums):
			temp_score += c
			while temp_score * (right - left + 1) >= k:
				temp_score -= nums[left]
				left += 1
			ans += right - left + 1
		return ans
	
if __name__ == '__main__':
	nums = [2,1,4,3,5]
	k = 10
	print(Solution1().countSubarrays(nums, k))