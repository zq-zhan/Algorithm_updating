# 1.在排序数组中查找元素的第一个和最后一个位置
class Solution1:
	def searchRange(self,nums,target):
		def lower_bound(nums,target):
			left = 0
			right = len(nums) - 1
			while left <= right:
				mid = (left + right) // 2
				if nums[mid] < target:
					left = mid + 1
				else:
					right = mid - 1
			return left
		start = lower_bound(nums,target)
		if start == len(nums) or nums[start] != target:
			return [-1,-1]
		end = lower_bound(nums,target + 1) - 1
		return [start,end]
	
if __name__ == '__main__':
	nums = [5,7,7,7,9,10]
	target = 8
	s = Solution1()
	print(s.searchRange(nums,target))