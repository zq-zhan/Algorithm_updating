# 2.k次乘运算后的最终数组1
import heapq

# 2.k次乘运算后的最终数组1
class Solution1:  # 错解
	def getFinalState(self, nums, k, multiplier):
		heapq.heapify(nums)
		while k > 0:
			x = heapq[0]
			heapq.heappop(nums)
			heapq.heappush(nums, x * multiplier)
			k -= 1
		return nums
##
class Solution2:
	def getFinalState(self, nums, k, multiplier):
		pq = [(x, i) for i, x in enumerate(nums)]
		heapq.heapify(pq)
		for _ in range(k):
			_, i = heapq.heappop(pq)
			nums[i] *= multiplier
			heapq.heappush(pq, (nums[i], i))
		return nums
	
class Solution:
    def getFinalState(self, nums, k, multiplier):
        for t in range(k):
            m = nums[0]
            index = 0
            for i in range(1, len(nums)):
                if nums[i] < m:
                    m, index = nums[i], i
            nums[index] *= multiplier
        return nums

##
class Solution3:
	def getFinalState(self, nums, k, multiplier):
		pq = [(x, i) for i, x in enumerate(nums)]
		heapq.heapify(pq)
		for _ in range(k):
			_, i = heapq.heappop(pq)  # 存储最小值的索引
			nums[i] *= multiplier
			heapq.heappush(pq, (nums[i], i))  # 将变换后的x根据其索引放回堆中
		return nums
	
if __name__ == '__main__':
	nums = [2,1,3,5,6]
	multiplier = 2
	k = 5
	print(Solution3().getFinalState(nums, 5, multiplier))