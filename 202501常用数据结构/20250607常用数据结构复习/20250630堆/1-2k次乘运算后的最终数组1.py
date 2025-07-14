import heapq

class Solution:
	def getFinalState(self, nums, k, multiplier):
		nums = [(x, i) for i, x in enumerate(nums)]
		heapq.heapify(nums)
		while k > 0:
			mn, i = heapq.heappop(nums)
			heapq.heappush(nums, (mn * multiplier, i))
			k -= 1
		ans = sorted(nums, key = lambda x:x[1])
		return [x[0] for x in ans]
	
if __name__ == '__main__':
	nums = [2,1,3,5,6]
	k = 5
	multiplier = 2
	print(Solution().getFinalState(nums, k, multiplier))