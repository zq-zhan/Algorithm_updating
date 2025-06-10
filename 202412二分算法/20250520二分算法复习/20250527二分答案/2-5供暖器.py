from math import inf

class Solution1:
	def findRadius(self, houses, heaters):
		def check(target):
			heaters_new = []
			for i in range(len(heaters)):
				if i > 0 and heaters[i] - target <= heaters[i - 1] + target + 1:
					heaters_new[-1] = heaters[i] + target
					continue
				heaters_new.append(heaters[i] - target)
				heaters_new.append(heaters[i] + target)
			n = len(heaters_new)
			new_arr = []
			for j in range(0, n, 2):
				new_arr.extend(x for x in range(heaters_new[j], heaters_new[j + 1] + 1))
			for y in houses:
				if y in set(new_arr):
					continue
				return False
			return True


		houses.sort()
		left, right = -1, max(abs(max(houses) - min(heaters)),abs(min(houses) - max(heaters)))
		while left + 1 < right:
			mid = (left + right) // 2
			if check(mid):
				right = mid
			else:
				left = mid
		return right 
	
## 思路：找到离每个house[i]最近的heater[i]
class Solution2:
	def findRadius(self, houses, heaters):
		houses.sort()
		heaters.sort()
		heaters = [-inf] + heaters + [inf]
		res, n = 0, len(heaters)
		for i, x in enumerate(houses):
			left, right = 0, n - 1
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
	heaters = [1]
	print(Solution2().findRadius(houses, heaters))