# 使结果不超过阈值的最小除数
class Solution1:
	def smallestDivisor(self, nums, threshold):
		nums.sort()
		for i in range(1,nums[-1] + 1):
			cum_sum = 0
			j = len(nums) - 1
			while j >= 0 and cum_sum <= threshold:
				cum_sum += nums[j] // i
				j -= 1

			if j < 0 and cum_sum <= threshold:
				return i
## 灵神二分法思路
class Solution2:
	def smallestDivisor(self, nums, threshold):
		left, right = 0, max(nums)
		while left + 1 < right:
			mid = (left + right) // 2
			if sum((x - 1) // mid for x in nums) <= threshold - len(nums):
				right = mid
			else:
				left = mid
		return right


# 2.完成旅途的最少时间
class Solution1:
	def minimumTime(self, time, totalTrips):
		left, right = 0, min(time) * totalTrips
		while left + 1 < right:
			mid = (left + right) // 2
			if sum(mid // x for x in time) >= totalTrips:
				right = mid
			else:
				left = mid
		return right
## 灵神思路：优化left, right边界
class Solution1:
	def minimumTime(self, time, totalTrips):
		left, right = min(time) - 1, min(time) * totalTrips
		while left + 1 < right:
			mid = (left + right) // 2
			if sum(mid // x for x in time) >= totalTrips:
				right = mid
			else:
				left = mid
		return right

# 3.准时到达的列车最小时速
class Solution1:
	def minSpeedOnTime(self, dist, hour):
		left, right = 0, max(dist)
		while left + 1 < right:
			mid = (left + right) // 2
			if ((sum((x - 1) // mid for x in dist[:-1]) * mid) + dist[-1]) * 100 <= hour - len(dist) + 1:
				right = mid
			else:
				left = mid
		if right == sum(dist):
			return -1
		return right
## 灵神思路
class Solution2:
	def minSpeedOnTime(self, dist, hour):
		n = len(dist)
		h100 = round(hour * 100)  # 去除浮点数影响
		if h100 <= (n - 1) * 100:  # 前面n-1个站至少花费n-1个小时，且还有最后一个站
			return -1

		max_dist = max(dist)
		if h100 <= n * 100:  # hour <= n的情况
			return max(max_dist, (dist[-1] * 100 - 1) // (h100 - (n - 1) * 100) + 1)

		def check(v):
			t = n - 1  # n-1个1
			for x in dist[:-1]:
				t += (x - 1) // v
			return (t * v + dist[-1]) * 100 <= h100 * v

		left, right = 0, max_dist
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				right = mid
			else:
				left = mid
		return right

# 4.在d天内送达包裹的能力
class Solution1:
	def check(self, weights, mid, days):
		n = len(weights)
		left = 0
		cum_sum = 0
		cnt = 0
		while left < n:
			while left < n and cum_sum + weights[left] <= mid:
				cum_sum += weights[left]
				left += 1
			cum_sum = 0
			cnt += 1
		return cnt <= days

	def shipWithinDays(self, weights, days):
		left, right = max(weights) - 1, sum(weights)
		while left + 1 < right:  # 开区间写法
			mid = (left + right) // 2
			if self.check(weights, mid, days):  # 核心是找到check函数
				right = mid
			else:
				left = mid
		return right

# 5.爱吃香蕉的珂珂
class Solution1:
	def minEatingSpeed(self, piles, h):
		left, right = 0, max(piles)
		while left + 1 < right:
			mid = (left + right) // 2
			if sum((x - 1) // mid for x in piles) <= h - len(piles):
				right = mid
			else:
				left = mid
		return right

# 6.移山所需的最小秒数
class Solution1:

	def check(self, mountainHeight, workerTimes, mid):
		cum_sum = 0
		for x in workerTimes:
			# cnt = 1
			# temp_cum_sum = 0
			# while temp_cum_sum + x * cnt <= mid:
			# 	temp_cum_sum += x * cnt
			# 	cnt += 1
			# cum_sum += cnt - 1
			ans = (sqrt(1 + 8 * mid // x) - 1) // 2
			cum_sum += ans
		return cum_sum >= mountainHeight

	def minNumberOfSeconds(self, mountainHeight, workerTimes):
		# min_time = min(workerTimes)
		# cnt = 1
		# right_cnt = 0
		# while cnt <= mountainHeight:
		# 	right_cnt += min_time * cnt
		# 	cnt += 1
		left, right = 0, max(workerTimes) * mountainHeight * (1 + mountainHeight) // 2
		while left + 1 < right:
			mid = (left + right) // 2
			if self.check(mountainHeight, workerTimes, mid):
				right = mid
			else:
				left = mid
		return right

# 7.供暖器
class Solution1:
	def check(self, houses, heaters, target):
		# for x in houses:
		# 	temp = min(abs(x - y) for y in heaters)
		# 	if temp <= mid:
		# 		continue
		# 	else:
		# 		return False
		# return True
		# p1 = p2 = 0
		# n, m = len(houses), len(heaters)
		# while p1 < n:
		# 	while p2 < m:
		# 		if abs(houses[p1] - heaters[p2]) > mid:
		# 			p2 += 1
		# 		else:
		# 			p2 = 0
		# 			break
		# 	if p2 == m:
		# 		return False
		# 	p1 += 1
		# return True
		## 在heaters中用二分找到最接近x的min
		heaters = [-inf] + heaters + [inf]
		for x in houses:
			left, right = 0, len(heaters)
			while left + 1 < right:
				mid = (left + right) // 2
				if heaters[mid] >= x:
					right = mid
				else:
					left = mid
			if min(abs(heaters[right] - x), abs(heaters[left] - x)) > target:
				return False
		return True

	def findRadius(self, houses, heaters):
		left, right = -1, max(abs(max(houses) - min(heaters)), abs(min(houses) - max(heaters)))
		while left + 1 < right:
			mid = (left + right) // 2
			if self.check(houses, heaters, mid):
				right = mid
			else:
				left = mid
		return right

class Solution2:
	def check(self, houses, heaters, target):
		## 在heaters中用二分找到最接近x的min
		heaters = [-inf] + heaters + [inf]
		left, right = 0, len(heaters)
		while left + 1 < right:
			mid = (left + right) // 2
			if heaters[mid] >= target:
				right = mid
			else:
				left = mid
		return min(abs(heaters[right] - x), abs(heaters[left] - x)) <= target

	def findRadius(self, houses, heaters):
		left, right = -1, max(abs(max(houses) - min(heaters)), abs(min(houses) - max(heaters)))
		new_arr = []
		for x in houses:
			new_arr.append(min(abs(x - heater) for heater in heaters))

		while left + 1 < right:
			mid = (left + right) // 2
			if max(new_arr) <= mid:
				right = mid
			else:
				left = mid
		return right



class Solution:
    def findRadius(self, houses, heaters):
        houses.sort()
        heaters.sort()
        heaters = [-inf] + heaters + [inf]
        res, n = 0, len(heaters)
        for i, x in enumerate(houses):
            # 灵神二分模板，找到离house[i]最近的heater[j]
            left, right = 0, n
            while left + 1 < right:
                mid = (left + right) // 2
                if heaters[mid] >= x:
                    right = mid
                else:
                    left = mid
            res = max(res, min(abs(heaters[right] - x), abs(heaters[left] - x)))

        return res
            
# 8.修车的最少时间
class Solution1:
	def check(self, ranks, cars, mid):
		ans = sum(isqrt(mid // x) for x in ranks)
		return ans >= cars
	def repairCars(self, ranks, cars):
		left, right = 0, min(ranks) * cars * cars
		while left + 1 < right:
			mid = (left + right) // 2
			if self.check(ranks, cars, mid):
				right = mid
			else:
				left = mid
		return right


			
