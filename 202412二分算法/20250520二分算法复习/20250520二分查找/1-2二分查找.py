class Solution1:
	def search(self, nums, target):
		def lower_bound(target):
			left, right = -1, len(nums)
			while left + 1 < right:
				mid = (left + right) // 2
				if nums[mid] < target:
					left = mid
				else:
					right = mid
			return right
		ans = lower_bound(target)
		if ans < len(nums) and nums[ans] == target:
			return ans
		else:
			return -1
		
if __name__ == '__main__':
	nums = [-1,0,3,5,9,12]
	target = 9
	print(Solution1().search(nums, target))