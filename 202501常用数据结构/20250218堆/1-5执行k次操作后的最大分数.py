# 5.执行k次操作后的最大分数
import heapq

## 复杂度 O(n + klogn)
class Solution1:
	def maxKelements(self, nums, k):
		nums = [-x for x in nums]
		heapq.heapify(nums)
		ans = 0
		for _ in range(k):
			pop_num = heapq.heappop(nums)
			ans += -pop_num
			heapq.heappush(nums, pop_num // 3)
		return ans
	
if __name__ == '__main__':
	nums = [10,10,10,10,10]
	k = 5
	print(Solution1().maxKelements(nums, k))