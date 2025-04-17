# 20250115——超过阈值的最少操作数2
from math import inf


class Solution1:
	def minOperations(self, nums, k):
		nums.sort()
		new_arr = nums.copy()
		ans = 0
		while min(new_arr.values()) < k:
			new_arr.append(new_arr[0] * 2 + new_arr[1])
			new_arr = new_arr[2:]
			new_arr.sort()
			ans += 1
		return ans
class Solution2:
	def minOperations(self, nums, k):
		nums.sort()
		ans = 0
		n = len(nums)
		left = 2
		while min(nums) < k:
			temp = nums[ans] * 2 + nums[ans + 1]
			nums[ans] = inf
			while left < n and nums[left] <= temp:
				nums[left - 1] = nums[left]
				left += 1
			nums[left - 1] = temp
			ans += 1
		return ans
	
if __name__ == '__main__':
	nums = [1,1,2,4,9]
	k = 10
	print(Solution2().minOperations(nums, k))