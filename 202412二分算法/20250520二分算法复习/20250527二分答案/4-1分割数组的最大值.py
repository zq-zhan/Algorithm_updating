class Solution:
	def splitArray(self, nums, k):
		def check(target):
			cnt = temp_s = 0
			for x in nums:
				if temp_s + x <= target:
					temp_s += x
				else:
					cnt += 1
					temp_s = x
			return cnt + 1 <= k

		left, right = max(nums) - 1, sum(nums)
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				right = mid
			else:
				left = mid
		return right
	
if __name__ == '__main__':
	nums = [7, 2, 5, 10, 8]
	k = 2
	print(Solution().splitArray(nums, k))