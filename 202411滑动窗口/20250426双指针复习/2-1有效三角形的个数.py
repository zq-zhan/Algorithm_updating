class Solution1:
	def triangleNumber(self, nums):
		nums.sort()  # 排序后枚举最大的边
		n = len(nums)
		ans = 0
		for right in range(n - 1, 1, -1):
			c = nums[right]
			for left in range(right - 1, 0, -1):
				b = nums[left]
				for k in range(left):
					if nums[k] + b > c:
						ans += left - k
						break
		return ans

if __name__ == '__main__':
	nums = [4,2,3,4]
	print(Solution1().triangleNumber(nums))