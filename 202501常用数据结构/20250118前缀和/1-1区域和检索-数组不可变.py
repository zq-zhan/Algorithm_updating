# 1.区域和检索-数组不可变
class NumArray:
	def __init__(self, nums):
		self.nums = nums
		pre_nums = [0]
		for i in range(0, len(nums)):
			pre_nums.append(nums[i] + pre_nums[-1])
		self.pre_nums = pre_nums

	def sumRange(self, left, right):
		return self.pre_nums[right + 1] - self.pre_nums[left]
	
if __name__ == '__main__':
	cls = NumArray([-2, 0, 3, -5, 2, -1])
	print(cls.sumRange(0, 2)) # 9
	print(cls.sumRange(2, 5)) # 15  