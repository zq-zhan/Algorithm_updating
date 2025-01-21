# 前缀和与哈希表
# 1.和相同的二元子数组
class Solution2:
	def numSubarraysWithSum(self, nums, goal):
		def max_win(target):
			temp_ans = temp_sum = 0
			left = 0
			for right, c in enumerate(nums):
				temp_sum += c
				while left <= right and temp_sum >= target:
					# temp_ans += left
					temp_sum -= nums[left]
					left += 1
				temp_ans += left
			return temp_ans
		
		return max_win(goal) - max_win(goal + 1)


if __name__ == '__main__':
	nums = [1, 0, 1, 0, 1]
	goal = 2
	print(Solution2().numSubarraysWithSum(nums, goal))