import heapq

class Solution:
	def lastStoneWeight(self, nums):
		nums = [-x for x in nums]
		heapq.heapify(nums)
		while len(nums) > 1:
			y = heapq.heappop(nums)
			x = heapq.heappop(nums)
			if y != x:
				heapq.heappush(nums, y - x)
		return -heapq.heappop(nums) if nums else 0
	
if __name__ == '__main__':
	nums = [2,7,4,1,8,1]
	print(Solution().lastStoneWeight(nums))