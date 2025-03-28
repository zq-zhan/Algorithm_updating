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

# 5.不同整数的最少数目
class Solution1:
	def findLeastNumOfUniqueInts(self, arr, k):
		arr = Counter(arr)
		n = len(arr)
		arr = sorted(arr.items(), key = lambda item: item[1])
		for i, (key, value) in enumerate(arr, 1):
			k -= value
			if k == 0:
				return n - i
			elif k < 0:
				return n - i + 1
		return 0
## 写法2
class Solution2:
	def findLeastNumOfUniqueInts(self, arr, k):
		arr = list(Counter(arr).values())
		arr.sort()
		while k > 0:
			if k > arr[0]:
				k -= arr.pop(0)
			else:
				k = 0
		return len(arr)

# 6.非递增顺序的最小子序列
class Solution1:
	def minSubsequence(self, nums):
		nums.sort(reverse = True)
		s = sum(nums)
		ans = []
		temp_ans = 0
		for x in nums:
			ans.append(x)
			temp_ans += x
			if temp_ans > s - temp_ans:
				break
		return ans

# 7.将数组分成最小总代价的子数组1
class Solution1:  # O(nlogn)
	def minimumCost(self, nums):
		new_arr = sorted(nums[1:])
		return nums[0] + sum(new_arr[:2])
## 灵神题解
class Solution2:
	def minimumCost(self, nums):  # O(n)
		return nums[0] + sum(nsmallest(2, nums[1:]))
##
class Solution3:  # O(n)
	def minimumCost(self, nums):
		new_arr = nums[1:]
		heapq.heapify(new_arr)
		return nums[0] + sum(heapq.heappop(new_arr) for _ in range(2))

# 8.数组大小减半
class Solution1:
	def minSetSize(self, arr):
		n = len(arr) // 2
		new_arr = sorted(Counter(arr).values(), reverse = True)
		for i, x in enumerate(new_arr, 1):
			n -= x
			if n <= 0:
				return i

# 9.卡车上的最大单元数
class Solution1:
	def maximumUnits(self, boxTypes, truckSize):
		boxTypes = sorted(boxTypes, key = lambda x: x[1], reverse = True)
		ans = 0
		for box_num, value in boxTypes:
			for _ in range(box_num):
				truckSize -= 1
				ans += value
				if truckSize == 0:
					return ans
		return ans
## 优化
class Solution2:
	def maximumUnits(self, boxTypes, truckSize):
		boxTypes = sorted(boxTypes, key = lambda x: -x[1])
		ans = 0
		for box_num, value in boxTypes:
			if box_num > truckSize:
				ans += truckSize * value
				return ans
			else:
				truckSize -= box_num
				ans += value * box_num
		return ans

# 10.幸福值最大化的选择方案
class Solution1:
	def maximumHappinessSum(self, happiness, k):
		happiness.sort(reverse = True)
		cnt = 0
		ans = 0
		for x in happiness:
			if k > 0:
				ans += max(x - cnt,0)
				cnt += 1
				k -= 1
			else:
				break
		return ans
## 灵神题解
class Solution2:
	def maximumHappinessSum(self, happiness, k):
		happiness.sort(reverse = True)
		ans = 0
		for i, x in enumerate(happiness[:k]):
			if x <= i:
				break
			ans += x - i
		return ans

# 11.从一个范围内选择最多整数1
class Solution1:
	def maxCount(self, banned, n, maxSum):
		ans = 0
		banned = list(set(banned))
		banned.sort()
		p1 = 0
		for x in range(1, n + 1):
			if p1 >= len(banned) or x != banned[p1]:
				maxSum -= x
				ans += 1
				if maxSum == 0:
					return ans
				elif maxSum < 0:
					return ans - 1
			else:
				p1 += 1
		return ans

# 12.摧毁小行星
class Solution1:
	def asteroidsDestroyed(self, mass, asteroids):
		# n = len(asteroids)
		asteroids.sort()
		while len(asteroids) > 0:
			i = bisect_right(asteroids, mass) - 1
			if i < 0:
				return False
			mass += asteroids[i]
			asteroids.pop(i)
		return True
## 优化
class Solution2:
	def asteroidsDestroyed(self, mass, asteroids):
		# n = len(asteroids)
		asteroids.sort()
		for x in asteroids:
			if mass >= x:
				mass += x
			else:
				return False
		return True

# 13.重组数组以得到最大前缀分数
class Solution1:
	def maxScore(self, nums):
		nums.sort(reverse = True)
		temp_s = 0
		for i, x in enumerate(nums, 1):
			temp_s += x
			if temp_s <= 0:
				return i - 1
		return i

# 14.三角形的最大周长
class Solution1:
	def largestPerimeter(self, nums):
		nums.sort(reverse = True)
		n = len(nums)
		for i in range(n - 2):
			if nums[i] >= nums[i + 1] + nums[i + 2]:
				continue
			else:
				return nums[i] + nums[i + 1] + nums[i + 2]
		return 0

# 15.你可以获得的最大硬币数目
class Solution1:
	def maxCoins(self, piles):
		ans = 0
		piles.sort(reverse = True)
		while len(piles) > 0:
			piles.pop(0)
			ans += piles.pop(0)
			piles.pop(-1)
		return ans
## 灵神题解
class Solution2:
	def maxCoins(self, piles):
		piles.sort()
		return sum(piles[len(piles)//3::2])

# 16.提取至多k个元素的最大总和
class Solution1:  # O(mnlog(mn))
	def maxSum(self, grid, limits, k):
		temp_lis = []
		for i, value_lis in enumerate(grid):
			for x in value_lis:
				temp_lis.append([i, x])
		temp_lis = sorted(temp_lis, key = lambda lis:-lis[1])

		ans = 0
		# cnt = 0
		for i, x in temp_lis:
			if limits[i] > 0:
				ans += x if k > 0 else 0
				k -= 1
				limits[i] -= 1
				if k == 0:
					return ans
			else:
				continue
		return ans
## 灵神题解
class Solution2:
	def maxSum(self, grid, limits, k):
		a = []
		for row, limit in zip(grid, limits):
			row.sort(reverse = True)
			a.extend(row[:limit])
		a.sort(reverse = True)
		return sum(a[:k])




















