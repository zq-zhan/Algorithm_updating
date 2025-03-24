import heapq

# 4.k次取反后最大化的数组和
class Solution1:
	def largestSumAfterKNegations(self, nums, k):
		heapq.heapify(nums)
		while k and nums:
			if nums[0] < 0:
				heapq.heappush(nums, -heapq.heappop(nums))
				k -= 1
			else:
				if nums[0] and k % 2:
					heapq.heappush(nums, -heapq.heappop(nums))
				break
		return sum(nums)
	
if __name__ == '__main__':
	nums = [-4,-1,5,6]
	k = 3
	print(Solution1().largestSumAfterKNegations(nums, k)) # Output: 5