# 7.字符串中最大的3位相同数字
class Solution1:
	def largestGoodInteger(self, nums):
		ans = ''
		temp_mx = 0
		for i in range(2, len(nums)):
			if nums[i] == nums[i - 1] == nums[i - 2]:
				if int(nums[i]) >= temp_mx:
					temp_mx = int(nums[i])
					ans = str(nums[i]) * 3
		return ans
	
if __name__ == '__main__':
	num = '6777133339'
	cls = Solution1()
	print(cls.largestGoodInteger(num))