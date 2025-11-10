class Solution:
	def countValidSelections(self, nums):
		cnt_left = 0
		s = sum(nums)
		ans = 0
		for x in nums:
			cnt_left += x
			if x == 0:
				if cnt_left == s - cnt_left:
					ans += 2
				elif abs(s - 2 * cnt_left) == 1:
					ans += 1
		return ans

	
if __name__ == '__main__':
	nums = [16,13,10,0,0,0,10,6,7,8,7]
	print(Solution().countValidSelections(nums))