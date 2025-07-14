from collections import Counter
import heapq

class Solution:
	def maxSubsequence(self, nums, k):
		new_arr = sorted(nums)
		target_s = Counter(new_arr[-k:])
		ans = []
		for x in nums:
			if target_s[x] > 0:
				ans.append(x)
				target_s[x] -= 1
			if len(ans) == k:
				break
		return ans
	
## 灵神题解
class Solution:
	def maxSubsequence(self, nums, k):
		idx = sorted(range(len(nums)), key = lambda x:nums[x])
		idx = sorted(idx[-k:])  # 取出前k大元素的下标，对下标再次排序
		return [nums[i] for i in idx]
## 最小堆模拟
class Solution:
	def maxSubsequence(self, nums, k):
		heap = []
		for i, num in enumerate(nums):
			if len(heap) < k:
				heapq.heappush(heap, (num, i))
			else:
				if num > heap[0][0]:
					heapq.heappop(heap)
					heapq.heappush(heap, (num, i))
		heap.sort(key = lambda x:x[1])
		return [num for num, i in heap]


if __name__ == '__main__':
	nums = [50,-75]
	k = 2
	print(Solution().maxSubsequence(nums, k))