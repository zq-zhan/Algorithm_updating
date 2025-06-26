class Solution1:
	def numberOfSubarrays(self, nums, k):
		temp_cnt1 = temp_cnt2 = ans = left1 = left2 = 0
		for c in nums:
			if c % 2 == 1:
				temp_cnt1 += 1
				temp_cnt2 += 1
			while temp_cnt1 >= k:
				temp_cnt1 -= nums[left1] % 2
				left1 += 1
			while temp_cnt2 >= k + 1:
				temp_cnt2 -= nums[left2] % 2
				left2 += 1
			ans += left1 - left2
		return ans

if __name__ == '__main__':
	nums = [1,1,2,1,1]
	k = 3
	print(Solution1().numberOfSubarrays(nums, k))