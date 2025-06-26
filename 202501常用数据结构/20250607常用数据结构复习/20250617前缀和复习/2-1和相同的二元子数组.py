from collections import defaultdict

class Solution:
	def numSubarraysWithSum(self, nums, goal):
		dic_win = defaultdict(int)
		ans = temp_s = 0
		for x in nums:
			dic_win[temp_s] += 1
			temp_s += x
			ans += dic_win[temp_s - goal]
		return ans
	
if __name__ == '__main__':
	nums = [1,0,1,0,1]
	goal = 2
	print(Solution().numSubarraysWithSum(nums, goal))