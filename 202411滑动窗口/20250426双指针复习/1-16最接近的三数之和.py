from math import inf

# 16.最接近的三数之和
class Solution1:
	def threeSumClosest(self, nums, target):
		nums.sort()
		ans = inf
		for i, c in enumerate(nums[:-2]):
			left, right = i + 1, len(nums) - 1
			while left < right:
				temp_s = c + nums[left] + nums[right]
				if abs(temp_s - target) < abs(ans - target):
					ans = temp_s
				if temp_s == target:
					return target
				elif temp_s < target:
					left += 1
				else:
					right -= 1
		return ans
	
if __name__ == '__main__':
	nums = [0,3,97,102,200]
	target = 300
	print(Solution1().threeSumClosest(nums, target))