from math import gcd

class Solution:
	def minOperations(self, nums):
		tag = True
		cnt = 0
		n = len(nums)
		cnt_1 = nums.count(1)
		while tag:
			m = len(nums)
			for i in range(m - 1):
				temp = gcd(nums[i], nums[i + 1])
				nums[i] = temp
				if temp == 1:
					tag = False
					break
			if nums:
				nums.pop()
			else:
				return -1
			cnt += 1
		return n - cnt_1 + cnt - 1

	
if __name__ == '__main__':
	nums = [2,10,6,14]
	print(Solution().minOperations(nums))