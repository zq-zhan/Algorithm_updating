# 11.统计公平数对的数目
from bisect import bisect_left,bisect_right


class Solution1:
	def countFairPairs(self,nums,lower,upper):
		nums.sort()
		ans = 0
		for i,c in enumerate(nums):
			find_lower = bisect_left(nums,lower - c)
			if find_lower == len(nums):
				continue
			find_upper = bisect_left(nums, upper - c + 1) - 1
			if find_upper == len(nums) - 1:
				if nums[find_upper] > upper - c:
					continue
			if find_lower <= find_upper:
				ans += find_upper - find_lower + 1
		return ans // 2
	
class Solution2:
	def countFairPairs(self,nums,lower,upper):
		nums.sort()
		ans = 0
		for j,c in enumerate(nums):
			find_right = bisect_right(nums,upper - c, 0, j)
			find_left = bisect_left(nums, lower - c, 0, j)
			ans += find_right - find_left
		return ans
	
class Solution3:
	def countFairPairs(self, nums, lower, upper):
		nums.sort()
		ans = 0
		for j in range(len(nums)):
			left_find = bisect_left(nums, lower - nums[j], 0, j)  # 
			right_find = bisect_right(nums, upper - nums[j], 0, j)
			ans += right_find - left_find
		return ans

if __name__ == '__main__':
	nums = [0,1,7,4,4,5]
	lower = 3
	upper = 6
	cls = Solution3()
	print(cls.countFairPairs(nums,lower,upper))