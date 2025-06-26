class Solution1:
	def maximumCount(self, nums):
		def lower_bound(target):
			left, right = -1, len(nums)
			while left + 1 < right:
				mid = (left + right) // 2
				if nums[mid] < target:
					left = mid
				else:
					right = mid
			return right

		pos_num = len(nums) - lower_bound(1)
		neg_num = lower_bound(0) - 1 + 1
		return max(pos_num, neg_num)
	
if __name__ == '__main__':
	nums = [-2,-1,-1,1,2,3]
	print(Solution1().maximumCount(nums))