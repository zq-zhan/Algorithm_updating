import heapq

class Solution:
	def halveArray(self, nums):
		nums = [-x for x in nums]
		heapq.heapify(nums)
		target_half = sum(nums) / 2
		temp_s = ans = 0
		while temp_s > target_half:
			x = heapq.heappop(nums)
			heapq.heappush(nums, x / 2)
			temp_s += x / 2
			ans += 1
		return ans

if __name__ == '__main__':
	nums = [5,19,8,1]
	print(Solution().halveArray(nums))