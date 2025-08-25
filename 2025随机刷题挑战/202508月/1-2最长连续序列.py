import heapq

# 58.最长连续序列
class Solution:
	def longestConsecutive(self, nums):
		nums = list(set(nums))
		heapq.heapify(nums)
		ans = temp_length = 0
		pre = 'a'
		while nums:
			if pre == 'a' or nums[0] - pre == 1:
				temp_length += 1
			else:
				temp_length = 1
			pre = heapq.heappop(nums)
			ans = max(ans, temp_length)
		return ans


if __name__ == '__main__':
	nums = [100,4,200,1,3,2]
	print(Solution().longestConsecutive(nums))