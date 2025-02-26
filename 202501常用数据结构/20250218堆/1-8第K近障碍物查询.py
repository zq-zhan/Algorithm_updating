# 14.第K近障碍物查询
import heapq

class Solution1:  # O(mlogn)
	def resultsArray(self, queries, k):
		nums = []
		ans = []
		heapq.heapify(nums)  # O(logn)
		for i, querie in enumerate(queries):
			heapq.heappush(nums, abs(querie[0]) + abs(querie[1]))
			if i >= k - 1:
				if i == k - 1:
					for _ in range(k - 1):
						heapq.heappop(nums)
				ans.append(nums[0])
			else:
				ans.append(-1)

		return ans
	
## 灵神题解：第k小——最大堆
class Solution2:
	def resultsArray(self, queries, k):
		ans = [-1] * len(queries)
		# heapq.heapify(ans)
		h = []
		for i, (x, y) in enumerate(queries):
			heapq.heappush(h, -abs(x) - abs(y))
			if len(h) > k:
				heapq.heappop(h)
			if len(h) == k:
				ans[i] = -h[0]
		return ans


	
if __name__ == '__main__':
	queries = [[6,10],[0,-10],[2,-6]]
	k = 2
	print(Solution2().resultsArray(queries, k))