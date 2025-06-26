class Solution:
	def minimizeMax(self, nums, p):  # O(nk)
		if 0 == p:
			return 0
		nums.sort()
		max_diff = nums[-1] - nums[0]
		
		for diff in range(max_diff + 1):
			i = cnt = 0
			while i < len(nums) - 1:
				if nums[i + 1] - nums[i] <= diff:
					cnt += 1
					if cnt == p:
						return diff
					i += 2
				else:
					i += 1
## 灵神二分
class Solution:
	def minimizeMax(self, nums, p):
		nums.sort()
		def check(target):
			cnt = i = 0
			while i < len(nums) - 1:
				if nums[i + 1] - nums[i] <= target:
					cnt += 1
					i += 2
				else:
					i += 1
			return cnt >= p

		left, right = -1, nums[-1] - nums[0]
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				right = mid
			else:
				left = mid
		return right
	
if __name__ == '__main__':
	nums = [2,6,2,4,2,2,0,2]
	p = 4
	print(Solution2().minimizeMax(nums, p))