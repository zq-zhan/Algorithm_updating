# 2.搜索插入位置
class Solution1:
	def searchInsert(self,nums,target):
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
		ans = lower_bound(nums,target)
		return ans
		
if __name__ == '__main__':
	nums = [1,3,5,6]
	target = 2
	print(Solution1().searchInsert(nums,target))