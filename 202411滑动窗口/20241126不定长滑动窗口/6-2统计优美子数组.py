class Solution1:
	def numberOfSubarrays(self, nums, k):
		left1 = left2 = ans = 0
		cnt1 = cnt2 = 0
		for right, c in enumerate(nums):
			if c % 2 == 1:
				cnt1 += 1
				cnt2 += 1
			while left1 <= right and cnt1 >= k:
				cnt1 -= 1 if nums[left1] % 2 == 1 else 0
				left1 += 1
			while left2 <= right and cnt2 >= k + 1:
				cnt2 -= 1 if nums[left2] % 2 == 1 else 0
				left2 += 1
			ans += left1 - left2
		return ans
	
if __name__ == '__main__':
	nums = [1,1,2,1,1]
	k = 3
	print(Solution1().numberOfSubarrays(nums, k))