from collections import defaultdict

class Solution1:
	def threeSum(self, nums):
		ans = set()
		n = len(nums)
		nums.sort()
		for i, c in enumerate(nums[:-2]):
			left, right = i + 1, n - 1
			while left < right:
				temp_s = c + nums[left] + nums[right]
				if temp_s == 0:
					temp_ans = (c, nums[left], nums[right])
					ans.add(temp_ans)
					left += 1
				elif temp_s < 0:
					left += 1
				else:
					right -= 1
		return [list(val) for val in ans]
	
## 优化：提前判断 去重
class Solution2:
	def threeSum(self, nums):
		ans = []
		n = len(nums)
		nums.sort()
		for i, c in enumerate(nums[:-2]):
			if i > 0 and nums[i - 1] == c:
				continue
			left, right = i + 1, n - 1
			while left < right:
				temp_s = c + nums[left] + nums[right]
				if temp_s == 0:
					ans.append([c, nums[left], nums[right]])
					right -= 1
					while left < right and nums[left] == nums[left - 1]:
						left += 1
					while left < right and nums[right] == nums[right + 1]:
						right -= 1
					# right -= 1
				elif temp_s < 0:
					left += 1
				else:
					right -= 1
		return ans
	
if __name__ == '__main__':
	nums = [-1,0,1,2,-1,-4]
	s = Solution2()
	print(s.threeSum(nums))