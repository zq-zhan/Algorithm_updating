# 1.分割数组的最大值
class Solution1:
	def splitArray(self, nums, k):
		def check(mx):
			cnt = 1
			s = 0
			for x in nums:
				if s + x <= mx:
					s += x
				else:
					if cnt == k:
						return False
					cnt += 1
					s = x
			return True

		right = sum(nums)
		left = max(max(nums) - 1, (right - 1) // k)
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				right = mid
			else:
				left = mid
		return right

# 2.分配给商店的最多商品的最小值
class Solution1:
	def minimizedMaximum(self, n, quantities):
		def check(mx):
			ans = 0
			for x in quantities:
				ans += (x - 1) // mx + 1
			return ans <= n

		right = sum(quantities)
		left = (right - 1) // n
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				right = mid
			else:
				left = mid
		return right

# 3.袋子里最少数目的球
class Solution1:
	def minimumSize(self, nums, maxOperations):
		def check(mx):
			ans = 0
			for x in nums:
				if x > mx:
					ans += (x - 1) // mx
			return ans <= maxOperations
		right = max(nums)
		left = 0
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				right = mid
			else:
				left = mid
		return right

# 4.最小体力消耗路径
class Solution1:
	def minimumEffortPath(self, heights):
		left = -1
		right = 0
		for height in heights:
			right = max(right, max(height))


# 5.最小化数组中的最大值
class Solution1:
	def minimizeArrayValue(self, nums):
		def check(mx, new_arr):
			for i in range(len(new_arr) - 1, 0, -1):
				if new_arr[i] > mx:
					new_arr[i] = mx
					new_arr[i - 1] += new_arr[i] - mx
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
class Solution:
	def minimizeArrayValue(self, nums):
		def check(limit):
			extra = 0
			for i in range(len(nums) - 1, 0, -1):
				extra = max(nums[i] + extra - limit, 0)
			return nums[0] + extra <= limit
			
		left, right = -1, max(nums)
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid, nums.copy()):
				right = mid
			else:
				left = mid
		return right
