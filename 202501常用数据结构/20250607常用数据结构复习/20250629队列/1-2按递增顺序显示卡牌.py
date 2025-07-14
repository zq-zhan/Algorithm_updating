from collections import deque

class Solution:
	def deckRevealedIncreasing(self, nums):
		nums.sort()
		index_lis = deque(range(len(nums)))

		ans = [0] * len(nums)
		for x in nums:
			ans[index_lis.popleft()] = x
			if index_lis:
				index_lis.append(index_lis.popleft())
		return ans
	
if __name__ == '__main__':
	nums = [17,13,11,2,3,5,7]
	print(Solution().deckRevealedIncreasing(nums))