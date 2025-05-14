# 5.有序数组的平方
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
	

"""
这题犯了个错误，不能原地修改！
"""

if __name__ == '__main__':
	nums = [-10000,-9999,-7,-5,0,0,10000]
	print(Solution1().sortedSquares(nums))