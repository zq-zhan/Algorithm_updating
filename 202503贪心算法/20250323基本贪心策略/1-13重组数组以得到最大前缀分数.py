# 13.重组数组以得到最大前缀分数
class Solution1:
	def maxScore(self, nums):
		nums.sort(reverse = True)
		temp_s = 0
		for i, x in enumerate(nums, 1):
			temp_s += x
			if temp_s <= 0:
				return i - 1
		return i
	
if __name__ == '__main__':
	nums = [2,-1,0,1,-3,3,-3]
	print(Solution1().maxScore(nums))