# 20250120找到最接近0的数字
from math import inf

class Solution1:
	def findClosestNumber(self, nums):
		ans = inf
		temp_dis = inf
		for x in nums:
			if temp_dis > abs(x) or (temp_dis == abs(x) and x > ans):
				temp_dis = abs(x)
				ans = x
		return ans
	
if __name__ == '__main__':
	nums = [1,2,3,4,5]
	print(Solution1().findClosestNumber(nums))