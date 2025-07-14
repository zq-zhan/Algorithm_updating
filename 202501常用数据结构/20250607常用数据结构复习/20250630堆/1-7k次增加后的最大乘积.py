import heapq

class Solution:
	def maximumProduct(self, nums, k):
		mod = 10 ** 9 + 7
		ans = 1
		heapq.heapify(nums)
		for _ in range(k):
			x = heapq.heappop(nums)
			heapq.heappush(nums, x + 1)
		for x in nums:
			ans *= x
		return ans % mod

if __name__ == '__main__':
	nums = [0,4]
	k = 5
	print(Solution().maximumProduct(nums, k))