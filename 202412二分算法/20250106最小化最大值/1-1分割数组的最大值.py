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

if __name__ == '__main__':
	nums = [7, 2, 5, 10, 8]
	k = 2
	print(Solution1().splitArray(nums, k)) # Output: 18