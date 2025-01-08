# 5.最小化数组中的最大值
from bisect import bisect_left


class Solution1:  # 错解
	def minimizeArrayValue(self, nums):
		def check(mx, new_arr):
			for i in range(len(new_arr)):
				if i == 0 and new_arr[i] > mx:
					return False
				while i > 0 and new_arr[i - 1] < mx and new_arr[i] > mx:
					new_arr[i - 1] += 1
					new_arr[i] -= 1
				if new_arr[i] > mx:
					return False
			return True

		left, right = -1, max(nums)
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid, nums.copy()):
				right = mid
			else:
				left = mid
		return right
	

# 灵神思路
class Solution2:
	def minimizeArrayValue(self, nums):
		def check(mx, new_arr):
			for i in range(len(new_arr) - 1, 0, -1):
				if new_arr[i] > mx:
					new_arr[i - 1] += new_arr[i] - mx
					new_arr[i] = mx
			return new_arr[0] <= mx

		left, right = -1, max(nums)
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid, nums.copy()):
				right = mid
			else:
				left = mid
		return right

## 灵神题解
class Solution3:
	def minimizeArrayValue(self, nums):
		def check(limit):
			extra = 0
			for i in range(len(nums) - 1, 0, -1):
				extra = max(nums[i] + extra - limit, 0)
			return nums[0] + extra <= limit
			
		left, right = -1, max(nums)
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				right = mid
			else:
				left = mid
		return right

if __name__ == '__main__':
	nums = [6,9,3,8,14]
	cls = Solution3()
	print(cls.minimizeArrayValue(nums))