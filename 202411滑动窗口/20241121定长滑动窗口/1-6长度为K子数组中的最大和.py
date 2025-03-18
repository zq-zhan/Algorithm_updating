# 3.长度为K子数组中的最大和
from collections import defaultdict

class Solution1:
	def maximumSubarraySum(self, nums, k):
		ans = 0
		temp_ans = 0
		set_win = set()
		for left, x in enumerate(nums):
			temp_ans += x
			set_win.add(x)
			if len(set_win) == k:
				ans = max(ans, temp_ans)
				temp_ans -= nums[left - k + 1]
				set_win.remove(nums[left - k + 1])
		return ans
	
class Solution2:
	def maximumSubarraySum(self, nums, k):
		ans = 0
		temp_ans = 0
		dic_win = defaultdict(int)
		for left, x in enumerate(nums):
			temp_ans += x
			dic_win[x] += 1
			if left >= k - 1:
				if len(dic_win) == k:
					ans = max(ans, temp_ans)
				temp_num = nums[left - k + 1]
				temp_ans -= temp_num
				if dic_win[temp_num] == 1:
					del dic_win[temp_num]
				else:
					dic_win[temp_num] -= 1
		return ans

	
if __name__ == '__main__':
	nums = [1,1,1,7,8,9]
	k = 3
	print(Solution2().maximumSubarraySum(nums, k))