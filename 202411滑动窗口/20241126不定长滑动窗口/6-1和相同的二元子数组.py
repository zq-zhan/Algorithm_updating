# 1.和相同的二元子数组
class Solution1:
	def numSubarraysWithSum(self, nums, goal):

		def mx_target(x):
			ans = left = 0
			temp_sum = 0
			for right, c in enumerate(nums):
				temp_sum += c
				while left <= right and temp_sum >= x:
					temp_sum -= nums[left]
					left += 1
				ans += left
			return ans
		return mx_target(goal) - mx_target(goal + 1)


class Solution2:
	def numSubarraysWithSum(self, nums, goal):
		def upper_target(nums, target):
			ans = left = 0
			temp_sum = 0
			for right, c in enumerate(nums):
				temp_sum += c
				while left <= right and temp_sum >= target:
					temp_sum -= nums[left]
					left += 1
				ans += left
			return ans
		return upper_target(nums, goal) - upper_target(nums, goal + 1)

## 优化：三指针——同时维护两个left
class Solution3:
	def numSubarraysWithSum(self, nums, goal):
		left1 = left2 = ans = 0
		temp_sum1 = temp_sum2 = 0
		for right, c in enumerate(nums):
			temp_sum1 += c
			temp_sum2 += c
			while left1 <= right and temp_sum1 >= goal:
				temp_sum1 -= nums[left1]
				left1 += 1
			while left2 <= right and temp_sum2 >= goal + 1:
				temp_sum2 -= nums[left2]
				left2 += 1
			ans += left1 - left2
		return ans
	
if __name__ == '__main__':
	nums = [1,0,1,0,1]
	goal = 2
	print(Solution3().numSubarraysWithSum(nums, goal))