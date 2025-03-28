from heapq import nsmallest

class Solution1:
	def minimumCost(self, nums):
		new_arr = sorted(nums[1:])
		return nums[0] + sum(new_arr[:2])
	
## 灵神题解
class Solution2:
	def minimumCost(self, nums):
		return nums[0] + sum(nsmallest(2, nums[1:]))
	
if __name__ == '__main__':
	nums = [1, 2, 3, 12]
	print(Solution1().minimumCost(nums))