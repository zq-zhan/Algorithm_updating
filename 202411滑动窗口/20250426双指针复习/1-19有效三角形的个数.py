class Solution1:
	def triangleNumber(self, nums):
		nums.sort()
		ans = 0
		n = len(nums)
		for k in range(2, n):
			left, right = 0, k - 1
			while left < right:
				if nums[left] + nums[right] > nums[k]:
					ans += right - left  # 以right为第二条边的合法三角形个数
					right -= 1
				else:
					left += 1  # 保证单调性
		return ans
	
if __name__ == '__main__':
	nums = [4,2,3,4]
	print(Solution1().triangleNumber(nums))