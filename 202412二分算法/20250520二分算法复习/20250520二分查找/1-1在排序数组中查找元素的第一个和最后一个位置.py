###### 二分查找 ##########
# 1.在排序数组中查找元素的第一个和最后一个位置
class Solution1:
	def searchRange(self, nums, target):
		# 闭区间写法
		def lower_bound(nums, target):
			left, right = 0, len(nums) - 1
			while left <= right:
				mid = (left + right) // 2
				if nums[mid] < target:
					left = mid + 1
				else:
					right = mid - 1
			return left
		# 左闭右开区间写法
		def lower_bound2(nums, target):
			left, right = 0, len(nums)
			while left < right:
				mid = (left + right) // 2
				if nums[mid] < target:
					left = mid + 1
				else:
					right = mid
			return left
		# 开区间写法
		def lower_bound3(nums, target):
			left, right = -1, len(nums)
			while left + 1 < right:
				mid = (left + right) // 2
				if nums[mid] < target:
					left = mid
				else:
					right = mid
			return right

		start = lower_bound(nums, target)
		if start == len(nums) or nums[start] != target:
			return [-1, -1]
		end = lower_bound(nums, target + 1) - 1
		return [start, end]
 
 
if __name__ == '__main__':
	nums = []
	target = 8
	print(Solution1().searchRange(nums, target))