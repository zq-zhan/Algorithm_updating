# 20250402有序三元组中的最大值1
class Solution1:  # O（n^3）
	def maximumTripletValue(self, nums):
		ans = 0
		n = len(nums)
		for p1 in range(n):
			for p2 in range(p1 + 1, n):
				if nums[p1] <= nums[p2]:
					continue
				for p3 in range(p2 + 1, n):
					ans = max(ans, (nums[p1] - nums[p2]) * nums[p3])
		return ans

## 枚举j——O(n^2)
class Solution2:
	def maximumTripletValue(self, nums):
		ans = 0
		n = len(nums)
		for j in range(1, n - 1):
			a = max(nums[:j])
			b = nums[j]
			c = max(nums[j + 1:])
			ans = max((a - b) * c, ans)
		return ans

## 灵神思路 —— 枚举k
class Solution3:  # O(n)
	def maximumTripletValue(self, nums):
		ans = max_diff = pre_max = 0
		for x in nums:
			ans = max(ans, max_diff * x)
			max_diff = max(max_diff, pre_max - x)
			pre_max = max(pre_max, x)
		return ans

if __name__ == '__main__':
	nums = [12,6,1,2,7]
	print(Solution2().maximumTripletValue(nums))