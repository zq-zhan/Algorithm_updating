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

	
if __name__ == '__main__':
	nums = [0,0,0,0,0]
	goal = 0
	print(Solution1().numSubarraysWithSum(nums, goal))