class Solution:
	def zeroFilledSubarray(self, nums):
		ans = left = 0
		for right, x in enumerate(nums):
			if x == 0:
				continue
			ans += (right - left) * (right - left + 1) // 2
			left = right + 1
		return ans
	
if __name__ == '__main__':
	nums = [1,3,0,0,2,0,0,4]
	print(Solution().zeroFilledSubarray(nums))