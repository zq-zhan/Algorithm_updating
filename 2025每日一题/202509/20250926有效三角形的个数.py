class Solution:
	def triangleNumber(self, nums):
		nums.sort()
		n = len(nums)
		ans = 0
		for k in range(n - 1, 1, -1):
			for j in range(k - 1, 0, -1):
				i = 0
				while i < j and nums[i] + nums[j] <= nums[k]:
					i += 1
				ans += j - i
		return ans

class Solution:
	def triangleNumber(self, nums):
		nums.sort()
		n = len(nums)
		ans = 0
		for k in range(2, n):
			left, right = 0, k - 1
			while left < right:
				if nums[left] + nums[right] > nums[k]:
					ans += right - left
					right -= 1
				else:
					left += 1
		return ans
	
if __name__ == '__main__':
	nums = [2, 2, 3, 4]
	print(Solution().triangleNumber(nums))