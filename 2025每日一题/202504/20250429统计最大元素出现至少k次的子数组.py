class Solution1:
	def countSubarrays(self, nums, k):
		max_num = max(nums)
		ans = left = cnt = 0
		for right, c in enumerate(nums):
			cnt += 1 if c == max_num else 0
			while cnt >= k:
				ans += left
				cnt -= 1 if nums[left] == max_num else 0
				left += 1
		return ans
	
if __name__ == '__main__':
	nums = [1,3,2,3,3]
	k = 2
	print(Solution1().countSubarrays(nums, k)) # Output: 2
	