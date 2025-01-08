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
	
if __name__ == '__main__':
	nums = [9]
	maxOperations = 2
	print(Solution1().minimumSize(nums, maxOperations)) # Output: 3