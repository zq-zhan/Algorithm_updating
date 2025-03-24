######## 基本贪心策略
# 1.重新分装苹果
class Solution1:
	def minimumBoxes(self, apple, capacity):
		capacity.sort(reverse = True)
		ans = 0
		for x in apple:
			while x > capacity[ans]:
				x -= capacity[ans]
				capacity[ans] = 0
				ans += 1
			capacity[ans] -= x
		return ans 
## 灵神思路
class Solution2:
	def minimumBoxes(self, apple, capacity):
		capacity.sort(reverse = True)
		s = sum(apple)
		for i, x in enumerate(capacity, 1):
			s -= x
			if s <= 0:
				return i

# 2.装满石头的背包的最大数量
class Solution1:
	def maximumBags(self, capacity, rocks, additionalRocks):
		capacity = [x - y for x, y in zip(capacity, rocks)]
		capacity.sort()
		for i, x in enumerate(capacity, 1):
			additionalRocks -= x
			if additionalRocks == 0:
				return i
			elif additionalRocks < 0:
				return i - 1
		return i

# 3.雪糕的最大数量
class Solution1:
	def maxIceCream(self, costs, coins):
		costs.sort()
		for i, c in enumerate(costs, 1):
			coins -= c
			if coins == 0:
				return i
			elif coins < 0:
				return i - 1
		return i

# 4.k次取反后最大化的数组和
class Solution1:
	def largestSumAfterKNegations(self, nums, k):
		heapq.heapify(nums)
		while k and nums:
			if nums[0] < 0:
				heapq.heappush(nums, -heapq.heappop(nums))
				k -= 1
			else:
				if nums[0] and k % 2:
					heapq.heappush(nums, -heapq.heappop(nums))
				break
		return sum(nums)





















