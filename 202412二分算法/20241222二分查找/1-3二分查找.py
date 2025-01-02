# 3.二分查找
class Solution1:
	def search(self,nums,target):
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
		if ans == len(nums) or nums[ans] != target:
			return -1
		else:
			return ans
		
if __name__ == '__main__':
	nums = [-1,0,3,5,9,12]
	target = 9
	cls = Solution1()
	print(cls.search(nums,target))