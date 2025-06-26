class Solution1:
	def countSubarrays(self, nums, k):
		temp_s = ans = left = 0
		for right, c in enumerate(nums):
			temp_s += c
			while temp_s * (right - left + 1) >= k:
				temp_s -= nums[left]
				left += 1
			ans += right - left + 1
		return ans
	
if __name__ == '__main__':
	nums = [2,1,4,3,5]
	k = 10
	print(Solution1().countSubarrays(nums, k))