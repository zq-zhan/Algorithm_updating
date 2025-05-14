class Solution1:
	def fourSum(self, nums, target):
		nums.sort()
		n = len(nums)
		ans = []
		for i in range(n - 3):
			if i > 0 and nums[i] == nums[i - 1]:
				continue
			for j in range(i + 1, n - 2):
				if j > i + 1 and nums[j] == nums[j - 1]:
					continue
				left, right = j + 1, n - 1
				while left < right:
					temp_s = nums[i] + nums[j] + nums[left] + nums[right]
					if temp_s < target:
						left += 1
					elif temp_s > target:
						right -= 1
					else:
						ans.append([nums[i], nums[j], nums[left], nums[right]])
						right -= 1
						while left < right and nums[left] == nums[left - 1]:
							left += 1
						while left < right and nums[right] == nums[right + 1]:
							right -= 1
		return ans
	
if __name__ == '__main__':
	nums = [1, 0, -1, 0, -2, 2]
	target = 0
	s = Solution1()
	print(s.fourSum(nums, target))