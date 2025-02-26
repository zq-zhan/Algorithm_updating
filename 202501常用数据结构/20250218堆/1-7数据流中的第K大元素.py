# 7.数据流中的第K大元素
import heapq

# class KthLargest:  # O(n + klogn)
# 	def __init__(self, k, nums):
# 		self.nums = [-x for x in nums]
# 		self.k = k

# 	def add(self, val):
# 		self.nums.append(-val)
# 		temp_heap = self.nums.copy()
# 		heapq.heapify(temp_heap)
# 		# heapq.heappush(temp_heap, -val)
# 		for _ in range(self.k - 1):
# 			heapq.heappop(temp_heap)  
# 		return -heapq.heappop(temp_heap)

## 优化
class KthLargest:  # O(logn)
	def __init__(self, k, nums):
		self.nums = nums
		self.k = k
		heapq.heapify(self.nums) # O(logn)

	def add(self, val):
		heapq.heappush(self.nums, val)
		while len(self.nums) > self.k:
			heapq.heappop(self.nums)  # O(logn),最多只需要进行一次heapq.heappop操作（第一次）
		return self.nums[0]

if __name__ == '__main__':
	kthLargest = KthLargest(3, [4, 5, 8, 2])
	print(kthLargest.add(3)) # 4
	print(kthLargest.add(5)) # 5
	print(kthLargest.add(10)) # 5
	print(kthLargest.add(9)) # 8
	print(kthLargest.add(4)) # 8