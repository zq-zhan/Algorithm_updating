class Solution:
	def sortedSquares(self, nums):
		n = len(nums)
		left, right = 0, n - 1
		while left <= right:
			if nums[left] ** 2 < nums[right] ** 2:
				nums[right] = nums[right] ** 2
				right -= 1
			else:
				temp = nums[left]
				nums[left] = nums[right]
				nums[right] = temp ** 2
				right -= 1
		return nums

class Solution1:
	def sortedSquares(self, nums):
		n = len(nums)
		left, right = 0, n - 1
		ans = [0] * n
		for p in range(n - 1, -1, -1):
			x = nums[left] ** 2
			y = nums[right] ** 2
			if x <= y:
				ans[p] = y
				right -= 1
			else:
				ans[p] = x
				left += 1
		return ans

if __name__ == '__main__':
	nums = [-5,-3,-2,-1]
	print(Solution1().sortedSquares(nums))