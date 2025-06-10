class Solution1:
	def smallestDivisor(self, nums, threshold):
		def check(target):
			if sum((x - 1) // target for x in nums) <= threshold - len(nums):
				return True
			else:
				return False

		left, right = min(nums) - 1, max(nums) + 1
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				right = mid
			else:
				left = mid
		return right

if __name__ == '__main__':
	nums = [44,22,33,11,1]
	threshold = 5
	print(Solution1().smallestDivisor(nums, threshold))