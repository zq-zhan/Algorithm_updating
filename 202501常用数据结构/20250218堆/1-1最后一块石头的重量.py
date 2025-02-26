# 1.最后一块石头的重量
import heapq

class Solution1:
	def lastStoneWeight(self, nums):
		nums.sort()
		while len(nums) > 1:
			y = nums.pop()
			x = nums.pop()
			if x == y:
				continue
			else:
				nums.append(y - x)
				nums.sort()
		return 0 if not nums else nums[-1]

## python最小堆
class Solution2:
	def lastStoneWeight(self, stones):
		heap = [-stone for stone in stones]
		heapq.heapify(heap)  # 将列表转化为堆

		while len(heap) > 1:
			x, y = heapq.heappop(heap), heapq.heappop(heap)
			if x != y:
				heapq.heappush(heap, x - y)

		if heap:
			return -heap[0]
		else:
			return 0
	
if __name__ == '__main__':
	nums = [2,7,4,1,8,1]
	print(Solution1().lastStoneWeight(nums))