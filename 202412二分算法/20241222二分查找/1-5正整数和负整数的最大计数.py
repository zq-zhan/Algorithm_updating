# 5.正整数和负整数的最大计数
class Solution1:
	def maximumCount(self,nums):
		def lower_bound(nums,target):
			left, right = 0, len(nums) - 1
			while left <= right:
				mid = (left + right) // 2
				if nums[mid] < target:
					left = mid + 1
				else:
					right = mid - 1
			return left
		end = lower_bound(nums,1) # >= 1
		start = lower_bound(nums,0) - 1 # <= -1
		return max(start + 1, len(nums) - end)
	
if __name__ == '__main__':
	nums = [0,0,0,0,0,0,0,0]
	cls = Solution1()
	print(cls.maximumCount(nums))