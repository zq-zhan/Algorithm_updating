# 7.供暖器
from math import inf

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
		houses.sort()
		heaters.sort()
		left, right = -1, max(abs(max(houses) - min(heaters)), abs(min(houses) - max(heaters)))
		while left + 1 < right:
			mid = (left + right) // 2
			if self.check(houses, heaters, mid):
				right = mid
			else:
				left = mid
		return right
	
class Solution2:
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

if __name__ == '__main__':
	houses = [1,2,3,4]
	heaters = [1,4]
	# houses = [1]
	# heaters = [1,2,3,4]
	cls = Solution2()
	print(cls.findRadius(houses, heaters))